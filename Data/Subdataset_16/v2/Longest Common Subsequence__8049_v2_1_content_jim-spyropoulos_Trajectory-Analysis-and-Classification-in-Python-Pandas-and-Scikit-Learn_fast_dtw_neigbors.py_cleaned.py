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
    for b4, row in enumerate(b3):
        if b4 = = 0:
            continue
        b5 = []
        for j in range(0, len(row), 3):
            b6 = float(re.sub(r'[\[]', '', row[j]))
            b7 = float(row[j + 1])
            b8 = float(re.sub(r'[\]]', '', row[j + 2]))
            b5.append([b6, b7, b8])
        b2.append(b5)
print("Dataset read successfully.")
os.makedirs("DTWresults", b9 = True)
for j, traj in enumerate(b2):
    b10 = []
    for elem in b1['timestamp_longitude_latitude']:
        distance, b11 = fastdtw(elem, traj, dist=haversine_np)
        b10.append(distance)
    b12 = np.array(b10)
    b13 = np.argsort(b12)[:5]
    for k, elem in enumerate(b13):
        b14 = f"./DTWresults/b5{j}neighbor{k}"
        print_results(b1, b12, elem, b14)
print("DTW analysis completed.")