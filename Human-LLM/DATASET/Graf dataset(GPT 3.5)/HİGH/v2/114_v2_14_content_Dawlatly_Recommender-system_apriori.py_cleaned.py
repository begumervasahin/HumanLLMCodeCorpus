import pandas as pd
from apyori import apriori
b1 = pd.read_csv('FYP.csv')
b2 = b1.iloc[:, [5, 10]].values
b2 = b2[b2[:, 0].argsort()]
b3 = [['Labels']]
for i in range(1, len(b2)):
    if b2[i][0] == b2[i - 1][0]:
        b3[-1].append(str(b2[i][1]))
    else:
        b3[-1] = list(set(b3[-1]))
        b3.append([str(b2[i][1])])
b4 = apriori(b3, min_support=0.02, min_confidence=0.2, min_lift=1.4, min_length=2)
b5 = list(b4)
def fonk1(b5):
    b6 = []
    for result in b5:
        b7 = tuple(result.ordered_statistics[0].items_base)
        b8 = tuple(result.ordered_statistics[0].items_add)
        b9 = result.b9
        b10 = result.ordered_statistics[0].b10
        b11 = result.ordered_statistics[0].b11
        b6.append((b7, b8, b9, b10, b11))
    return b6
b6 = fonk1(b5)
b12 = [result[1] for result in b6[:19]]
b13 = [result[0] for result in b6[:19]]
print("Final LHS Values:")
print(b12)
print("Final RHS Values:")
print(b13)