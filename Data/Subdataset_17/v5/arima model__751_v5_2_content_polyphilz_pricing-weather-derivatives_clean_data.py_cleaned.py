import sys
import pandas as pd
def check_temperature_legitimacy(grouped_data):
    for date, row in grouped_data.iterrows():
        if row['max'] > 100:
            print(f"{date}: min {row['min']}, max {row['max']}, mean {row['mean']}")
def fill_missing_values(data):
    return data.fillna(method='ffill')
def replace_invalid_values_with_nans(data):
    data['min'] = data['min'].apply(lambda x: float('nan') if x < 0 else x)
    data['max'] = data['max'].apply(lambda x: float('nan') if x < 0 else x)
    data['mean'] = data['mean'].apply(lambda x: float('nan') if x < 12.46 else x)
    return data
def group_temperature_data_by_day(df):
    return df.groupby(pd.Grouper(freq='D'))['TemperatureF'].agg(['min', 'max', 'mean'])
def process_temperature_data(df):
    grouped_data = group_temperature_data_by_day(df)
    grouped_data = replace_invalid_values_with_nans(grouped_data)
    grouped_data = fill_missing_values(grouped_data)
    return grouped_data
def main():
    try:
        df = pd.read_csv("temp_data_raw.csv", index_col="Time", parse_dates=True)
    except FileNotFoundError:
        print("Please run `scrape_data.py` to generate the raw data first.")
        sys.exit(0)
    df.drop(columns=[col for col in df.columns if "Unnamed" in col], inplace=True)
    grouped_data = process_temperature_data(df)
    check_temperature_legitimacy(grouped_data)
    grouped_data.to_csv("temp_data_cleaned.csv")
if __name__ == "__main__":
    main()