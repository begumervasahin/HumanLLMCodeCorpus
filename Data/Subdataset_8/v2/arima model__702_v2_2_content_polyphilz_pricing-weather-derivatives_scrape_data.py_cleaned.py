import io
import requests
import pandas as pd
from dateutil import parser, rrule
from datetime import datetime, time, date
import time
def get_temperature_data(station, day, month, year):
    url = "http:
    full_url = url.format(station, day, month, year)
    response = requests.get(full_url)
    data = response.text.replace("<br>", "")
    try:
        dataframe = pd.read_csv(io.StringIO(data), usecols=["Time", "TemperatureF"], index_col=False)
    except:
        print("Issue with date: {}-{}-{} for station {}".format(day, month, year, station))
        return None
    return dataframe
def main():
    start_date = "2010-07-30"
    end_date = "2018-07-30"
    start = parser.parse(start_date)
    end = parser.parse(end_date)
    dates = list(rrule.rrule(rrule.DAILY, dtstart=start, until=end))
    stations = ["KCASANFR49"]
    backoff_time = 10
    data = {}
    for station in stations:
        print("Working on station: {}".format(station))
        data[station] = []
        for date in dates:
            if date.day % 10 == 0:
                print("Working on date: {} for station {}".format(date, station))
            done = False
            while not done:
                try:
                    weather_data = get_temperature_data(station, date.day, date.month, date.year)
                    done = True
                except requests.exceptions.ConnectionError:
                    print("Connection error occurred on {}".format(date))
                    print("Retrying in {} seconds".format(backoff_time))
                    time.sleep(backoff_time)
            if weather_data is not None:
                data[station].append(weather_data)
        pd.concat(data[station]).to_csv("temp_data_raw.csv".format(station), index=False)
if __name__ == "__main__":
    main()