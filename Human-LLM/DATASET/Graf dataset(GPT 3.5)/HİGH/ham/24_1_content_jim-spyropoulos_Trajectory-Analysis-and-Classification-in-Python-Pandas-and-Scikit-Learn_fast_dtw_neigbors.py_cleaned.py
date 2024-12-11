import csv
import os
import re
import numpy as np
import pandas as pd
from fastdtw import fastdtw
from auxiliaryfunctions import *
b1 = pd.read_pickle('./final_cleaned.b1')
with open('./test_set_a1.csv', 'r') as f:
    b2 = csv.b2(f)
    b3 = (list(rec) for rec in csv.b2(f, delimiter=','))
    a1 = 0
    a2 = 0
    b4 = []
    for row in b3:
        if (a1 != 0):
            b5 = []
            b6 = []
            a3 = 0
            while (a3 != len(row)):
                b5 = [float(re.sub('[[]', '', row[a3])), float(row[a3 + 1]), float(re.sub('[]]', '', row[a3 + 2]))]
                a3 = a3 + 3
                b6.append(b5)
                b5 = []
            b4.append(b6)
        a1 = a1 + 1
print("Dataset read successfully.")
os.mkdir("DTWresults")
a3 = 0
for traj in b4:
    b7 = []
    for elem in b1['timestamp_longitude_latitude']:
        distance, b8 = fastdtw(elem, traj, dist=haversine_np)
        b7.append(distance)
    b9 = np.array(b7)
    b10 = np.argsort(b9)[:5]
    a4 = 0
    for elem in b10:
        print_results(b1, b9, elem, "./DTWresults/b6" + str(a3) + "neighbor" + str(a4))
        a4 = a4 + 1
    a3 = a3 + 1