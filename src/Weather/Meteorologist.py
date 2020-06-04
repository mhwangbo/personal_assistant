import WeatherConfig

from datetime import datetime
from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import urllib
import json
import os
import pandas as pd


class Meteorologist:
    def get_weather_data(self):
        current_time = datetime.now()
        ultra_srt_ncst = _UltraSrtNcst().get_ultra_srt_ncst(current_time)
        vilage_fcst = _VilageFcst().get_vilage_fcst(current_time)
        return [ultra_srt_ncst, vilage_fcst]

# 초단기실황조회
class _UltraSrtNcst:
    def get_ultra_srt_ncst(self, current_time):
        base_date, base_time = self._get_base_time(current_time)
        try:
            return _Common().get_fcst_from_api(
                api_url = WeatherConfig.ULTRA_SRT_URL,
                base_date = base_date,
                base_time = base_time
            )
        except Exception as e:
            print(e)
            return None

    def _get_base_time(self, current_time):
        date = int(current_time.strftime('%Y%m%d'))
        hour = int(current_time.strftime('%H'))
        minute = int(current_time.strftime('%M'))
        # calculate base time for ultra short cast
        # report update every 30 min
        if minute < 40:
            hour -= 1
        if hour < 0:
            hour = 23
            date -= 1
        return [str(date), str(hour).zfill(2) + "00"]

# 동네예보조회
class _VilageFcst:
    def get_vilage_fcst(self, current_time):
        base_date, base_time = self._get_base_time(current_time)
        try:
            return _Common().get_fcst_from_api(
                api_url = WeatherConfig.VILAGE_URL,
                base_date = base_date,
                base_time = base_time
            )
        except Exception as e:
            print(e)
            return None

    def _get_base_time(self, current_time):
        date = int(current_time.strftime('%Y%m%d'))
        hour = int(current_time.strftime('%H'))
        minute = int(current_time.strftime('%M'))
        if minute < 10:
            hour -= 1
        if hour < 2:
            return [str(date - 1), str(23).zfill(2) + "00"]
        for max_hour, base_hour in WeatherConfig.VILAGE_HOUR_SET.items():
            if hour < max_hour:
                return [str(date), str(base_hour).zfill(2) + "00"]

class _Common:
    def get_fcst_from_api(self, api_url, base_date, base_time):
        base_params = '?' + urlencode({
            quote_plus("serviceKey"): WeatherConfig.SERVICE_KEY,
            quote_plus("numOfRows"): WeatherConfig.NUM_OF_ROWS,
            quote_plus("pageNo"): WeatherConfig.PAGENO,
            quote_plus("dataType"): WeatherConfig.DATA_TYPE,
            quote_plus('nx'): WeatherConfig.NX,
            quote_plus('ny'): WeatherConfig.NY,
            quote_plus('base_date'): base_date,
            quote_plus('base_time'): base_time
        })
        try:
            req = urllib.request.Request(api_url + unquote(base_params))
            response_body = urlopen(req).read()
            data = json.loads(response_body)
            res = data
        except Exception as e:
            print(e)
            res = None
        return res