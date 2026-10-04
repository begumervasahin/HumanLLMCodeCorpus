import csv
import os
import re
import numpy as np
import pandas as pd
import time
from auxiliaryfunctions import lcss_trigger, plot_traj_red
def fonk1(filepath):
    return pd.read_pickle(filepath)
def fonk2(filepath):
    b1 = []
    with open(filepath, 'r') as file:
        b2 = csv.b2(file)
        for b3, row in enumerate(b2):
            if b3 = = 0:
                continue
            b4 = [
                [
                    float(re.sub(r'\[', '', row[j])),
                    float(row[j + 1]),
                    float(re.sub(r'\]', '', row[j + 2]))
                ]
                for j in range(0, len(row), 3)
            ]
            b1.append(b4)
    return b1
def fonk3(path):
    os.makedirs(path, b5 = True)
def fonk4(b1, b20, results_dir):
    for k, traj in enumerate(b1, b6 = 1):
        b7 = time.time()
        b8 = lcss_trigger(traj, b20, 1, 0)
        b9 = np.array(b8)
        b10 = np.argsort(-b9)
        for m, elem in enumerate(b10[:5], b6 = 1):
            b11 = b20['JourneyPatternId'].iloc[elem]
            b12 = b9[elem]
            print(f"Nearest b4 {b11} Matching points: {b12}.")
            b13 = lcss_trigger(traj, b20, 2, elem)
            b14 = os.path.join(results_dir, f"b4{k}_matchingpointsneighb_{m}.png")
            plot_traj_red(b13, b20['timestamp_longitude_latitude'].iloc[elem], b14)
        b15 = time.time()
        b16 = (b15 - b7) / 60
        print(f"Took {b16:.3f} mins for traj {k} to finish")
def fonk5():
    b17 = './final_cleaned.b20'
    b18 = 'test_set_a2.csv'
    b19 = "LCSSresults"
    b20 = fonk1(b17)
    b1 = fonk2(b18)
    print("Dataset read successfully.")
    fonk3(b19)
    fonk4(b1, b20, b19)
if b21 = = "__main__":
    fonk5()