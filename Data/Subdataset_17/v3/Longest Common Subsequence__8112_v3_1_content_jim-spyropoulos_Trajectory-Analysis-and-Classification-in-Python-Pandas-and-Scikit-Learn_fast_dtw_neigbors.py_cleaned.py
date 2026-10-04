import csv
import os
import re
import numpy as np
import pandas as pd
from fastdtw import fastdtw
from auxiliaryfunctions import haversine_np, print_results
def load_dataframe(filepath):
    return pd.read_pickle(filepath)
def read_trajectories_from_csv(filepath):
    trajectories = []
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            trajectory = []
            for j in range(0, len(row), 3):
                lat = float(re.sub(r'[\[]', '', row[j]))
                lon = float(row[j + 1])
                timestamp = float(re.sub(r'[\]]', '', row[j + 2]))
                trajectory.append([lat, lon, timestamp])
            trajectories.append(trajectory)
    return trajectories
def create_directory(directory_name):
    os.makedirs(directory_name, exist_ok=True)
def calculate_dtw_distances(dataframe, trajectory, distance_function):
    distances = []
    for elem in dataframe['timestamp_longitude_latitude']:
        distance, _ = fastdtw(elem, trajectory, dist=distance_function)
        distances.append(distance)
    return np.array(distances)
def find_nearest_neighbors(distances, num_neighbors=5):
    return np.argsort(distances)[:num_neighbors]
def store_dtw_results(dataframe, distances, indices, trajectory_index, output_dir):
    for k, idx in enumerate(indices):
        result_path = os.path.join(output_dir, f"trajectory{trajectory_index}_neighbor{k}")
        print_results(dataframe, distances, idx, result_path)
def main():
    df = load_dataframe('./final_cleaned.df')
    print("DataFrame loaded successfully.")
    trajectories = read_trajectories_from_csv('./test_set_a1.csv')
    print("Dataset read successfully.")
    create_directory("DTWresults")
    for j, trajectory in enumerate(trajectories):
        distances = calculate_dtw_distances(df, trajectory, haversine_np)
        nearest_neighbors = find_nearest_neighbors(distances)
        store_dtw_results(df, distances, nearest_neighbors, j, "DTWresults")
    print("DTW analysis completed.")
if __name__ == "__main__":
    main()