
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
b1 = pd.read_csv('Market_Basket_Optimisation.csv', header=None)
b2 = []
for i in range(len(b1)):
    b3 = [str(b1.values[i, j]) for j in range(len(b1.columns))]
    b2.append(b3)
a1 = 0.003
a2 = 0.2
a3 = 3
a4 = 2
b4 = apriori(b2, a1=a1, a2=a2, a3=a3, a4=a4)
b5 = list(b4)
for result in b5:
    print(result)