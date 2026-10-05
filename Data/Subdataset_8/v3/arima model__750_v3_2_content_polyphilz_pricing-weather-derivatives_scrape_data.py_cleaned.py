import io
import requests
import pandas as pd
from dateutil import parser, rrule
from datetime import datetime, time, date
import time
def get_temperature_data(station, day, month, year):
    url = "http:
    full_url = url.format(station, day, month, year)
    try:
        response = requests.get(full_url)
        data = response.text.replace("<br>", "")
        dataframe = pd.read_csv(io.StringIO(data), usecols=["Time", "TemperatureF"], index_col=False)
    except requests.exceptions.ConnectionError:
        print("Connection error occurred while fetching data for station {} on {}-{}-{}".format(station, day, month, year))
        return None
    except Exception as e:
        print("An error occurred: {}".format(e))
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
            weather_data = None
            while weather_data is None:
                weather_data = get_temperature_data(station, date.day, date.month, date.year)
                if weather_data is None:
                    print("Retrying in {} seconds".format(backoff_time))
                    time.sleep(backoff_time)
            data[station].append(weather_data)
        pd.concat(data[station]).to_csv("temp_data_raw.csv".format(station), index=False)
if __name__ == "__main__":
    main()