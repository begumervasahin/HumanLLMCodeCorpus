import csv
import os
import re
import numpy as np
import pandas as pd
from fastdtw import fastdtw
from auxiliaryfunctions import haversine_np, print_results
def extract_trajectory(row):
    trajectory = []
    for j in range(0, len(row), 3):
        longitude = float(re.sub('[[]', '', row[j]))
        latitude = float(row[j + 1])
        timestamp = float(re.sub('[]]', '', row[j + 2]))
        trajectory.append([longitude, latitude, timestamp])
    return trajectory
df = pd.read_pickle('./final_cleaned.df')
with open('./test_set_a1.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)[1:]
    trajectories_read = [extract_trajectory(row) for row in data]
print("Dataset read successfully.")
os.mkdir("DTWresults")
for j, traj in enumerate(trajectories_read):
    distances = []
    for elem in df['timestamp_longitude_latitude']:
        distance, _ = fastdtw(elem, traj, dist=haversine_np)
        distances.append(distance)
    distancesnp = np.array(distances)
    sorted_ind = np.argsort(distancesnp)[:5]
    for k, elem in enumerate(sorted_ind):
        output_path = f"./DTWresults/trajectory{j}neighbor{k}"
        print_results(df, distancesnp, elem, output_path)