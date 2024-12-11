
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
b1 = pd.read_csv('Market_Basket_Optimisation.csv', header=None)
b2 = []
for i in range(len(b1)):
    b3 = [str(b1.values[i, j]) for j in range(len(b1.columns))]
    b2.append(b3)
b4 = apriori(b2, min_support=0.003, min_confidence=0.2, min_lift=3, min_length=2)
b5 = list(b4)
for result in b5:
    print(result)