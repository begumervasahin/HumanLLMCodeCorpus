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
    b3 = list(b2)[1:]
    b4 = []
    for row in b3:
        b5 = []
        for j in range(0, len(row), 3):
            b6 = [
                float(re.sub('[\[\]]', '', row[j])),
                float(row[j + 1]),
                float(re.sub('[\[\]]', '', row[j + 2]))
            ]
            b5.append(b6)
        b4.append(b5)
os.mkdir("LCSSresults")
for k, traj in enumerate(b4, b7 = 1):
    b8 = time.time()
    b9 = lcss_trigger(traj, b1, min_length=1, min_points=0)
    b10 = np.array(b9)
    b11 = np.argsort(-b10)
    for m, index in enumerate(b11[:5], b7 = 1):
        b12 = b1['JourneyPatternId'].iloc[index]
        print(f"Nearest b5 {b12} Matching points: {b10[index]}.")
        b13 = lcss_trigger(traj, b1, min_length=2, reference_index=index)
        plot_traj_red(b13, b1['timestamp_longitude_latitude'].iloc[index],
                      f"./LCSSresults/b5{k}_matchingpointsneighb_{m}")
    b14 = time.time()
    b15 = (b14 - b8) / 60
    print(f"Took {b15:.3f} mins for traj {k} to finish")