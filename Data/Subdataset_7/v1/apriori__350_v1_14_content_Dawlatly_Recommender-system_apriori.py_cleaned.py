import numpy as np
import pandas as pd
from apyori import apriori
b1 = pd.read_csv('FYP.csv')
b2 = b1.iloc[:, [5, 10]].values
b2 = b2[b2[:, 0].argsort()]
b3 = [['Labels']]
for b4 in range(0, 9426):
    if b4 = = 0:
        continue
    if b2[b4][0] == b2[b4 - 1][0]:
        b3[-1].append(str(b2[b4][1]))
    else:
        b3[-1] = list(set(b3[-1]))
        b3.append([str(b2[b4][1])])
b5 = apriori(b3, min_support=0.02, min_confidence=0.2, min_lift=1.4, min_length=2)
b6 = list(b5)
def fonk1(b6):
    b7 = [tuple(result[2][0][0]) for result in b6]
    b8 = [tuple(result[2][0][1]) for result in b6]
    b9 = [result[1] for result in b6]
    b10 = [result[2][0][2] for result in b6]
    b11 = [result[2][0][3] for result in b6]
    return list(zip(b7, b8, b9, b10, b11))
b12 = pd.DataFrame(fonk1(b6))
b13 = [b12[1][b4][0] for b4 in range(b12.__len__())]
b14 = [b12[0][j] for j in range(b12.__len__())]
b15 = [b13[0], b13[1], b13[2], b13[4], b13[5], b13[9], b13[10], b13[16], b13[17], b13[21], b13[24], b13[32], b13[33], b13[35], b13[42], b13[47], b13[50], b13[51], b13[55]]
b16 = [b14[0], b14[1], b14[2], b14[4], b14[5], b14[9], b14[10], b14[16], b14[17], b14[21], b14[24], b14[32], b14[33], b14[35], b14[42], b14[47], b14[50], b14[51], b14[55]]
print("Final LHS Values:")
print(b15)
print("Final RHS Values:")
print(b16)