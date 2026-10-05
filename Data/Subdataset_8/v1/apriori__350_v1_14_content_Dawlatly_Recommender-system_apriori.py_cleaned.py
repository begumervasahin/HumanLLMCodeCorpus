import numpy as np
import pandas as pd
from apyori import apriori
dataset = pd.read_csv('FYP.csv')
customer_ID = dataset.iloc[:, [5, 10]].values
customer_ID = customer_ID[customer_ID[:, 0].argsort()]
anlist = [['Labels']]
for i in range(0, 9426):
    if i == 0:
        continue
    if customer_ID[i][0] == customer_ID[i - 1][0]:
        anlist[-1].append(str(customer_ID[i][1]))
    else:
        anlist[-1] = list(set(anlist[-1]))
        anlist.append([str(customer_ID[i][1])])
rules = apriori(anlist, min_support=0.02, min_confidence=0.2, min_lift=1.4, min_length=2)
results = list(rules)
def inspect(results):
    rh = [tuple(result[2][0][0]) for result in results]
    lh = [tuple(result[2][0][1]) for result in results]
    supports = [result[1] for result in results]
    confidences = [result[2][0][2] for result in results]
    lifts = [result[2][0][3] for result in results]
    return list(zip(rh, lh, supports, confidences, lifts))
resultDataFrame = pd.DataFrame(inspect(results))
lhs = [resultDataFrame[1][i][0] for i in range(resultDataFrame.__len__())]
rhs = [resultDataFrame[0][j] for j in range(resultDataFrame.__len__())]
finalLhs = [lhs[0], lhs[1], lhs[2], lhs[4], lhs[5], lhs[9], lhs[10], lhs[16], lhs[17], lhs[21], lhs[24], lhs[32], lhs[33], lhs[35], lhs[42], lhs[47], lhs[50], lhs[51], lhs[55]]
finalRhs = [rhs[0], rhs[1], rhs[2], rhs[4], rhs[5], rhs[9], rhs[10], rhs[16], rhs[17], rhs[21], rhs[24], rhs[32], rhs[33], rhs[35], rhs[42], rhs[47], rhs[50], rhs[51], rhs[55]]
print("Final LHS Values:")
print(finalLhs)
print("Final RHS Values:")
print(finalRhs)