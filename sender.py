from scheduler import At, Wait
from scraper import SendMessageTo

def WaitAndSend(time,name,message):

    Wait(time)
    SendMessageTo(f'{name}', f'{message}', "https://web.whatsapp.com/", 1)


def SendAt(date,name,message):
    At(date)
    SendMessageTo(f'{name}', f'{message}', "https://web.whatsapp.com/", 1)


def StartAt(date,period,name,message):
    At(date)

    while(True):
        SendMessageTo(f'{name}', f'{message}', "https://web.whatsapp.com/", 1)
        Wait(period)
