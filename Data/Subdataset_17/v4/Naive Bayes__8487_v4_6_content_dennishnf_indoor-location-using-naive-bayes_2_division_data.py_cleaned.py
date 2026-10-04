import os
import glob
import pandas as pd
DATA = "DATA_001_House"
path_data = f"data1_filtered_wifis/{DATA}/"
output_paths = [f"data2_divided_parts/{DATA}/part{str(i).zfill(2)}/" for i in range(1, 11)]
for path in output_paths:
    if not os.path.exists(path):
        os.makedirs(path)
numRegions = 0
for fullname in glob.glob(path_data + "*.csv"):
    dfInRegion = pd.read_csv(fullname, sep=" ")
    numAPs = len(dfInRegion.columns)
    numRegions += 1
Regions = [f"R{str(i).zfill(3)}" for i in range(1, numRegions + 1)]
APs = [f"W{str(i).zfill(3)}" for i in range(1, numAPs + 1)]
data = {}
for region in Regions:
    filename = f"{region}.csv"
    filepath = os.path.join(path_data, filename)
    data[region + "_"] = pd.read_csv(filepath, sep=" ")
    data[region] = data[region + "_"][APs]
    print(f"Reading: {filepath}")
    data[region] = data[region].sample(frac=1).reset_index(drop=True)
    print(f"Shuffling {region}")
for region in Regions:
    num_interval = int(0.1 * len(data[region]))
    for i in range(10):
        part_key = f"{region}_part{str(i + 1).zfill(2)}"
        start_idx = i * num_interval
        end_idx = (i + 1) * num_interval
        data[part_key] = data[region].iloc[start_idx:end_idx].reset_index(drop=True)
        output_filename = f"{region}.csv"
        output_path = output_paths[i]
        output_filepath = os.path.join(output_path, output_filename)
        data[part_key].to_csv(output_filepath, sep=' ', index=False)
        print(f"Saving {output_filepath}")
print("Data splitting and saving completed.")