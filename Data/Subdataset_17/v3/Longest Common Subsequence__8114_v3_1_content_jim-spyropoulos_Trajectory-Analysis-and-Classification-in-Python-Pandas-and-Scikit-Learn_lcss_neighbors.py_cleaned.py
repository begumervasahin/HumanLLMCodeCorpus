import csv
import os
import re
import numpy as np
import pandas as pd
import time
from auxiliaryfunctions import lcss_trigger, plot_traj_red
def load_dataframe(filepath):
    return pd.read_pickle(filepath)
def read_trajectories_from_csv(filepath):
    trajectories = []
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i == 0:
                continue
            trajectory = [
                [
                    float(re.sub(r'\[', '', row[j])),
                    float(row[j + 1]),
                    float(re.sub(r'\]', '', row[j + 2]))
                ]
                for j in range(0, len(row), 3)
            ]
            trajectories.append(trajectory)
    return trajectories
def create_directory(path):
    os.makedirs(path, exist_ok=True)
def process_trajectories(trajectories, df, results_dir):
    for k, traj in enumerate(trajectories, start=1):
        start_time = time.time()
        matching_points = lcss_trigger(traj, df, 1, 0)
        distancesnp = np.array(matching_points)
        sorted_ind = np.argsort(-distancesnp)
        for m, elem in enumerate(sorted_ind[:5], start=1):
            journey_pattern_id = df['JourneyPatternId'].iloc[elem]
            matching_point_count = distancesnp[elem]
            print(f"Nearest trajectory {journey_pattern_id} Matching points: {matching_point_count}.")
            common_points = lcss_trigger(traj, df, 2, elem)
            plot_filepath = os.path.join(results_dir, f"trajectory{k}_matchingpointsneighb_{m}.png")
            plot_traj_red(common_points, df['timestamp_longitude_latitude'].iloc[elem], plot_filepath)
        end_time = time.time()
        elapsed_time = (end_time - start_time) / 60
        print(f"Took {elapsed_time:.3f} mins for traj {k} to finish")
def main():
    dataframe_filepath = './final_cleaned.df'
    test_set_filepath = 'test_set_a2.csv'
    results_directory = "LCSSresults"
    df = load_dataframe(dataframe_filepath)
    trajectories = read_trajectories_from_csv(test_set_filepath)
    print("Dataset read successfully.")
    create_directory(results_directory)
    process_trajectories(trajectories, df, results_directory)
if __name__ == "__main__":
    main()