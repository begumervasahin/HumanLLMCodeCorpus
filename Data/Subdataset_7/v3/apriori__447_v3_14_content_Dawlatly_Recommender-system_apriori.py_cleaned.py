import pandas as pd
from apyori import apriori
b1 = pd.read_csv('FYP.csv')
b2 = b1.iloc[:, [5, 10]].values
b2 = b2[b2[:, 0].argsort()]
b3 = []
b4 = []
for i in range(len(b2)):
    if i > 0 and b2[i][0] != b2[i - 1][0]:
        b3.append(list(set(b4)))
        b4 = []
    b4.append(str(b2[i][1]))
b3.append(list(set(b4)))
b5 = apriori(b3, min_support=0.02, min_confidence=0.2, min_lift=1.4, min_length=2)
b6 = list(b5)
def fonk1(b6):
    b7 = []
    for result in b6:
        b8 = tuple(result.ordered_statistics[0].items_base)
        b9 = tuple(result.ordered_statistics[0].items_add)
        b10 = result.b10
        b11 = result.ordered_statistics[0].b11
        b12 = result.ordered_statistics[0].b12
        b7.append((b8, b9, b10, b11, b12))
    return b7
b7 = fonk1(b6)
b13 = [result[1] for result in b7[:19]]
b14 = [result[0] for result in b7[:19]]
print("Final LHS Values:")
print(b13)
print("Final RHS Values:")
print(b14)