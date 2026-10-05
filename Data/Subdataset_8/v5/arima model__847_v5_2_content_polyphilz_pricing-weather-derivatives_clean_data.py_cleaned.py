import sys
import pandas as pd
def check_temperature_legitimacy(grouped_data):
    for date, row in grouped_data.iterrows():
        if row["max"] > 100:
            print(f"Date: {date}, Min Temp: {row['min']}, Max Temp: {row['max']}, Mean Temp: {row['mean']}")
def fill_missing_temperature_values(grouped_data):
    grouped_data.fillna(method="ffill", inplace=True)
    return grouped_data
def replace_negative_temperature_values_with_nan(grouped_data):
    grouped_data["min"] = grouped_data["min"].apply(lambda x: float("nan") if x < 0 else x)
    grouped_data["max"] = grouped_data["max"].apply(lambda x: float("nan") if x < 0 else x)
    grouped_data["mean"] = grouped_data["mean"].apply(lambda x: float("nan") if x < 12.46 else x)
    return grouped_data
def group_temperature_data_by_day(df):
    grouped_data = df.groupby(pd.Grouper(freq="D"))["TemperatureF"].agg(
        ["min", "max", "mean"]
    )
    return grouped_data
def process_temperature_data(df):
    grouped_data = group_temperature_data_by_day(df)
    grouped_data = replace_negative_temperature_values_with_nan(grouped_data)
    grouped_data = fill_missing_temperature_values(grouped_data)
    return grouped_data
def main():
    try:
        df = pd.read_csv("temp_data_raw.csv", index_col="Time", parse_dates=True)
    except FileNotFoundError:
        print("Please run `scrape_data.py` to generate the raw data first.")
        sys.exit(1)
    df.drop(df.columns[df.columns.str.contains("Unnamed")], axis=1, inplace=True)
    grouped_data = process_temperature_data(df)
    check_temperature_legitimacy(grouped_data)
    grouped_data.to_csv("temp_data_cleaned.csv")
if __name__ == "__main__":
    main()