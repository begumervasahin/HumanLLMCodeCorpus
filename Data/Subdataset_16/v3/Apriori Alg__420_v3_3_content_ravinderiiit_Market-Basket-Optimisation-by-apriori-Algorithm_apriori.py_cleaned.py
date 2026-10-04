
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
b1 = pd.read_csv('Market_Basket_Optimisation.csv', header=None)
b2 = [
    [str(b1.values[i, j]) for j in range(b1.shape[1]) if pd.notna(b1.values[i, j])]
    for i in range(b1.shape[0])
]
a1 = 0.003
a2 = 0.2
a3 = 3
a4 = 2
b3 = apriori(
    b2,
    a1 = a1,
    a2 = a2,
    a3 = a3,
    a4 = a4
)
b4 = list(b3)
def fonk1(b4):
    b5 = [tuple(result.items_base) for result in b4]
    b6 = [tuple(result.items_add) for result in b4]
    b7 = [result.support for result in b4]
    b8 = [result.ordered_statistics[0].confidence for result in b4]
    b9 = [result.ordered_statistics[0].lift for result in b4]
    return list(zip(b5, b6, b7, b8, b9))
b10 = pd.DataFrame(fonk1(b4), columns=['Left Hand Side', 'Right Hand Side', 'Support', 'Confidence', 'Lift'])
print(b10)