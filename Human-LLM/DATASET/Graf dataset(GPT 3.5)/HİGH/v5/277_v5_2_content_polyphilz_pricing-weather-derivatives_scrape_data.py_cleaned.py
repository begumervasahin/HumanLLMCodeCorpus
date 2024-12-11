import io
import requests
import pandas as pd
from dateutil import parser, rrule
from datetime import datetime, time, date
import time
def fonk1(station, day, month, year):
    b1 = "http:
    b2 = b1.format(station, day, month, year)
    b3 = requests.get(b2)
    b4 = b3.text
    b4 = b4.replace("<br>", "")
    try:
        b5 = pd.read_csv(io.StringIO(b4), usecols=["Time", "TemperatureF"])
    except Exception as e:
        print(f"Issue with date: {day}-{month}-{year} for station {station}")
        print(e)
        return None
    return b5
def fonk2():
    b6 = "2010-07-30"
    b7 = "2018-07-30"
    b8 = parser.parse(b6)
    b9 = parser.parse(b7)
    b10 = list(rrule.rrule(rrule.DAILY, dtstart=b8, until=b9))
    b11 = ["KCASANFR49"]
    a1 = b12
    b4 = {}
    for station in b11:
        print(f"Working on {station}")
        b4[station] = []
        for date in b10:
            if date.day % b12 = = 0:
                print(f"Working on date: {date} for station {station}")
            b13 = False
            while not b13:
                try:
                    b14 = fonk1(station, date.day, date.month, date.year)
                    b13 = True
                except ConnectionError:
                    print(f"Got connection error on {date}")
                    print(f"Will retry in {a1} seconds")
                    time.sleep(a1)
            if b14 is not None:
                b4[station].append(b14)
        if b4[station]:
            pd.concat(b4[station]).to_csv(f"temp_data_raw_{station}.csv", b15 = False)
if b16 = = "__main__":
    fonk2()