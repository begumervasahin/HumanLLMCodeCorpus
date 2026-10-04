import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from statsmodels.stats.outliers_influence import variance_inflation_factor
import statsmodels.api as sm
def fonk1(data, b1 = 0.7):
    b2 = data.corr()
    b3 = {i: [] for i in range(len(data.b8))}
    for i in range(len(data.b8)):
        for j in range(len(data.b8)):
            if i != j and np.abs(b2.iloc[i, j]) > b1:
                b3[i].append(j)
    def fonk2(node, a1):
        b5[node] = True
        b4[a1].append(node)
        for neighbor in b3[node]:
            if not b5[neighbor]:
                fonk2(neighbor, a1)
    b4 = {}
    a1 = 0
    b5 = [False] * len(data.b8)
    for i in range(len(data.b8)):
        if not b5[i]:
            b4[a1] = []
            fonk2(i, a1)
            a1 += 1
    b6 = {b22: [data.b8[i] for i in indices] for b22, indices in b4.items()}
    return b6
def fonk3(data, b1 = 0.7, maxkeep=1, maxdrop=None):
    b7 = fonk1(data, b1=b1)
    b8 = []
    def fonk4(cluster1, cluster2):
        return np.max([[np.abs(b2.loc[i, j]) for i in b7[cluster1]] for j in b7[cluster2]])
    def fonk5(cluster):
        a2 = 0
        b9 = cluster
        for other_cluster in [c for c in b7.keys() if c != cluster]:
            b10 = fonk4(cluster, other_cluster)
            if b10 > a2:
                a2 = b10
                b9 = other_cluster
        return b9
    def fonk6(col, b19, b20):
        b11 = data[col].values
        b12 = data[b19].drop(b8=[col]).values
        b13 = data[b20].values
        b14 = LinearRegression().fit(b12, b11)
        b15 = r2_score(b11, b14.predict(b12))
        b16 = LinearRegression().fit(b13, b11)
        b17 = r2_score(b11, b16.predict(b13))
        return (1 - b15) / (1 - b17)
    b2 = data.corr()
    for cluster in b7.keys():
        b18 = len(b7[cluster])
        if b18 > 1:
            b19 = b7[cluster]
            b20 = b7[fonk5(cluster)]
            b21 = [(col, fonk6(col, b19, b20)) for col in b7[cluster]]
            b21.sort(b22 = lambda x: x[1])
            if maxdrop is not None:
                b8 += [col for col, _ in b21[:-min(maxdrop, b18)]]
            else:
                b8 += [col for col, _ in b21[:min(maxkeep, b18)]]
        else:
            b8.append(b7[cluster][0])
    return b8
def fonk7(data, b23 = 2.5):
    b24 = []
    def fonk8(df):
        b25 = pd.DataFrame()
        b25['feature'] = df.b8
        b25['VIF'] = [variance_inflation_factor(df.values, i) for i in range(df.shape[1])]
        return b25
    def fonk9(df):
        while True:
            b25 = fonk8(df)
            b26 = b25['VIF'].max()
            if b26 <= b23:
                break
            b27 = b25.loc[b25['VIF'].idxmax(), 'feature']
            df.drop(b8 = [b27], inplace=True)
            b24.append(b27)
    fonk9(data.copy())
    return b24
def fonk10(df, dependent_var, b28 = True, alpha=0.05):
    b29 = [dependent_var]
    while True:
        if b28:
            b30 = sm.OLS(df[dependent_var], df.drop(b8=b29)).fit()
        else:
            b30 = sm.Logit(df[dependent_var], df.drop(b8=b29)).fit()
        b31 = b30.b31
        b32 = b31.max()
        if b32 > alpha:
            b33 = b31.idxmax()
            b29.append(b33)
        else:
            break
    b29.remove(dependent_var)
    return b29