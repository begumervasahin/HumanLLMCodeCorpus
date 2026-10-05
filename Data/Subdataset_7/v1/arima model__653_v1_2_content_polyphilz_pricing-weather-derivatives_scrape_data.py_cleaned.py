import io
import requests
import pandas as pd
from dateutil import parser, rrule
from datetime import datetime, time, date
import time
def fonk1(station, day, month, year):
    b1 = (
        "http:
    )
    b2 = b1.format(station=station, day=day, month=month, year=year)
    b3 = requests.get(b2)
    b4 = b3.text
    b4 = b4.replace("<br>", "")
    try:
        b5 = pd.read_csv(
            io.StringIO(b4), b6 = ["Time", "TemperatureF"], index_col=False
        )
    except:
        print(
            "Issue with date: {}-{}-{} for station {}".format(day, month, year, station)
        )
        return None
    return b5
def fonk2():
    b7 = "2010-07-30"
    b8 = "2018-07-30"
    b9 = parser.parse(b7)
    b10 = parser.parse(b8)
    b11 = list(rrule.rrule(rrule.DAILY, dtstart=b9, until=b10))
    b12 = ["KCASANFR49"]
    a1 = b13
    b4 = {}
    for station in b12:
        print("Working on {}".format(station))
        b4[station] = []
        for date in b11:
            if date.day % b13 = = 0:
                print("Working on date: {} for station {}".format(date, station))
            b14 = False
            while not b14:
                try:
                    b15 = fonk1(
                        station, date.day, date.month, date.year
                    )
                    b14 = True
                except requests.exceptions.ConnectionError:
                    print("Got connection error on {}".format(date))
                    print("Will retry in {} seconds".format(a1))
                    time.sleep(a1)
            if b15 is not None:
                b4[station].append(b15)
        pd.concat(b4[station]).to_csv("temp_data_raw.csv".format(station), b16 = False)
if b17 = = "__main__":
    fonk2()