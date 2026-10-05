import pandas as pd
import math
import numpy as np
def fonk1(b7, b9):
    b1 = {}
    b2 = len(b9)
    for term in b7:
        b3 = sum(1 for name in b9 if term in name)
        b1[term] = math.log(b2 / (1 + b3))
    return b1
def fonk2(b7, b1, b9):
    b4 = pd.DataFrame()
    for term in b7:
        b5 = []
        for name in b9:
            b6 = len(name.split())
            b3 = sum(1 for word in name.split() if word.lower() == term.lower())
            b5.append(b3 / b6)
        b4[term] = np.array(b5) * b1[term]
    return b4
def fonk3(b12, b11):
    b7 = b12.split()
    b8 = pd.read_csv(b11, index_col=None)
    b9 = b8['Job_Name'].tolist()
    b1 = fonk1(b7, b9)
    b4 = fonk2(b7, b1, b9)
    b8['TF-IDF'] = b4.sum(b10 = 1)
    b8 = b8.sort_values(by='TF-IDF', ascending=False)
    b8 = b8.loc[b8['TF-IDF'] != 0]
    b8 = b8.iloc[:, :4]
    return b8
b11 = "path_to_your_data/Job_search.csv"
b12 = "data science"
b13 = fonk3(b12, b11)
print(b13)