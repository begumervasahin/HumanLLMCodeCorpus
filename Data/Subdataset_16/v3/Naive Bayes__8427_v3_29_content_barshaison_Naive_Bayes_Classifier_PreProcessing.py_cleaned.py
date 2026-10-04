import pandas as pd
import re
b1 = {}
def fonk1(structure_file, df, a1):
    b2 = fonk3(structure_file)
    b3 = fonk4(df, b2)
    b4 = fonk7(b2, b3, a1)
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
    for key, b6 in b2.items():
        if b6 = = "N":
            df[key].fillna(df.groupby("class")[key].transform("mean"), b7 = True)
        elif b6 = = "C":
            df[key].fillna(df[key].mode()[0], b7 = True)
    return df
def fonk5(col, a1, key):
    global b1
    min_val, b8 = col.min(), col.max()
    b9 = [min_val + (i + 1) * (b8 - min_val) / a1 for i in range(a1 - 1)]
    b10 = [min_val] + b9 + [b8]
    b11 = range(len(b9) + 1)
    b1[key] = [b10, b11]
    return pd.cut(col, b12 = b10, b11=b11, include_lowest=True)
def fonk6(col, b10, b11):
    return pd.cut(col, b12 = b10, b11=b11, include_lowest=True)
def fonk7(b2, df, a1):
    for key, b6 in b2.items():
        if b6 = = "N":
            df[key] = fonk5(df[key], a1, key)
    return df
def fonk8(b1, df):
    for key, (b10, b11) in b1.items():
        df[key] = fonk6(df[key], b10, b11)
    return df
if b13 = = "__main__":
    b14 = structure_file = b14.strip().split('\n')
    b15 = {
        'age': [25, 30, 35, None, 40],
        'income': [50000, 60000, None, 80000, 100000],
        'student': ['yes', 'no', 'yes', None, 'no'],
        'credit_rating': ['fair', 'excellent', 'fair', 'excellent', None],
        'class': ['yes', 'no', 'yes', 'no', 'yes']
    }
    b16 = pd.DataFrame(b15)
    a1 = 3
    b17 = fonk1(structure_file, b16, a1)
    print("Training data after preprocessing:")
    print(b17)
    b18 = {
        'age': [28, 34, None, 45, 50],
        'income': [54000, 72000, 81000, 92000, None],
        'student': ['yes', 'no', 'yes', 'no', None],
        'credit_rating': ['excellent', 'fair', 'fair', 'excellent', 'fair'],
        'class': ['no', 'yes', 'no', 'yes', 'no']
    }
    b19 = pd.DataFrame(b18)
    b20 = fonk2(structure_file, b19)
    print("Test data after preprocessing:")
    print(b20)