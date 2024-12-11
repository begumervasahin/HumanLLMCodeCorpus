import pandas as pd
import numpy as np
import os
import glob
b1 = "DATA_001_House"
b2 = f"data1_filtered_wifis/{b1}/"
b3 = f"data2_divided_parts/{b1}/part"
def fonk1(data_path):
    b4 = {}
    for idx, file_path in enumerate(glob.glob(f"{data_path}*.csv")):
        b5 = pd.read_csv(file_path, b15=" ")
        b5 = b5.sample(frac=1).reset_index(drop=True)
        b6 = f"R{idx + 1:03d}"
        b4[b6] = b5
        print("Reading and shuffling:", file_path)
    return b4
def fonk2(b4):
    a1 = 10
    for b6, b5 in b4.items():
        b7 = len(b5)
        b8 = b7
        for i in range(a1):
            b9 = i * b8
            b10 = (i + 1) * b8
            b11 = b5.iloc[b9:b10].reset_index(drop=True)
            b12 = f"{b3}{i + 1:02d}/"
            os.makedirs(b12, b13 = True)
            b14 = f"{b12}{b6}.csv"
            b11.to_csv(b14, b15 = ' ', index=False)
            print("Saved part:", b14)
if b16 = = "__main__":
    b4 = fonk1(b2)
    fonk2(b4)