import WeatherConfig
import requests
import json
from datetime import datetime
import pytz

class Meteorologist:
    def get_weather_data(self):
        response = requests.get(WeatherConfig.API_URL)
        data = json.loads(response.text)
        return data

    def clean_weather_data(self, raw_data):
        print("current: ", float(raw_data["current"]["temp"]) + WeatherConfig.K_C_DIFF)
        hourly = raw_data["hourly"]
        for entry in hourly:
            dt = datetime.fromtimestamp(entry["dt"], pytz.timezone(raw_data['timezone']))
            temp = float(entry["temp"]) + WeatherConfig.K_C_DIFF
            print(dt, temp)
