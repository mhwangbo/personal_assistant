from WeatherConfig import *
import requests
import json
from datetime import datetime
import pytz

class Meteorologist:
    def get_weather_data(self):
        response = requests.get(API_URL)
        data = json.loads(response.text)
        return data

    def clean_weather_data(self, raw_data):
        print("current: ", float(raw_data["current"]["temp"]) + K_C_DIFF)
        current = raw_data["current"]
        hourly = raw_data["hourly"]
        daily = raw_data["daily"]
        
        self._clean_current_data(current)
        self._clean_hourly_data(hourly)
        self._clean_daily_data(daily)

        # weather_dict = {"current": dict, "hourly": dict, "daily": dict}
        # for entry in hourly:
        #     dt = datetime.fromtimestamp(entry["dt"], pytz.timezone(raw_data['timezone']))
        #     temp = float(entry["temp"]) + WeatherConfig.K_C_DIFF
        #     print(dt, temp)

    def _clean_current_data(self, raw_data):
        current_dict = dict(CURRENT_W)
        for key in current_dict:
            try:
                current_dict[key] = raw_data[key]
            except:
                current_dict[key] = 0
        print(current_dict)

    def _clean_hourly_data(self, raw_data):
        hourly_data = []
        for each_hour in raw_data:
            hourly_dict = dict(HOURLY_W)
            for key in hourly_dict:
                try:
                    hourly_dict[key] = each_hour[key]
                except:
                    hourly_dict[key] = 0
            hourly_data.append(hourly_dict)
        print(hourly_data)


    def _clean_daily_data(self, raw_data):
        print(raw_data[0])

Meteorologist().clean_weather_data(Meteorologist().get_weather_data())