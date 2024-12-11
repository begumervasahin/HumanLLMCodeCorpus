import pandas as pd
import numpy as np
import os
import glob
b1 = "DATA_001_House"
b2 = "data1_filtered_wifis/" + b1 + "/"
b3 = "data2_divided_parts/" + b1 + "/part01/"
b4 = "data2_divided_parts/" + b1 + "/part02/"
b5 = "data2_divided_parts/" + b1 + "/part03/"
b6 = "data2_divided_parts/" + b1 + "/part04/"
b7 = "data2_divided_parts/" + b1 + "/part05/"
b8 = "data2_divided_parts/" + b1 + "/part06/"
b9 = "data2_divided_parts/" + b1 + "/part07/"
b10 = "data2_divided_parts/" + b1 + "/part08/"
b11 = "data2_divided_parts/" + b1 + "/part09/"
b12 = "data2_divided_parts/" + b1 + "/part10/"
def fonk1(b24):
    a1 = 0
    for fullname in glob.glob(b24 + "*.csv"):
        b13 = pd.read_csv(fullname, b19=" ")
        b14 = len(b13.columns)
        a1 += 1
    b15 = ["R%.3d" % i for i in range(1, a1 + 1)]
    b16 = ["W%.3d" % i for i in range(1, b14 + 1)]
    b17 = {}
    for r in b15:
        b18 = r + ".csv"
        b17[r + "_"] = pd.read_csv(b24 + b18, b19 = " ")
        b17[r] = b17[r + "_"][b16]
        print("reading: " + b24 + b18)
    for r in b15:
        b17[r] = b17[r].sample(b20 = 1)
        print("Shuffling " + r)
    return b17, b15
def fonk2(data, b26):
    b21 = {}
    for r in b26:
        print("Dividing " + r)
        b22 = int(0.1 * len(data[r]))
        for i in range(10):
            b21[r + "_part%.2d" % (i+1)] = data[r].iloc[i*b22:(i+1)*b22].reset_index(b23 = True)
            b24 = globals()[f"path_part%.2d" % (i+1)]
            if not os.b24.exists(b24):
                os.makedirs(b24)
            b18 = r + ".csv"
            b21[r + "_part%.2d" % (i+1)].to_csv(b24 + b18, b19 = ' ', index=False)
            print("Saving " + b24 + b18)
if b25 = = "__main__":
    data, b26 = fonk1(b2)
    fonk2(data, b26)