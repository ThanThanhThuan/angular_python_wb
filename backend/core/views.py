from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import IndicatorData
from .analytics import generate_forecast

class IndicatorDataView(APIView):
    # Open to all authenticated users
    permission_classes = [IsAuthenticated]

    def get(self, request):
        c_code = request.query_params.get('country')
        i_code = request.query_params.get('indicator')
        
        data = IndicatorData.objects.filter(
            country_id=c_code, indicator_code=i_code
        ).values('year', 'value')
        
        return Response(list(data))

class ForecastView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Role check: Students shouldn't trigger expensive forecast computations
        if request.user.role == 'student':
            return Response({"error": "Upgrade to Researcher/Policymaker"}, status=403)

        c_code = request.query_params.get('country')
        i_code = request.query_params.get('indicator')
        
        forecast = generate_forecast(c_code, i_code)
        return Response(forecast)