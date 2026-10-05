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
    data = response.text
    data = data.replace("<br>", "")
    try:
        dataframe = pd.read_csv(io.StringIO(data), usecols=["Time", "TemperatureF"])
    except Exception as e:
        print(f"Issue with date: {day}-{month}-{year} for station {station}")
        print(e)
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
        print(f"Working on {station}")
        data[station] = []
        for date in dates:
            if date.day % 10 == 0:
                print(f"Working on date: {date} for station {station}")
            done = False
            while not done:
                try:
                    weather_data = get_temperature_data(station, date.day, date.month, date.year)
                    done = True
                except ConnectionError:
                    print(f"Got connection error on {date}")
                    print(f"Will retry in {backoff_time} seconds")
                    time.sleep(backoff_time)
            if weather_data is not None:
                data[station].append(weather_data)
        if data[station]:
            pd.concat(data[station]).to_csv(f"temp_data_raw_{station}.csv", index=False)
if __name__ == "__main__":
    main()