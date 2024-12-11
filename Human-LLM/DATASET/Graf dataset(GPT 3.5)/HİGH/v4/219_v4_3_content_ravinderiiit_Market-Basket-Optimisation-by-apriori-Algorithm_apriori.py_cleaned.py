
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
b1 = pd.read_csv('Market_Basket_Optimisation.csv', header=None)
b2 = []
for i in range(0, 7501):
    b2.append([str(b1.values[i, j]) for j in range(0, 20)])
a1 = 0.003
a2 = 0.2
a3 = 3
a4 = 2
b3 = apriori(b2,
                a1 = a1,
                a2 = a2,
                a3 = a3,
                a4 = a4)
b4 = list(b3)
