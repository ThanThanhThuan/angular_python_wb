import requests
from .models import Country, IndicatorData

def sync_world_bank_data(country_code, indicator_code):
    # World Bank API URL
    url = f"http://api.worldbank.org/v2/country/{country_code}/indicator/{indicator_code}?format=json&per_page=1000"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if len(data) > 1:
            records = data[1]
            for item in records:
                if item['value'] is not None:
                    IndicatorData.objects.update_or_create(
                        country_id=country_code,
                        indicator_code=indicator_code,
                        year=int(item['date']),
                        defaults={'value': float(item['value'])}
                    )