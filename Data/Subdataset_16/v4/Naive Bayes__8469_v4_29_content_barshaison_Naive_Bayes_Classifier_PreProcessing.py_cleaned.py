import pandas as pd
import re
b1 = {}
def fonk1(structure_file, df, num_of_intervals):
    b2 = fonk3(structure_file)
    b3 = fonk5(df, b2)
    b4 = fonk8(b2, b3, num_of_intervals)
    return b4
def fonk2(structure_file, df):
    b2 = fonk3(structure_file)
    b3 = fonk5(df, b2)
    b4 = fonk9(b1, b3)
    return b4
def fonk3(structure_file):
    b2 = {}
    for line in structure_file:
        b5 = re.split(r'\s+', line)
        b6 = "N" if b5[2] == "NUMERIC" else "C"
        b2[b5[1]] = b6
    return b2
def fonk4(structure_file):
    b7 = {}
    for line in structure_file:
        b5 = re.split(r'\s+', line)
        if b5[2] == "NUMERIC":
            b8 = b16
        else:
            b9 = b5[2].strip('{}').split(',')
            b8 = b9
        b7[b5[1]] = b8
    return b7
def fonk5(df, b2):
    for key, b10 in b2.items():
        if b10 = = "N":
            df[key].fillna(df.groupby("class")[key].transform("mean"), b11 = True)
        elif b10 = = "C":
            df[key].fillna(df[key].mode()[0], b11 = True)
    return df
def fonk6(col, k, key):
    global b1
    b12 = col.min()
    b13 = col.max()
    b14 = [b12 + (i + 1) * (b13 - b12) / k for i in range(k - 1) if b12 < (b12 + (i + 1) * (b13 - b12) / k) < b13]
    b15 = [b12] + b14 + [b13]
    global b16
    b16 = range(len(b14) + 1)
    b1[key] = [b15, b16]
    b17 = pd.cut(col, b18=b15, b16=b16, include_lowest=True)
    return b17
def fonk7(col, b15, b16):
    return pd.cut(col, b18 = b15, b16=b16, include_lowest=True)
def fonk8(b2, df, num_of_intervals):
    for key, b10 in b2.items():
        if b10 = = "N":
            df[key] = fonk6(df[key], num_of_intervals, key)
    return df
def fonk9(b1, df):
    for key, (b15, b16) in b1.items():
        df[key] = fonk7(df[key], b15, b16)
    return df