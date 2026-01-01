import pandas as pd
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
from .models import IndicatorData

def generate_forecast(country_code, indicator_code, years_ahead=5):
    # 1. Fetch data from DB
    queryset = IndicatorData.objects.filter(
        country_id=country_code, 
        indicator_code=indicator_code
    ).order_by('year')
    
    if not queryset.exists():
        return []

    # 2. Prepare DataFrame
    df = pd.DataFrame(list(queryset.values('year', 'value')))
    df.set_index('year', inplace=True)
    
    # 3. Model Training
    model = SimpleExpSmoothing(df['value']).fit(smoothing_level=0.2, optimized=False)
    
    # 4. Predict
    last_year = df.index.max()
    forecast_values = model.forecast(years_ahead)
    
    results = []
    for i, val in enumerate(forecast_values):
        results.append({
            'year': last_year + i + 1,
            'value': round(val, 2),
            'type': 'forecast'
        })
        
    return results