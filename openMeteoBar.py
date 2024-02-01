#!/usr/bin/env python3
import openmeteo_requests

import requests_cache
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 00.00,
	"longitude": 00.00,
	"current": ["temperature_2m", "is_day", "rain", "snowfall", "cloud_cover", "wind_speed_10m"],
	"forecast_days": 1
}
responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]

# Current values. The order of variables needs to be the same as requested.
current = response.Current()
temperature_2m = current.Variables(0).Value()
is_day = current.Variables(1).Value()
rain = current.Variables(2).Value()
snowfall = current.Variables(3).Value()
cloud_cover = current.Variables(4).Value()
wind_speed_10m = current.Variables(5).Value()

# check if there's rain and snowfall
if rain == 1.0 and snowfall == 1.0:
    specialIcon = '󰙿 '
else:
    # check if there is rain or snow
	if rain == 1.0:
		specialIcon = '󰖗 ' 
	elif snowfall == 1.0:
		specialIcon = '󰖘 '
	else:
		specialIcon = ''
# check if there's day or night
if is_day == 1.0:
        # check for cloud coverage and wind speed during the day
    if cloud_cover > 50:
        if wind_speed_10m > 20:
            mainIcon = ""
        else:
            mainIcon = ""

    elif cloud_cover < 50:
        if wind_speed_10m > 20:
            mainIcon = ""
        else:
            mainIcon = ""

else:
    # check for cloud coverage and wind speed at night
    if cloud_cover > 50:
        if wind_speed_10m > 20:
            mainIcon = ""
        else:
            mainIcon = ""

    elif cloud_cover < 50:
        if wind_speed_10m > 20:
            mainIcon = ""
        else:
            mainIcon = ""

# check the temperature
if temperature_2m >= 30:
    temperatureIcon = ""  # Icon for very high temperature
elif 20 <= temperature_2m < 30:
    temperatureIcon = ""  # Icon for high temperature
elif 10 <= temperature_2m < 20:
    temperatureIcon = ""  # Icon for moderate temperature
elif 0 <= temperature_2m < 10:
    temperatureIcon = ""  # Icon for low temperature
else:
    temperatureIcon = ""  # Icon for very low temperature
    
if wind_speed_10m < 1:
    windIcon = ""
elif 1 <= wind_speed_10m <= 5:
    windIcon = ""
elif 6 <= wind_speed_10m <= 11:
    windIcon = ""
elif 12 <= wind_speed_10m <= 19:
    windIcon = ""
elif 20 <= wind_speed_10m <= 28:
    windIcon = ""
elif 29 <= wind_speed_10m <= 38:
    windIcon = ""
elif 39 <= wind_speed_10m <= 49:
    windIcon = ""
elif 50 <= wind_speed_10m <= 61:
    windIcon = ""
elif 62 <= wind_speed_10m <= 74:
    windIcon = ""
elif 75 <= wind_speed_10m <= 88:
    windIcon = ""
elif 89 <= wind_speed_10m <= 102:
    windIcon = ""
elif 103 <= wind_speed_10m <= 117:
    windIcon = ""
elif wind_speed_10m >= 118:
    windIcon = ""

print(f'{mainIcon}  {specialIcon}@ {temperatureIcon} {round(temperature_2m)}°C {windIcon} {round(wind_speed_10m)}km/s')
