import sys
import pandas as pd
def fonk1(b3):
    for date, row in b3.iterrows():
        if row['max'] > 100:
            print(f"{date}: min {row['min']}, max {row['max']}, mean {row['mean']}")
def fonk2(data):
    return data.fillna(b1 = 'ffill')
def fonk3(data):
    data['min'] = data['min'].apply(lambda x: float('nan') if x < 0 else x)
    data['max'] = data['max'].apply(lambda x: float('nan') if x < 0 else x)
    data['mean'] = data['mean'].apply(lambda x: float('nan') if x < 12.46 else x)
    return data
def fonk4(b4):
    return b4.groupby(pd.Grouper(b2 = 'D'))['TemperatureF'].agg(['min', 'max', 'mean'])
def fonk5(b4):
    b3 = fonk4(b4)
    b3 = fonk3(b3)
    b3 = fonk2(b3)
    return b3
def fonk6():
    try:
        b4 = pd.read_csv("temp_data_raw.csv", index_col="Time", parse_dates=True)
    except FileNotFoundError:
        print("Please run `scrape_data.py` to generate the raw data first.")
        sys.exit(0)
    b4.drop(b5 = [col for col in b4.b5 if "Unnamed" in col], inplace=True)
    b3 = fonk5(b4)
    fonk1(b3)
    b3.to_csv("temp_data_cleaned.csv")
if b6 = = "__main__":
    fonk6()