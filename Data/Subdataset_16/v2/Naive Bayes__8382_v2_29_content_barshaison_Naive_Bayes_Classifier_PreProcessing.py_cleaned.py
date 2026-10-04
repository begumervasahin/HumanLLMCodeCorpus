import pandas as pd
import re
b1 = {}
def fonk1(structure_file, b18, a1):
    b2 = fonk3(structure_file)
    b3 = fonk5(b18, b2)
    b4 = fonk8(b2, b3, a1)
    return b4
def fonk2(structure_file, b18):
    b2 = fonk3(structure_file)
    b3 = fonk5(b18, b2)
    b4 = fonk9(b1, b3)
    return b4
def fonk3(structure_file):
    b2 = {}
    for line in structure_file:
        b5 = re.split(r'\s+', line.strip())
        b6 = "N" if b5[2] == "NUMERIC" else "C"
        b2[b5[1]] = b6
    return b2
def fonk4(structure_file):
    b7 = {}
    for line in structure_file:
        b5 = re.split(r'\s+', line.strip())
        if b5[2] == "NUMERIC":
            b8 = b13
        else:
            b8 = b5[2].replace('{', '').replace('}', '').split(',')
        b7[b5[1]] = b8
    return b7
def fonk5(b18, b2):
    for key, b6 in b2.items():
        if b6 = = "N":
            b18[key].fillna(b18.groupby("class")[key].transform("mean"), b9 = True)
        elif b6 = = "C":
            b18[key].fillna(b18[key].mode()[0], b9 = True)
    return b18
def fonk6(col, a1, key):
    global b1
    min_val, b10 = col.min(), col.max()
    b11 = [min_val + (i + 1) * (b10 - min_val) / a1 for i in range(a1 - 1)]
    b12 = [min_val] + b11 + [b10]
    b13 = range(len(b11) + 1)
    b1[key] = [b12, b13]
    return pd.cut(col, b14 = b12, b13=b13, include_lowest=True)
def fonk7(col, b12, b13):
    return pd.cut(col, b14 = b12, b13=b13, include_lowest=True)
def fonk8(b2, b18, a1):
    for key, b6 in b2.items():
        if b6 = = "N":
            b18[key] = fonk6(b18[key], a1, key)
    return b18
def fonk9(b1, b18):
    for key, (b12, b13) in b1.items():
        b18[key] = fonk7(b18[key], b12, b13)
    return b18
if b15 = = "__main__":
    b16 = structure_file = b16.strip().split('\n')
    b17 = {
        'age': [25, 30, 35, None, 40],
        'income': [50000, 60000, None, 80000, 100000],
        'student': ['yes', 'no', 'yes', None, 'no'],
        'credit_rating': ['fair', 'excellent', 'fair', 'excellent', None],
        'class': ['yes', 'no', 'yes', 'no', 'yes']
    }
    b18 = pd.DataFrame(b17)
    a1 = 3
    b19 = fonk1(structure_file, b18, a1)
    print("Training b17 after preprocessing:")
    print(b19)
    b20 = {
        'age': [28, 34, None, 45, 50],
        'income': [54000, 72000, 81000, 92000, None],
        'student': ['yes', 'no', 'yes', 'no', None],
        'credit_rating': ['excellent', 'fair', 'fair', 'excellent', 'fair'],
        'class': ['no', 'yes', 'no', 'yes', 'no']
    }
    b21 = pd.DataFrame(b20)
    b22 = fonk2(structure_file, b21)
    print("Test b17 after preprocessing:")
    print(b22)