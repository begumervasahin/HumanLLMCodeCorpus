import pandas as pd
import numpy as np
import os
import glob
DATA = "DATA_001_House"
DATA_DIR = f"data1_filtered_wifis/{DATA}/"
PART_DIR = f"data2_divided_parts/{DATA}/part"
def read_and_shuffle_data(data_path):
    region_data = {}
    for idx, file_path in enumerate(glob.glob(f"{data_path}*.csv")):
        df_region = pd.read_csv(file_path, sep=" ")
        df_region = df_region.sample(frac=1).reset_index(drop=True)
        region_name = f"R{idx + 1:03d}"
        region_data[region_name] = df_region
        print("Reading and shuffling:", file_path)
    return region_data
def divide_and_save_parts(region_data):
    num_intervals = 10
    for region_name, df_region in region_data.items():
        num_rows = len(df_region)
        interval_size = num_rows
        for i in range(num_intervals):
            start_idx = i * interval_size
            end_idx = (i + 1) * interval_size
            part_df = df_region.iloc[start_idx:end_idx].reset_index(drop=True)
            part_path = f"{PART_DIR}{i + 1:02d}/"
            os.makedirs(part_path, exist_ok=True)
            part_file = f"{part_path}{region_name}.csv"
            part_df.to_csv(part_file, sep=' ', index=False)
            print("Saved part:", part_file)
if __name__ == "__main__":
    region_data = read_and_shuffle_data(DATA_DIR)
    divide_and_save_parts(region_data)