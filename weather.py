import glob
import json
import time
import urllib
import sys
import requests

import keys

def get_location():
    res = requests.get('http://ipinfo.io')
    if(res.status_code == 200):
        json_data = json.loads(res.text)
        return json_data
    return {}

def get_weather(api_key, location):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(location, api_key)
    r = requests.get(url)
    return r.json()


loc = get_location()
print(loc)

place = '{},{}'.format(loc['city'], loc['country'])
print(place)

weather = get_weather(keys.WEATHER_API, place)
print(weather)

temp = weather['main']['temp']
print(temp)

desc = weather['weather'][0]['main']
print(desc)

