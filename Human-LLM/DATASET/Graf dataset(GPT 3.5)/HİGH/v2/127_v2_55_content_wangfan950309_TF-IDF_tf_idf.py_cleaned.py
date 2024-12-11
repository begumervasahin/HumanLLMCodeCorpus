import pandas as pd
import math
import numpy as np
def fonk1(b9, b8):
    b1 = b9.split()
    b2 = {}
    b3 = pd.read_csv(b8, index_col=None)
    b4 = b3['Job_Name'].tolist()
    for term in b1:
        b5 = sum(1 for name in b4 if term in name)
        b2[term] = math.log(len(b3) / (1 + b5))
    b3['TF-IDF'] = 0
    for term in b1:
        b6 = []
        for name in b4:
            b7 = len(name.split())
            b5 = sum(1 for word in name.split() if word.lower() == term.lower())
            b6.append(b5 / b7)
        b3[term] = np.array(b6) * b2[term]
        b3['TF-IDF'] += b3[term]
    b3 = b3.sort_values(by='TF-IDF', ascending=False)
    b3 = b3.loc[b3['TF-IDF'] != 0]
    b3 = b3.iloc[:, :4]
    return b3
b8 = "path_to_your_data/Job_search.csv"
b9 = "data science"
b10 = fonk1(b9, b8)
print(b10)