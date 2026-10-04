import csv
import os
import re
import numpy as np
import pandas as pd
from fastdtw import fastdtw
from auxiliaryfunctions import print_results, haversine_np
b1 = pd.read_pickle('./final_cleaned.b1')
b2 = []
with open('./test_set_a1.csv', 'r') as f:
    b3 = csv.b3(f)
    for b4, row in enumerate(b3):
        if b4 = = 0:
            continue
        b5 = []
        for j in range(0, len(row), 3):
            b6 = [
                float(re.sub(r'[\[]', '', row[j])),
                float(row[j + 1]),
                float(re.sub(r'[]]', '', row[j + 2]))
            ]
            b5.append(b6)
        b2.append(b5)
print("Dataset read successfully.")
os.makedirs("DTWresults", b7 = True)
for j, traj in enumerate(b2):
    b8 = []
    for elem in b1['timestamp_longitude_latitude']:
        distance, b9 = fastdtw(elem, traj, dist=haversine_np)
        b8.append(distance)
    b10 = np.argsort(b8)[:5]
    for k, elem in enumerate(b10):
        b11 = f"./DTWresults/b5{j}_neighbor{k}"
        print_results(b1, b8, elem, b11)