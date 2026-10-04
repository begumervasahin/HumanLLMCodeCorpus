import csv
import os
import re
import numpy as np
import pandas as pd
from fastdtw import fastdtw
from auxiliaryfunctions import print_results, haversine_np
df = pd.read_pickle('./final_cleaned.df')
trajectories_read = []
with open('./test_set_a1.csv', 'r') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        if i == 0:
            continue
        trajectory = []
        for j in range(0, len(row), 3):
            tmp_list = [
                float(re.sub(r'[\[]', '', row[j])),
                float(row[j + 1]),
                float(re.sub(r'[]]', '', row[j + 2]))
            ]
            trajectory.append(tmp_list)
        trajectories_read.append(trajectory)
print("Dataset read successfully.")
os.makedirs("DTWresults", exist_ok=True)
for j, traj in enumerate(trajectories_read):
    distances = []
    for elem in df['timestamp_longitude_latitude']:
        distance, _ = fastdtw(elem, traj, dist=haversine_np)
        distances.append(distance)
    sorted_ind = np.argsort(distances)[:5]
    for k, elem in enumerate(sorted_ind):
        output_path = f"./DTWresults/trajectory{j}_neighbor{k}"
        print_results(df, distances, elem, output_path)