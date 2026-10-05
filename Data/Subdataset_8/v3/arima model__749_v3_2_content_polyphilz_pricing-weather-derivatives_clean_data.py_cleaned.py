import sys
import pandas as pd
def check_max_temperature(grouped):
    for index, row in grouped.iterrows():
        if row["max"] > 100:
            print(f"Date: {index}, Min Temp: {row['min']}, Max Temp: {row['max']}, Mean Temp: {row['mean']}")
def fill_missing_values(grouped):
    grouped.fillna(method="ffill", inplace=True)
    return grouped
def replace_negatives_with_nan(grouped):
    grouped["min"] = grouped["min"].apply(lambda x: float("nan") if x < 0 else x)
    grouped["max"] = grouped["max"].apply(lambda x: float("nan") if x < 0 else x)
    grouped["mean"] = grouped["mean"].apply(lambda x: float("nan") if x < 12.46 else x)
    return grouped
def group_temperature_data(df):
    grouped = df.groupby(pd.Grouper(freq="D"))["TemperatureF"].agg(
        ["min", "max", "mean"]
    )
    return grouped
def process_temperature_data(df):
    grouped = group_temperature_data(df)
    grouped = replace_negatives_with_nan(grouped)
    grouped = fill_missing_values(grouped)
    return grouped
def main():
    try:
        df = pd.read_csv("temp_data_raw.csv", index_col="Time", parse_dates=True)
    except FileNotFoundError:
        print("Please run `scrape_data.py` to generate the raw data first.")
        sys.exit(0)
    df.drop(df.columns[df.columns.str.contains("Unnamed")], axis=1, inplace=True)
    grouped = process_temperature_data(df)
    check_max_temperature(grouped)
    grouped.to_csv("temp_data_cleaned.csv")
if __name__ == "__main__":
    main()