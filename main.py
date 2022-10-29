from scraper import SendMessageTo
from scheduler import Wait, At


if __name__ == "__main__":

    #Wait(1)
    #At(29/10/2022 15:40:00)

    date = '29/10/2022 15:40:00'

    SendMessageTo('Name', f'Message scheduled at {date}', "https://web.whatsapp.com/", 1)

    At(date)
    SendMessageTo('Name','The message is: it works :D', "https://web.whatsapp.com/", 1)