import csv
import os
import re
import numpy as np
import pandas as pd
from fastdtw import fastdtw
from auxiliaryfunctions import haversine_np, print_results
def fonk1(filepath):
    return pd.read_pickle(filepath)
def fonk2(filepath):
    b1 = []
    with open(filepath, 'r') as f:
        b2 = csv.b2(f)
        next(b2)
        for row in b2:
            b3 = []
            for j in range(0, len(row), 3):
                b4 = float(re.sub(r'[\[]', '', row[j]))
                b5 = float(row[j + 1])
                b6 = float(re.sub(r'[\]]', '', row[j + 2]))
                b3.append([b4, b5, b6])
            b1.append(b3)
    return b1
def fonk3(directory_name):
    os.makedirs(directory_name, b7 = True)
def fonk4(dataframe, b3, distance_function):
    b8 = []
    for elem in dataframe['timestamp_longitude_latitude']:
        distance, b9 = fastdtw(elem, b3, dist=distance_function)
        b8.append(distance)
    return np.array(b8)
def fonk5(b8, b10 = 5):
    return np.argsort(b8)[:b10]
def fonk6(dataframe, b8, indices, trajectory_index, output_dir):
    for k, idx in enumerate(indices):
        b11 = os.path.join(output_dir, f"b3{trajectory_index}_neighbor{k}")
        print_results(dataframe, b8, idx, b11)
def fonk7():
    b12 = fonk1('./final_cleaned.b12')
    print("DataFrame loaded successfully.")
    b1 = fonk2('./test_set_a1.csv')
    print("Dataset read successfully.")
    fonk3("DTWresults")
    for j, b3 in enumerate(b1):
        b8 = fonk4(b12, b3, haversine_np)
        b13 = fonk5(b8)
        fonk6(b12, b8, b13, j, "DTWresults")
    print("DTW analysis completed.")
if b14 = = "__main__":
    fonk7()