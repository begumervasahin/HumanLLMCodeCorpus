import pandas as pd
import re
b1 = {}
def fonk1(structure_file, df, numOfIntervals):
    b2 = fonk3(structure_file)
    b3 = fonk4(df, b2)
    b4 = fonk7(b2, b3, numOfIntervals)
    return b4
def fonk2(structure_file, df):
    b2 = fonk3(structure_file)
    b3 = fonk4(df, b2)
    b4 = fonk8(b1, b3)
    return b4
def fonk3(structure_file):
    b2 = {}
    b5 = ""
    for line in structure_file:
        b6 = re.split('\s', line)
        if b6[2] == "NUMERIC":
            b5 = "N"
        else:
            b5 = "C"
        b2[b6[1]] = b5
    return b2
def fonk4(df, b2):
    for key in b2:
        if b2[key] == "N":
            df[key].fillna(df.groupby("class")[key].transform("mean"), b7 = True)
    for key in b2:
        if b2[key] == "C":
            df[key] = df[key].fillna(df[key].mode()[0])
    return df
def fonk5(col, k, key):
    b8 = col.min()
    b9 = col.max()
    b10 = []
    b11 = (b9 - b8) / k
    for i in range(0, k-1):
        if (b8 + (i+1) * b11) != b8 and (b8 + (i+1) * b11) != b9:
            b10.append(b8 + (i+1) * b11)
    b12 = [b8] + b10 + [b9]
    b13 = range(len(b10) + 1)
    b14 = [b12, b13]
    b1[key] = b14
    b15 = pd.cut(col, bins=b12, b13=b13, include_lowest=True)
    return b15
def fonk6(col, b12, b13):
    b15 = pd.cut(col, bins=b12, b13=b13, include_lowest=True)
    return b15
def fonk7(b2, df, numOfIntervals):
    for key in b2:
        if b2[key] == "N":
            df[key] = fonk5(df[key], numOfIntervals, key)
    return df
def fonk8(b1, df):
    for key in b1:
        df[key] = fonk6(df[key], b1[key][0], b1[key][1])
    return df