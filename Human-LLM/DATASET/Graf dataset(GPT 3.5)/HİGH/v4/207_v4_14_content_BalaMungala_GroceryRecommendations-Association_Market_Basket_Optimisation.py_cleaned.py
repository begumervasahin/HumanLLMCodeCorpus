
import pandas as pd
from apyori import apriori
import matplotlib.pyplot as plt
b1 = "F:
b2 = pd.read_csv(b1, header=None)
b3 = []
for i in range(0, len(b2)):
    b3.append([str(b2.values[i, j]) for j in range(0, 20)])
b4 = apriori(b3,
                b5 = 0.003,
                b6 = 0.2,
                b7 = 2,
                b8 = 3)
b9 = list(b4)
plt.itemFrequency(b9)