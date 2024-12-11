import io
import requests
import pandas as pd
from dateutil import parser, rrule
from datetime import datetime, time, date
import time
def fonk1(station, day, month, year):
    b1 = "http:
    b2 = b1.format(station=station, day=day, month=month, year=year)
    b3 = requests.get(b2)
    b4 = b3.text
    b4 = b4.replace("<br>", "")
    try:
        b5 = pd.read_csv(io.StringIO(b4), usecols=["Time", "TemperatureF"], index_col=False)
    except:
        print("Issue with date: {}-{}-{} for station {}".format(day, month, year, station))
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
        print("Working on {}".format(station))
        b4[station] = []
        for date in b10:
            if date.day % b12 = = 0:
                print("Working on date: {} for station {}".format(date, station))
            b13 = False
            while not b13:
                try:
                    b14 = fonk1(station, date.day, date.month, date.year)
                    b13 = True
                except ConnectionError:
                    print("Got connection error on {}".format(date))
                    print("Will retry in {} seconds".format(a1))
                    time.sleep(a1)
            b4[station].append(b14)
        pd.concat(b4[station]).to_csv("temp_data_raw.csv".format(station))
if b15 = = "__main__":
    fonk2()