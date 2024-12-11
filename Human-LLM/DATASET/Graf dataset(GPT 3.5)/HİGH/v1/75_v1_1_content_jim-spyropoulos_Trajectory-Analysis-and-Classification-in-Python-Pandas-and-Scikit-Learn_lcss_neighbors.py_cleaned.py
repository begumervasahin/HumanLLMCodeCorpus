import csv
import os
import re
import numpy as np
import pandas as pd
import time
from auxiliaryfunctions import lcss_trigger, plot_traj_red
b1 = pd.read_pickle('./final_cleaned.b1')
with open('test_set_a2.csv', 'r') as f:
    b2 = csv.b2(f)
    b3 = [list(rec) for rec in csv.b2(f, delimiter=',')]
    b4 = []
    for i, row in enumerate(b3):
        if i != 0:
            b5 = []
            b6 = []
            a1 = 0
            while a1 != len(row):
                b5 = [float(re.sub('[\[\]]', '', row[a1])), float(row[a1 + 1]), float(re.sub('[\[\]]', '', row[a1 + 2]))]
                a1 += 3
                b6.append(b5)
                b5 = []
            b4.append(b6)
os.mkdir("LCSSresults")
for k, traj in enumerate(b4, b7 = 1):
    b8 = time.time()
    b9 = lcss_trigger(traj, b1, 1, 0)
    b10 = np.array(b9)
    b11 = np.argsort(-b10)
    for m, elem in enumerate(b11[:5], b7 = 1):
        print(f"Nearest b6 {b1['JourneyPatternId'].iloc[elem]} Matching points: {b10[elem]}.")
        b12 = lcss_trigger(traj, b1, 2, elem)
        plot_traj_red(b12, b1['timestamp_longitude_latitude'].iloc[elem],
                      f"./LCSSresults/b6{k}_matchingpointsneighb_{m}")
    b13 = time.time()
    print(f"Took {((b13 - b8) / 60):.3f} mins for traj {k} to finish")