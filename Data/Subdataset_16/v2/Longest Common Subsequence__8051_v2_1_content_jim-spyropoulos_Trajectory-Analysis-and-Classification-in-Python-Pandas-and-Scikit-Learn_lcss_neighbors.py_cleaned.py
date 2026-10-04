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
    b3 = []
    for b4, row in enumerate(b2):
        if b4 = = 0:
            continue
        b5 = []
        for j in range(0, len(row), 3):
            b6 = [
                float(re.sub(r'\[', '', row[j])),
                float(row[j + 1]),
                float(re.sub(r'\]', '', row[j + 2]))
            ]
            b5.append(b6)
        b3.append(b5)
print("Dataset read successfully.")
os.makedirs("LCSSresults", b7 = True)
for k, traj in enumerate(b3, b8 = 1):
    b9 = time.time()
    b10 = lcss_trigger(traj, b1, 1, 0)
    b11 = np.array(b10)
    b12 = np.argsort(-b11)
    for m, elem in enumerate(b12[:5], b8 = 1):
        print(f"Nearest b5 {b1['JourneyPatternId'].iloc[elem]} Matching points: {b11[elem]}.")
        b13 = lcss_trigger(traj, b1, 2, elem)
        plot_traj_red(b13, b1['timestamp_longitude_latitude'].iloc[elem],
                      f"./LCSSresults/b5{k}_matchingpointsneighb_{m}.png")
    b14 = time.time()
    print(f"Took {(b14 - b9) / 60:.3f} mins for traj {k} to finish")