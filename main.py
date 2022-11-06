from sender import StartAt, SendAt
from weather import GetWeatherInformation


if __name__ == "__main__":

    #Wait(1)
    #At(29/10/2022 15:40:00)

    date = '06/11/2022 17:46:00'
    name = "Bot"
    period = 1440

    message = GetWeatherInformation()


    SendAt(date,name,message)
    