import sys
import pandas as pd
def fonk1(b2):
    for date, stats in b2.iterrows():
        if stats["max"] > 100:
            print(f"Date: {date}, Min: {stats['min']}, Max: {stats['max']}, Mean: {stats['mean']}")
def fonk2(b2):
    b2.fillna(b1 = "ffill", inplace=True)
    return b2
def fonk3(b2):
    b2["min"] = b2["min"].apply(lambda temp: float("nan") if temp < 0 else temp)
    b2["max"] = b2["max"].apply(lambda temp: float("nan") if temp < 0 else temp)
    b2["mean"] = b2["mean"].apply(lambda temp: float("nan") if temp < 12.46 else temp)
    return b2
def fonk4(b3):
    b2 = b3.groupby(pd.Grouper(freq="D"))["TemperatureF"].agg(["min", "max", "mean"])
    return b2
def fonk5(b3):
    b2 = fonk4(b3)
    b2 = fonk3(b2)
    b2 = fonk2(b2)
    return b2
def fonk6():
    try:
        b3 = pd.read_csv("temp_data_raw.csv", index_col="Time", parse_dates=True)
    except FileNotFoundError:
        print("Error: Please run `scrape_data.py` to generate the raw data first.")
        sys.exit(1)
    b3.drop(b4 = b3.b4[b3.b4.str.contains("Unnamed")], inplace=True)
    b2 = fonk5(b3)
    fonk1(b2)
    b2.to_csv("temp_data_cleaned.csv")
if b5 = = "__main__":
    fonk6()