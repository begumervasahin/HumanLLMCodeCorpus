import io
import requests
import pandas as pd
from dateutil import parser, rrule
from datetime import datetime, time, date
import time
def fonk1(station, day, month, year):
    b1 = "http:
    b2 = b1.format(station, day, month, year)
    try:
        b3 = requests.get(b2)
        b4 = b3.text.replace("<br>", "")
        b5 = pd.read_csv(io.StringIO(b4), usecols=["Time", "TemperatureF"], index_col=False)
    except requests.exceptions.ConnectionError:
        print("Connection error occurred while fetching b4 for station {} on {}-{}-{}".format(station, day, month, year))
        return None
    except Exception as e:
        print("An error occurred: {}".format(e))
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
        print("Working on station: {}".format(station))
        b4[station] = []
        for date in b10:
            if date.day % b12 = = 0:
                print("Working on date: {} for station {}".format(date, station))
            b13 = None
            while b13 is None:
                b13 = fonk1(station, date.day, date.month, date.year)
                if b13 is None:
                    print("Retrying in {} seconds".format(a1))
                    time.sleep(a1)
            b4[station].append(b13)
        pd.concat(b4[station]).to_csv("temp_data_raw.csv".format(station), b14 = False)
if b15 = = "__main__":
    fonk2()