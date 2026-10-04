15. Repository: DiptaGomes/Apriori-Association-Rule-Mining-
   File: implementation.py
   URL: https:
   Code Content:
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
b1 = pd.read_csv('Nursery.csv', header = 1)
b2 = []
for i in range(1, 9409):
    b2.append([str(b1.values[i,j]) for j in range(0, 9)])
from apyori import apriori
b3 = apriori(b2, min_support = 0.04, min_confidence = .90, min_lift = 3, min_length = 2)
b4 = list(b3)
print(b4)
for item in b4:
    b5 = item[0]
    b6 = [x for x in b5]
    print("Rule: " + b6[0] + " -> " + b6[1])
    print("Support: " + str(item[1]))
    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")
   README Content:
