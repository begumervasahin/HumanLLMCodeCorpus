import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
b1 = pd.read_csv('D:\\Shreyas Kulkarni\\Documents\\PycharmProjects\\MarketAnalysis_Apriori_Basic\\b1.csv', header=None)
b2 = []
for i in range(0, len(b1)):
    b2.append([str(b1.values[i, j]) for j in range(0, b1.shape[1])])
b3 = apriori(b2, min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=2)
b4 = list(b3)
print(f"Number of association rules: {len(b4)}")
if b4:
    print("First association rule:")
    b5 = b4[0]
    print(f"Items: {list(b5.b7)}")
    print(f"Support: {b5.support}")
    for ordered_stat in b5.ordered_statistics:
        print(f"Confidence: {ordered_stat.confidence}")
        print(f"Lift: {ordered_stat.lift}")
    print("=====================================")
for item in b4:
    b6 = item.b7
    b7 = [x for x in b6]
    print(f"Rule: {b7[0]} -> {b7[1] if len(b7) > 1 else ''}")
    print(f"Support: {item.support}")
    for ordered_stat in item.ordered_statistics:
        print(f"Confidence: {ordered_stat.confidence}")
        print(f"Lift: {ordered_stat.lift}")
    print("=====================================")