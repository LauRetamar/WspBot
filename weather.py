import requests
import json

apiKey = '91f69fe9e12eb03409cedebefe42e###'

#Add locations
#
#

url1 = f'https://api.openweathermap.org/data/2.5/weather?lat={location1[0]}&lon={location1[1]}&appid={apiKey}'
url2 = f'https://api.openweathermap.org/data/2.5/weather?lat={location2[0]}&lon={location2[1]}&appid={apiKey}'

response = requests.get(f'{url2}')

data = response.json()

weather = 'weather: ' + (data['weather'][0]['description'])
temp = 'temp: ' + (((data['main']['temp'])-32)*(5/9))
pressure = 'pressure: ' + (data['main']['pressure'])
humidity = 'humidity: ' + (data['main']['humidity'])
visibility = 'visibility: ' + (data['visibility'])
windSpeed = 'wind speed: ' + ((data['wind']['speed'])*1,60934)
