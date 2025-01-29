import requests
from datetime import datetime

def fetch_prayer_times():
    latitude = 53.0333  # Portlaoise latitude
    longitude = -7.3000  # Portlaoise longitude
    calculation_method = 3  # Muslim World League (MWL)
    date = datetime.now().strftime("%d-%m-%Y")


    api_url = "http://api.aladhan.com/v1/timings"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "method": calculation_method,
        "date": date
    }

    # Build and print the full URL for debugging purposes
    full_url = f"{api_url}?latitude={params['latitude']}&longitude={params['longitude']}&method={params['method']}&date={params['date']}"
    print(f"API Request URL: {full_url}")

    # Make the request
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        return response.json()["data"]["timings"]
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")