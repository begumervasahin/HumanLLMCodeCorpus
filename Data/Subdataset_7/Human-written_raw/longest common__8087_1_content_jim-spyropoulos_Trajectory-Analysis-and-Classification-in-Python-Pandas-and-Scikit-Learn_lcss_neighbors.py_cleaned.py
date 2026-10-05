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
os.mkdir("LCSSresults")
a4 = 0
for traj in b4:
    b7 = time.time()
    a4 = a4 + 1
    b8 = lcss_trigger(traj, b1, 1, 0)
    b9 = np.array(b8)
    b10 = np.argsort(-b9)
    a5 = 1
    for elem in b10[:5]:
        print("Nearest b6 " + str(b1['JourneyPatternId'].iloc[elem]) + " Matching points : %d." % b9[
            elem])
        b11 = lcss_trigger(traj, b1, 2, elem)
        plot_traj_red(b11, b1['timestamp_longitude_latitude'].iloc[elem],
                      "./LCSSresults/b6" + str(a4) + "matchingpointsneighb: " + str(a5))
        a5 = a5 + 1
    b12 = time.time()
    print("Took %.3f mins for traj %d to finish" % ((float)((b12 - b7) / 60), a4))