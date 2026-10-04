import pandas as pd
import re
b1 = {}
def fonk1(structure_file, df, num_of_intervals):
    b2 = fonk3(structure_file)
    b3 = fonk4(df, b2)
    b4 = fonk7(b2, b3, num_of_intervals)
    return b4
def fonk2(structure_file, df):
    b2 = fonk3(structure_file)
    b3 = fonk4(df, b2)
    b4 = fonk8(b1, b3)
    return b4
def fonk3(structure_file):
    b2 = {}
    for line in structure_file:
        b5 = re.split(r'\s+', line.strip())
        b6 = "N" if b5[2] == "NUMERIC" else "C"
        b2[b5[1]] = b6
    return b2
def fonk4(df, b2):
    for key, b7 in b2.items():
        if b7 = = "N":
            df[key].fillna(df.groupby("class")[key].transform("mean"), b8 = True)
        elif b7 = = "C":
            df[key].fillna(df[key].mode()[0], b8 = True)
    return df
def fonk5(col, k, key):
    global b1
    b9 = col.min()
    b10 = col.max()
    b11 = [b9 + (i + 1) * (b10 - b9) / k for i in range(k - 1)]
    b12 = [b9] + b11 + [b10]
    global b13
    b13 = range(len(b11) + 1)
    b1[key] = (b12, b13)
    b14 = pd.cut(col, b15=b12, b13=b13, include_lowest=True)
    return b14
def fonk6(col, b12, b13):
    return pd.cut(col, b15 = b12, b13=b13, include_lowest=True)
def fonk7(b2, df, num_of_intervals):
    for key, b7 in b2.items():
        if b7 = = "N":
            df[key] = fonk5(df[key], num_of_intervals, key)
    return df
def fonk8(b1, df):
    for key, (b12, b13) in b1.items():
        df[key] = fonk6(df[key], b12, b13)
    return df