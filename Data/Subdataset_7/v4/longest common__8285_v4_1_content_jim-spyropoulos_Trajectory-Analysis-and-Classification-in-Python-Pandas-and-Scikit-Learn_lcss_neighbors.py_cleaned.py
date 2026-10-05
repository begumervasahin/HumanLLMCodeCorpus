import csv
import os
import re
import numpy as np
import pandas as pd
import time
from auxiliaryfunctions import lcss_trigger, plot_traj_red
b1 = pd.read_pickle('./final_cleaned.b1')
with open('test_set_a2.csv', 'r') as f:
    b2 = csv.reader(f, delimiter=',')
    next(b2)
    b3 = []
    for row in b2:
        b4 = []
        a1 = 0
        while a1 < len(row):
            b5 = [
                float(re.sub('[\[\]]', '', row[a1])),
                float(row[a1 + 1]),
                float(re.sub('[\[\]]', '', row[a1 + 2]))
            ]
            b4.append(b5)
            a1 += 3
        b3.append(b4)
print("Dataset read successfully.")
os.mkdir("LCSSresults")
for k, traj in enumerate(b3, b6 = 1):
    b7 = time.time()
    b8 = lcss_trigger(traj, b1, min_length=1, min_points=0)
    b9 = np.array(b8)
    b10 = np.argsort(-b9)
    for m, elem in enumerate(b10[:5], b6 = 1):
        b11 = b1['JourneyPatternId'].iloc[elem]
        print(f"Nearest trajectory {b11} Matching points: {b9[elem]}.")
        b12 = lcss_trigger(traj, b1, min_length=2, reference_index=elem)
        b13 = f"./LCSSresults/trajectory{k}_matchingpointsneighb_{m}"
        plot_traj_red(b12, b1['timestamp_longitude_latitude'].iloc[elem], b13)
    b14 = time.time()
    b15 = (b14 - b7) / 60
    print(f"Took {b15:.3f} mins for traj {k} to finish")