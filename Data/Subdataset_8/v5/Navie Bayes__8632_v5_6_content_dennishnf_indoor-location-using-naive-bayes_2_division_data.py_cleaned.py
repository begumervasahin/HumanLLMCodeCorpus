import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
plt.close('all')
DATA = "DATA_001_House"
path_data = f"data1_filtered_wifis/{DATA}/"
path_parts = [f"data2_divided_parts/{DATA}/part{i:02d}/" for i in range(1, 11)]
def read_and_shuffle_data(file_path):
    df = pd.read_csv(file_path, sep=" ")
    df = df.sample(frac=1)
    return df
def divide_and_save_data(data, parts_paths):
    num_intervals = int(0.1 * len(data))
    for i, part_path in enumerate(parts_paths, start=1):
        part_data = data.iloc[(i - 1) * num_intervals: i * num_intervals].reset_index(drop=True)
        part_data.to_csv(f"{part_path}R{i:03d}.csv", sep=' ', index=False)
        print("Saving:", f"{part_path}R{i:03d}.csv")
for file_path in glob.glob(path_data + "*.csv"):
    region_data = read_and_shuffle_data(file_path)
    divide_and_save_data(region_data, path_parts)