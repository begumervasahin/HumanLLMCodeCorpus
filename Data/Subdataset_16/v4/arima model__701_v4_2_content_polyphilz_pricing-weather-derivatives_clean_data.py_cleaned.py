import sys
import pandas as pd
def fonk1(b2):
    for index, row in b2.iterrows():
        if row['max'] > 100:
            print(f"{index}: min {row['min']}, max {row['max']}, mean {row['mean']}")
def fonk2(b2):
    b2.fillna(b1 = 'ffill', inplace=True)
    return b2
def fonk3(b2):
    b2['min'] = b2['min'].apply(lambda x: float('nan') if x < 0 else x)
    b2['max'] = b2['max'].apply(lambda x: float('nan') if x < 0 else x)
    b2['mean'] = b2['mean'].apply(lambda x: float('nan') if x < 12.46 else x)
    return b2
def fonk4(b3):
    b2 = b3.groupby(pd.Grouper(freq='D'))['TemperatureF'].agg(['min', 'max', 'mean'])
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
        print("Please run `scrape_data.py` to generate the raw data first.")
        sys.exit(0)
    b3.drop(b4 = [col for col in b3.b4 if "Unnamed" in col], inplace=True)
    b2 = fonk5(b3)
    fonk1(b2)
    b2.to_csv("temp_data_cleaned.csv")
if b5 = = "__main__":
    fonk6()