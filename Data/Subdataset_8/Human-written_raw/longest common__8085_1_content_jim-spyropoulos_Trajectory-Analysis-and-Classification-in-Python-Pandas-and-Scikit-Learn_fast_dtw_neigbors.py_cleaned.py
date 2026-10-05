import csv
import os
import re
import numpy as np
import pandas as pd
from fastdtw import fastdtw
from auxiliaryfunctions import *
df = pd.read_pickle('./final_cleaned.df')
with open('./test_set_a1.csv', 'r') as f:
    reader = csv.reader(f)
    data = (list(rec) for rec in csv.reader(f, delimiter=','))
    i = 0
    count = 0
    trajectories_read = []
    for row in data:
        if (i != 0):
            tmp_list = []
            trajectory = []
            j = 0
            while (j != len(row)):
                tmp_list = [float(re.sub('[[]', '', row[j])), float(row[j + 1]), float(re.sub('[]]', '', row[j + 2]))]
                j = j + 3
                trajectory.append(tmp_list)
                tmp_list = []
            trajectories_read.append(trajectory)
        i = i + 1
print("Dataset read successfully.")
os.mkdir("DTWresults")
j = 0
for traj in trajectories_read:
    distances = []
    for elem in df['timestamp_longitude_latitude']:
        distance, path = fastdtw(elem, traj, dist=haversine_np)
        distances.append(distance)
    distancesnp = np.array(distances)
    sorted_ind = np.argsort(distancesnp)[:5]
    k = 0
    for elem in sorted_ind:
        print_results(df, distancesnp, elem, "./DTWresults/trajectory" + str(j) + "neighbor" + str(k))
        k = k + 1
    j = j + 1