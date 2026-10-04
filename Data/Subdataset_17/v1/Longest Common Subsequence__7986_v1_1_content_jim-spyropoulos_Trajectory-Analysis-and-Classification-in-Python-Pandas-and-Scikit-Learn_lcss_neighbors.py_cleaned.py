import csv
import os
import re
import numpy as np
import pandas as pd
import time
from auxiliaryfunctions import lcss_trigger, plot_traj_red
df = pd.read_pickle('./final_cleaned.df')
with open('test_set_a2.csv', 'r') as f:
    reader = csv.reader(f)
    data = (list(rec) for rec in csv.reader(f, delimiter=','))
    trajectories_read = []
    for i, row in enumerate(data):
        if i != 0:
            trajectory = []
            for j in range(0, len(row), 3):
                tmp_list = [float(re.sub(r'\[', '', row[j])), float(row[j + 1]), float(re.sub(r'\]', '', row[j + 2]))]
                trajectory.append(tmp_list)
            trajectories_read.append(trajectory)
print("Dataset read successfully.")
os.makedirs("LCSSresults", exist_ok=True)
for k, traj in enumerate(trajectories_read, start=1):
    start_time = time.time()
    matching_points = lcss_trigger(traj, df, 1, 0)
    distancesnp = np.array(matching_points)
    sorted_ind = np.argsort(-distancesnp)
    for m, elem in enumerate(sorted_ind[:5], start=1):
        print(f"Nearest trajectory {df['JourneyPatternId'].iloc[elem]} Matching points: {distancesnp[elem]}.")
        common_points = lcss_trigger(traj, df, 2, elem)
        plot_traj_red(common_points, df['timestamp_longitude_latitude'].iloc[elem],
                      f"./LCSSresults/trajectory{k}_matchingpointsneighb_{m}.png")
    end_time = time.time()
    print(f"Took {(end_time - start_time) / 60:.3f} mins for traj {k} to finish")