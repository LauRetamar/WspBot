import requests
import json
import math

apiKey = '91f69fe9e12eb03409cedebefe42e###'

location1 = ['-##.##00', '-##.##00']

url1 = f'https://api.openweathermap.org/data/2.5/weather?lat={location1[0]}&lon={location1[1]}&appid={apiKey}'
#url2 = f'https://api.openweathermap.org/data/2.5/weather?lat={location2[0]}&lon={location2[1]}&appid={apiKey}'

def GetWeatherInformation():

    response = requests.get(f'{url1}')
    data = response.json()

    print(data)

    weather = 'Weather: ' + str(data['weather'][0]['description'])
    temp = 'Temp: ' + str(round   (((data['main']['temp'])-273.15), 1))
    pressure = 'Pressure: ' + str(data['main']['pressure'])
    humidity = 'Humidity: ' + str(data['main']['humidity'])
    visibility = 'Visibility: ' + str(data['visibility'])
    windSpeed = 'Wind speed m/s: ' + str(data['wind']['speed'])

    info = f'{weather} \n {temp} \n {pressure} \n {humidity} \n {visibility} \n {windSpeed}' 

    return info