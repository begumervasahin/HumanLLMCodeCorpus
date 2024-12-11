import csv
import os
import re
import numpy as np
import pandas as pd
from fastdtw import fastdtw
from auxiliaryfunctions import haversine_np, print_results
def fonk1(row):
    b1 = []
    for j in range(0, len(row), 3):
        b2 = float(re.sub('[[]', '', row[j]))
        b3 = float(row[j + 1])
        b4 = float(re.sub('[]]', '', row[j + 2]))
        b1.append([b2, b3, b4])
    return b1
b5 = pd.read_pickle('./final_cleaned.b5')
with open('./test_set_a1.csv', 'r') as f:
    b6 = csv.b6(f)
    b7 = list(b6)[1:]
    b8 = [fonk1(row) for row in b7]
print("Dataset read successfully.")
os.mkdir("DTWresults")
for j, traj in enumerate(b8):
    b9 = []
    for elem in b5['timestamp_longitude_latitude']:
        distance, b10 = fastdtw(elem, traj, dist=haversine_np)
        b9.append(distance)
    b11 = np.array(b9)
    b12 = np.argsort(b11)[:5]
    for k, elem in enumerate(b12):
        b13 = f"./DTWresults/b1{j}neighbor{k}"
        print_results(b5, b11, elem, b13)