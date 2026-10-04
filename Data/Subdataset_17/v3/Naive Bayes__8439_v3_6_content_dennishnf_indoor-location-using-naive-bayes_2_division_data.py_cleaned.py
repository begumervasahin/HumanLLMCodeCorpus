import os
import glob
import pandas as pd
DATA = "DATA_001_House"
PATH_DATA = f"data1_filtered_wifis/{DATA}/"
PATH_PARTS = f"data2_divided_parts/{DATA}/part{{:02d}}/"
def create_directories():
    for part_num in range(1, 11):
        os.makedirs(PATH_PARTS.format(part_num), exist_ok=True)
def load_region_files():
    region_files = glob.glob(PATH_DATA + "*.csv")
    num_regions = len(region_files)
    regions = [f"R{str(i).zfill(3)}" for i in range(1, num_regions + 1)]
    return region_files, regions
def get_number_of_aps(region_file):
    num_aps = len(pd.read_csv(region_file, sep=" ").columns)
    return num_aps
def load_data(regions):
    data = {region: pd.read_csv(PATH_DATA + f"{region}.csv", sep=" ") for region in regions}
    return data
def shuffle_and_divide_data(data, regions):
    divided_data = {}
    for region in regions:
        data[region] = data[region].sample(frac=1).reset_index(drop=True)
        num_interval = int(0.1 * len(data[region]))
        for part_num in range(1, 11):
            start_index = ((part_num - 1) % 5) * num_interval
            end_index = start_index + num_interval
            divided_data[f"{region}_part{str(part_num).zfill(2)}"] = data[region].iloc[start_index:end_index]
    return divided_data
def save_divided_data(divided_data, regions):
    for region in regions:
        for part_num in range(1, 11):
            part_name = f"{region}_part{str(part_num).zfill(2)}.csv"
            part_path = os.path.join(PATH_PARTS.format(part_num), part_name)
            divided_data[f"{region}_part{str(part_num).zfill(2)}"].to_csv(part_path, sep=' ', index=False)
            print(f"Saving {part_path}")
def main():
    create_directories()
    region_files, regions = load_region_files()
    num_aps = get_number_of_aps(region_files[0])
    print(f"Number of Access Points (APs): {num_aps}")
    data = load_data(regions)
    divided_data = shuffle_and_divide_data(data, regions)
    save_divided_data(divided_data, regions)
    print("Data division and saving complete.")
if __name__ == "__main__":
    main()