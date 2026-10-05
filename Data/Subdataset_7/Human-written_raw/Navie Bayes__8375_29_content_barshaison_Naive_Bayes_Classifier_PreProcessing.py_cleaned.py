import pandas as pd
import re
b1 = {}
def fonk1(structure_file,df,numOfIntervals):
    b2 = fonk3(structure_file)
    b3 = fonk5(df, b2)
    b4 = fonk8(b2, b3, numOfIntervals)
    return b4
def fonk2(structure_file,df):
    b2 = fonk3(structure_file)
    b3 = fonk5(df, b2)
    b4 = fonk9(b1, b3)
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
def fonk4(structure_file):
    b7 = {}
    for line in structure_file:
        b6 = re.split('\s', line)
        if b6[2] == "NUMERIC":
            b8 = b17
        else:
            b9 = b6[2].replace('{', '')
            b10 = b9.replace('}', '')
            b8 = b10.split(',')
        b7[b6[1]] = b8
    return b7
def fonk5(df, b2):
    for key in b2:
        if b2[key] == "N":
            df[key].fillna(df.groupby("class")[key].transform("mean"), b11 = True)
    for key in b2:
        if b2[key] == "C":
            df[key] = df[key].fillna(df[key].mode()[0])
    return df
def fonk6(col, k,key):
    global b1
    b12 = col.min()
    b13 = col.max()
    b14 = []
    b15 = (b13 - b12)/k
    for i in range(0, k-1):
        if (b12 + (i+1)*b15) != b12 and (b12 + (i+1)*b15) != b13:
            b14.append(b12 + (i+1)*b15)
    b16 = [b12] + b14 + [b13]
    global b17
    b17 = range(len(b14) + 1)
    b18 = [b16, b17]
    b1[key] = b18
    b19 = pd.cut(col, bins=b16, b17=b17, include_lowest=True)
    return b19
def fonk7(col,b16,b17):
    b19 = pd.cut(col, bins=b16, b17=b17, include_lowest=True)
    return b19
def fonk8(b2,df,numOfIntervals):
    for key in b2:
        if b2[key] == "N":
            df[key] = fonk6(df[key], numOfIntervals,key)
    return df
def fonk9(b1,df):
    for key in b1:
        df[key] = fonk7(df[key],b1[key][0],b1[key][1])
    return df