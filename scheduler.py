import time
from datetime import datetime


def At(date):
    
    # dd/mm/YY H:M:S
    dateTimeNowFormated = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    while dateTimeNowFormated < date:
        time.sleep(20)

        dateTimeNowFormated = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(dateTimeNowFormated + '   waiting for -->   ' + date)

    return

    
def Wait(mins):
    time.sleep(mins*60)

    return

def StartAt(date, period):
    At(date)
