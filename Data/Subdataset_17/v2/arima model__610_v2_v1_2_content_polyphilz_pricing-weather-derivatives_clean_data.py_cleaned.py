import sys
import pandas as pd
def check_temperature_legitimacy(daily_stats):
    for date, stats in daily_stats.iterrows():
        if stats["max"] > 100:
            print(f"Date: {date}, Min: {stats['min']}, Max: {stats['max']}, Mean: {stats['mean']}")
def fill_missing_values(daily_stats):
    daily_stats.fillna(method="ffill", inplace=True)
    return daily_stats
def replace_invalid_values(daily_stats):
    daily_stats["min"] = daily_stats["min"].apply(lambda temp: float("nan") if temp < 0 else temp)
    daily_stats["max"] = daily_stats["max"].apply(lambda temp: float("nan") if temp < 0 else temp)
    daily_stats["mean"] = daily_stats["mean"].apply(lambda temp: float("nan") if temp < 12.46 else temp)
    return daily_stats
def aggregate_daily_temperatures(df):
    daily_stats = df.groupby(pd.Grouper(freq="D"))["TemperatureF"].agg(["min", "max", "mean"])
    return daily_stats
def process_temperature_data(df):
    daily_stats = aggregate_daily_temperatures(df)
    daily_stats = replace_invalid_values(daily_stats)
    daily_stats = fill_missing_values(daily_stats)
    return daily_stats
def main():
    try:
        df = pd.read_csv("temp_data_raw.csv", index_col="Time", parse_dates=True)
    except FileNotFoundError:
        print("Error: Please run `scrape_data.py` to generate the raw data first.")
        sys.exit(1)
    df.drop(columns=df.columns[df.columns.str.contains("Unnamed")], inplace=True)
    daily_stats = process_temperature_data(df)
    check_temperature_legitimacy(daily_stats)
    daily_stats.to_csv("temp_data_cleaned.csv")
if __name__ == "__main__":
    main()