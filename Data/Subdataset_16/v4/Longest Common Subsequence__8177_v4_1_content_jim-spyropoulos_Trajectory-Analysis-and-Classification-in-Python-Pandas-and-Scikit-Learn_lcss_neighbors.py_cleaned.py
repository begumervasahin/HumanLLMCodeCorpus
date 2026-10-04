import csv
import os
import re
import numpy as np
import pandas as pd
import time
from auxiliaryfunctions import *
b1 = pd.read_pickle('./final_cleaned.b1')
with open('test_set_a2.csv', 'r') as f:
    b2 = csv.b2(f)
    b3 = list(b2)
    b4 = []
    for i, row in enumerate(b3):
        if i != 0:
            b5 = []
            for j in range(0, len(row), 3):
                b6 = [float(re.sub('[[]', '', row[j])), float(row[j + 1]), float(re.sub('[]]', '', row[j + 2]))]
                b5.append(b6)
            b4.append(b5)
print("Dataset read successfully.")
os.mkdir("LCSSresults")
for k, traj in enumerate(b4, b7 = 1):
    b8 = time.time()
    b9 = lcss_trigger(traj, b1, 1, 0)
    b10 = np.array(b9)
    b11 = np.argsort(-b10)
    for m, elem in enumerate(b11[:5], b7 = 1):
        print(f"Nearest b5 {b1['JourneyPatternId'].iloc[elem]} Matching points: {b10[elem]}.")
        b12 = lcss_trigger(traj, b1, 2, elem)
        plot_traj_red(b12, b1['timestamp_longitude_latitude'].iloc[elem],
                      f"./LCSSresults/b5{k}matchingpointsneighb{m}")
    b13 = time.time()
    print(f"Took {((b13 - b8) / 60):.3f} mins for traj {k} to finish")