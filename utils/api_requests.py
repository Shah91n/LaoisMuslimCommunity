import requests
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def get_prayer_data():
    latitude = os.getenv('PORTLAOISE_LATITUDE', '53.0333')
    longitude = os.getenv('PORTLAOISE_LONGITUDE', '-7.3000')
    calculation_method = 3  # Muslim World League (MWL)
    date = datetime.now().strftime("%d-%m-%Y")

    api_url = "http://api.aladhan.com/v1/timings" + f"/{date}"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "method": calculation_method,
        "date": date
    }

    # Build and print the full URL for debugging purposes
    full_url = f"{api_url}?latitude={params['latitude']}&longitude={params['longitude']}&method={params['method']}"
    print(f"Endpoint Request: {full_url}")

    # Make the request
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        response_json = response.json()
        # print(response_json)  # Print the full response for debugging
        return response_json  # Return the full response
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")
