import os


# for weather api
SERVICE_KEY = os.environ.get('WEATHER_SERVICE_KEY')
ULTRA_SRT_URL = "http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtNcst"
VILAGE_URL = "http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst"
DATA_TYPE = "JSON"
NUM_OF_ROWS = "200"
PAGENO = "1"

# VilageFcst basetime calc
VILAGE_HOUR_SET = {2: 23, 5: 1, 8: 5, 11: 8, 14: 11, 17: 14, 20: 17, 23: 20}

# current location
NX = '62'
NY = '122'
