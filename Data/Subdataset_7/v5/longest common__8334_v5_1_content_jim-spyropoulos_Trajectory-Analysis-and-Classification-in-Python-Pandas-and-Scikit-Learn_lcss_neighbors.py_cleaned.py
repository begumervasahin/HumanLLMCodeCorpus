import csv
import os
import re
import numpy as np
import pandas as pd
import time
from auxiliaryfunctions import lcss_trigger, plot_traj_red
def fonk1(file_path):
    with open(file_path, 'r') as file:
        b1 = csv.reader(file, delimiter=',')
        next(b1)
        b2 = []
        for row in b1:
            b3 = []
            for j in range(0, len(row), 3):
                b4 = [
                    float(re.sub('[\[\]]', '', row[j])),
                    float(row[j + 1]),
                    float(re.sub('[\[\]]', '', row[j + 2]))
                ]
                b3.append(b4)
            b2.append(b3)
    return b2
b5 = pd.read_pickle('./final_cleaned.b5')
b6 = fonk1('test_set_a2.csv')
print("Dataset read successfully.")
os.mkdir("LCSSresults")
for k, traj in enumerate(b6, b7 = 1):
    b8 = time.time()
    b9 = lcss_trigger(traj, b5, min_length=1, min_points=0)
    b10 = np.array(b9)
    b11 = np.argsort(-b10)
    for m, elem in enumerate(b11[:5], b7 = 1):
        b12 = b5['JourneyPatternId'].iloc[elem]
        print(f"Nearest b3 {b12} Matching points: {b10[elem]}.")
        b13 = lcss_trigger(traj, b5, min_length=2, reference_index=elem)
        b14 = f"./LCSSresults/b3{k}_matchingpointsneighb_{m}"
        plot_traj_red(b13, b5['timestamp_longitude_latitude'].iloc[elem], b14)
    b15 = time.time()
    b16 = (end_