import os


# current location
LAT = '37.23825'
LON = '127.17795'

# for weather api
API_KEY = os.environ.get('WEATHER_API_KEY')
API_URL = f"https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LON}&appid={API_KEY}"

# calculate temp
K_C_DIFF = -273.15

# dict for weather data
CURRENT_W = {"temp": 0, "feels_like": 0, "humidity": 0, "clouds": 0, "wind_speed": 0, "rain": 0, "snow": 0}
HOURLY_W = {"dt": "", "temp": 0, "feels_like": 0, "humidity": 0, "cloud": 0, "wind_speed": 0, "rain": 0, "snow": 0}
DAILY_W = {"dt": "", "temp_min": 0, "temp_max": 0, "humidity": 0, "cloud": 0, "wind_speed": 0, "rain": }