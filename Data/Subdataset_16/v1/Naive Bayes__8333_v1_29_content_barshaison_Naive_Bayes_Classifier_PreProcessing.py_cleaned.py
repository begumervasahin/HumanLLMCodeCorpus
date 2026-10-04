import pandas as pd
import re
b1 = {}
def fonk1(structure_file, b24, a1):
    b2 = fonk3(structure_file)
    b3 = fonk5(b24, b2)
    b4 = fonk8(b2, b3, a1)
    return b4
def fonk2(structure_file, b24):
    b2 = fonk3(structure_file)
    b3 = fonk5(b24, b2)
    b4 = fonk9(b1, b3)
    return b4
def fonk3(structure_file):
    b2 = {}
    b5 = ""
    for line in structure_file:
        b6 = re.split('\s+', line.strip())
        if b6[2] == "NUMERIC":
            b5 = "N"
        else:
            b5 = "C"
        b2[b6[1]] = b5
    return b2
def fonk4(structure_file):
    b7 = {}
    for line in structure_file:
        b6 = re.split('\s+', line.strip())
        if b6[2] == "NUMERIC":
            b8 = b18
        else:
            b9 = b6[2].replace('{', '')
            b10 = b9.replace('}', '')
            b8 = b10.split(',')
        b7[b6[1]] = b8
    return b7
def fonk5(b24, b2):
    for key in b2:
        if b2[key] == "N":
            b24[key].fillna(b24.groupby("class")[key].transform("mean"), b11 = True)
    for key in b2:
        if b2[key] == "C":
            b24[key] = b24[key].fillna(b24[key].mode()[0])
    return b24
def fonk6(col, k, key):
    global b1
    b12 = col.min()
    b13 = col.max()
    b14 = []
    b15 = (b13 - b12) / k
    for i in range(0, k - 1):
        b16 = b12 + (i + 1) * b15
        if b16 != b12 and b16 != b13:
            b14.append(b16)
    b17 = [b12] + b14 + [b13]
    global b18
    b18 = range(len(b14) + 1)
    b19 = [b17, b18]
    b1[key] = b19
    b20 = pd.cut(col, bins=b17, b18=b18, include_lowest=True)
    return b20
def fonk7(col, b17, b18):
    b20 = pd.cut(col, bins=b17, b18=b18, include_lowest=True)
    return b20
def fonk8(b2, b24, a1):
    for key in b2:
        if b2[key] == "N":
            b24[key] = fonk6(b24[key], a1, key)
    return b24
def fonk9(b1, b24):
    for key in b1:
        b24[key] = fonk7(b24[key], b1[key][0], b1[key][1])
    return b24
if b21 = = "__main__":
    b22 = structure_file = b22.strip().split('\n')
    b23 = {
        'age': [25, 30, 35, None, 40],
        'income': [50000, 60000, None, 80000, 100000],
        'student': ['yes', 'no', 'yes', None, 'no'],
        'credit_rating': ['fair', 'excellent', 'fair', 'excellent', None],
        'class': ['yes', 'no', 'yes', 'no', 'yes']
    }
    b24 = pd.DataFrame(b23)
    a1 = 3
    b25 = fonk1(structure_file, b24, a1)
    print("Training b23 after preprocessing:")
    print(b25)
    b26 = {
        'age': [28, 34, None, 45, 50],
        'income': [54000, 72000, 81000, 92000, None],
        'student': ['yes', 'no', 'yes', 'no', None],
        'credit_rating': ['excellent', 'fair', 'fair', 'excellent', 'fair'],
        'class': ['no', 'yes', 'no', 'yes', 'no']
    }
    b27 = pd.DataFrame(b26)
    b28 = fonk2(structure_file, b27)
    print("Test b23 after preprocessing:")
    print(b28)