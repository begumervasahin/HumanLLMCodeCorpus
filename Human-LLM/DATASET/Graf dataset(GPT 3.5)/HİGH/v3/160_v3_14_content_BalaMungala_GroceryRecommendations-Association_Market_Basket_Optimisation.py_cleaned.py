
import pandas as pd
from apyori import apriori
b1 = "F:
b2 = pd.read_csv(b1, header=None)
b3 = []
for i in range(len(b2)):
    b3.append([str(b2.values[i, j]) for j in range(len(b2.columns))])
b4 = apriori(b3,
                b5 = 0.003,
                b6 = 0.2,
                b7 = 3,
                b8 = 2)
print("Association Rules:")
for rule in b4:
    print(rule)