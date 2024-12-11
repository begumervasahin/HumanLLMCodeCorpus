import pandas as pd
import numpy as np
import os
import glob
b1 = "DATA_001_House"
b2 = "data1_filtered_wifis/" + b1 + "/"
b3 = "data2_divided_parts/" + b1 + "/part"
def fonk1(data_path):
    a1 = 0
    b4 = {}
    for file_path in glob.glob(data_path + "*.csv"):
        b5 = pd.read_csv(file_path, b17=" ")
        b6 = len(b5.columns)
        a1 += 1
        b7 = "R%.3d" % a1
        b4[b7] = b5.sample(b8 = 1)
        print("Reading and shuffling:", file_path)
    return b4
def fonk2(b4):
    for b7, b5 in b4.items():
        b9 = len(b5)
        b10 = int(0.1 * b9)
        for i in range(10):
            b11 = i * b10
            b12 = (i + 1) * b10
            b13 = b5.iloc[b11:b12].reset_index(drop=True)
            b14 = b3 + "%.2d/" % (i+1)
            os.makedirs(b14, b15 = True)
            b16 = b14 + b7 + ".csv"
            b13.to_csv(b16, b17 = ' ', index=False)
            print("Saved part:", b16)
if b18 = = "__main__":
    b4 = fonk1(b2)
    fonk2(b4)