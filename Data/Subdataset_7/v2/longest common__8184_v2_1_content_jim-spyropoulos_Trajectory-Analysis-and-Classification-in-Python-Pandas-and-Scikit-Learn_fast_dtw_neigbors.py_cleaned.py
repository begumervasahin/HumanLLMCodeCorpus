import csv
import os
import re
import numpy as np
import pandas as pd
from fastdtw import fastdtw
from auxiliaryfunctions import haversine_np, print_results
b1 = pd.read_pickle('./final_cleaned.b1')
with open('./test_set_a1.csv', 'r') as f:
    b2 = csv.b2(f)
    b3 = list(b2)
    b4 = []
    for row in b3[1:]:
        b5 = []
        for j in range(0, len(row), 3):
            b6 = float(re.sub('[[]', '', row[j]))
            b7 = float(row[j + 1])
            b8 = float(re.sub('[]]', '', row[j + 2]))
            b5.append([b6, b7, b8])
        b4.append(b5)
print("Dataset read successfully.")
os.mkdir("DTWresults")
for j, traj in enumerate(b4):
    b9 = []
    for elem in b1['timestamp_longitude_latitude']:
        distance, b10 = fastdtw(elem, traj, dist=haversine_np)
        b9.append(distance)
    b11 = np.array(b9)
    b12 = np.argsort(b11)[:5]
    for k, elem in enumerate(b12):
        print_results(b1, b11, elem, f"./DTWresults/b5{j}neighbor{k}")