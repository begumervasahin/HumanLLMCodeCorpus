import csv
import os
import re
import numpy as np
import pandas as pd
import time
from auxiliaryfunctions import lcss_trigger, plot_traj_red
def read_trajectories_from_csv(file_path):
    with open(file_path, 'r') as file:
        data_reader = csv.reader(file, delimiter=',')
        next(data_reader)
        trajectories = []
        for row in data_reader:
            trajectory = []
            for j in range(0, len(row), 3):
                point = [
                    float(re.sub('[\[\]]', '', row[j])),
                    float(row[j + 1]),
                    float(re.sub('[\[\]]', '', row[j + 2]))
                ]
                trajectory.append(point)
            trajectories.append(trajectory)
    return trajectories
df = pd.read_pickle('./final_cleaned.df')
trajectories_read = read_trajectories_from_csv('test_set_a2.csv')
print("Dataset read successfully.")
os.mkdir("LCSSresults")
for k, traj in enumerate(trajectories_read, start=1):
    start_time = time.time()
    matching_points = lcss_trigger(traj, df, min_length=1, min_points=0)
    distances_np = np.array(matching_points)
    sorted_indices = np.argsort(-distances_np)
    for m, elem in enumerate(sorted_indices[:5], start=1):
        nearest_journey = df['JourneyPatternId'].iloc[elem]
        print(f"Nearest trajectory {nearest_journey} Matching points: {distances_np[elem]}.")
        common_points = lcss_trigger(traj, df, min_length=2, reference_index=elem)
        output_path = f"./LCSSresults/trajectory{k}_matchingpointsneighb_{m}"
        plot_traj_red(common_points, df['timestamp_longitude_latitude'].iloc[elem], output_path)
    end_time = time.time()
    duration_minutes = (end_