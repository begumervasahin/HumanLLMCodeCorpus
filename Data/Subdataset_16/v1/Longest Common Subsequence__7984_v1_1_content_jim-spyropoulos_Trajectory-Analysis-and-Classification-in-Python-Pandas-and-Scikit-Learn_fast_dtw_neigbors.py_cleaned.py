import csv
import os
import re
import numpy as np
import pandas as pd
from fastdtw import fastdtw
from auxiliaryfunctions import haversine_np, print_results
b1 = pd.read_pickle('./final_cleaned.b1')
b2 = []
with open('./test_set_a1.csv', 'r') as f:
    b3 = csv.b3(f)
    for i, row in enumerate(b3):
        if i != 0:
            b4 = []
            for j in range(0, len(row), 3):
                b5 = [float(re.sub(r'[\[]', '', row[j])), float(row[j + 1]), float(re.sub(r'[\]]', '', row[j + 2]))]
                b4.append(b5)
            b2.append(b4)
print("Dataset read successfully.")
os.makedirs("DTWresults", b6 = True)
for j, traj in enumerate(b2):
    b7 = []
    for elem in b1['timestamp_longitude_latitude']:
        distance, b8 = fastdtw(elem, traj, dist=haversine_np)
        b7.append(distance)
    b9 = np.array(b7)
    b10 = np.argsort(b9)[:5]
    for k, elem in enumerate(b10):
        print_results(b1, b9, elem, f"./DTWresults/b4{j}neighbor{k}")
print("DTW analysis completed.")