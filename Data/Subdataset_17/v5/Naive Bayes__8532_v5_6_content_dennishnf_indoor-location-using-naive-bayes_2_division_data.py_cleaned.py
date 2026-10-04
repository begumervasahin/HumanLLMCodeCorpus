import os
import glob
import pandas as pd
def create_output_directories(output_paths):
    for path in output_paths:
        os.makedirs(path, exist_ok=True)
def determine_regions_and_aps(path_data):
    num_regions = 0
    num_aps = 0
    for fullname in glob.glob(os.path.join(path_data, "*.csv")):
        df_in_region = pd.read_csv(fullname, sep=" ")
        num_aps = len(df_in_region.columns)
        num_regions += 1
    regions = [f"R{str(i).zfill(3)}" for i in range(1, num_regions + 1)]
    aps = [f"W{str(i).zfill(3)}" for i in range(1, num_aps + 1)]
    return num_regions, regions, aps
def read_and_shuffle_data(path_data, regions, aps):
    data = {}
    for region in regions:
        filename = f"{region}.csv"
        filepath = os.path.join(path_data, filename)
        df = pd.read_csv(filepath, sep=" ")
        print(f"Reading: {filepath}")
        data[region] = df[aps].sample(frac=1).reset_index(drop=True)
        print(f"Shuffling {region}")
    return data
def split_and_save_data(data, regions, output_paths):
    for region in regions:
        num_interval = len(data[region])
        for i in range(10):
            part_key = f"{region}_part{str(i + 1).zfill(2)}"
            start_idx = i * num_interval
            end_idx = (i + 1) * num_interval
            data_part = data[region].iloc[start_idx:end_idx].reset_index(drop=True)
            output_filename = f"{region}.csv"
            output_path = output_paths[i]
            output_filepath = os.path.join(output_path, output_filename)
            data_part.to_csv(output_filepath, sep=' ', index=False)
            print(f"Saving {output_filepath}")
def main():
    DATA = "DATA_001_House"
    path_data = f"data1_filtered_wifis/{DATA}/"
    output_paths = [f"data2_divided_parts/{DATA}/part{str(i).zfill(2)}/" for i in range(1, 11)]
    create_output_directories(output_paths)
    num_regions, regions, aps = determine_regions_and_aps(path_data)
    data = read_and_shuffle_data(path_data, regions, aps)
    split_and_save_data(data, regions, output_paths)
    print("Data splitting and saving completed.")
if __name__ == "__main__":
    main()