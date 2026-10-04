import sys
import pandas as pd
def test_legitimacy(grouped):
    for index, row in grouped.iterrows():
        if row["max"] > 100:
            print(index, row["min"], row["max"], row["mean"])
def fill_nans(grouped):
    grouped.fillna(method="ffill", inplace=True)
    return grouped
def make_negatives_nans(grouped):
    grouped["min"] = grouped["min"].apply(lambda x: float("nan") if x < 0 else x)
    grouped["max"] = grouped["max"].apply(lambda x: float("nan") if x < 0 else x)
    grouped["mean"] = grouped["mean"].apply(lambda x: float("nan") if x < 12.46 else x)
    return grouped
def group_data(df):
    grouped = df.groupby(pd.Grouper(freq="D"))["TemperatureF"].agg(["min", "max", "mean"])
    return grouped
def process_data(df):
    grouped = group_data(df)
    grouped = make_negatives_nans(grouped)
    grouped = fill_nans(grouped)
    return grouped
def main():
    try:
        df = pd.read_csv("temp_data_raw.csv", index_col="Time", parse_dates=True)
    except FileNotFoundError:
        print("Please run `scrape_data.py` to generate the raw data first.")
        sys.exit(0)
    df.drop(columns=[col for col in df.columns if "Unnamed" in col], inplace=True)
    grouped = process_data(df)
    test_legitimacy(grouped)
    grouped.to_csv("temp_data_cleaned.csv")
if __name__ == "__main__":
    main()