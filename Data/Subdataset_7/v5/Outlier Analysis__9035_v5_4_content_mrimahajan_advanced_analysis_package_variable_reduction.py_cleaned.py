import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statsmodels.discrete.discrete_model as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
def fonk1(data, b1 = 0.7):
    b2 = data.corr()
    b3 = {}
    b4 = data.b4
    def fonk2(i, a1):
        b6[i] = True
        b3.setdefault(a1, []).append(i)
        for j in b5[i]:
            if not b6[j]:
                fonk2(j, a1)
    b5 = {i: [] for i in range(len(b4))}
    for i in range(len(b4)):
        for j in range(len(b4)):
            if i != j and abs(b2.iloc[i, j]) > b1:
                b5[i].append(j)
    b6 = [False] * len(b4)
    a1 = 0
    for i in range(len(b4)):
        if not b6[i]:
            fonk2(i, a1)
            a1 += 1
    b7 = {key: [b4[i] for i in val] for key, val in b3.items()}
    return b7
def fonk3(data, b1, b8 = 1, maxdrop=None):
    b4 = []
    b2 = data.corr()
    b3 = fonk1(data, b1=b1)
    def fonk4(c1, c2):
        return np.max([[abs(b2.loc[i, j]) for i in b3[c1]] for j in b3[c2]])
    def fonk5(c):
        a2 = 0
        b9 = c
        for c1 in [i for i in b3.keys() if i != c]:
            b10 = fonk4(c, c1)
            if b10 > a2:
                a2 = b10
                b9 = c1
        return b9
    def fonk6(col, own_cluster, b18):
        b11 = data[col].values
        b12 = data[own_cluster].drop(col, b24=1).values
        b13 = LinearRegression().fit(b12, b11)
        b14 = b13.predict(b12)
        b15 = r2_score(b11, b14)
        b12 = data[b18].values
        b13 = LinearRegression().fit(b12, b11)
        b14 = b13.predict(b12)
        b16 = r2_score(b11, b14)
        return float(1 - b15) / (1 - b16)
    for c1, own_cluster in b3.items():
        b17 = len(own_cluster)
        if b17 > 1:
            b18 = b3[fonk5(c1)]
            b19 = [(col, fonk6(col, own_cluster, b18)) for col in own_cluster]
            b19 = sorted(b19, key=lambda b12: b12[1])
            if maxdrop is not None:
                b4 += [col[0] for col in b19[:-min(maxdrop, b17)]]
            else:
                b4 += [col[0] for col in b19[:min(b8, b17)]]
        else:
            b4.append(own_cluster[0])
    return b4
def fonk7(data, b20 = 2.5):
    b21 = []
    def fonk8(fn_data):
        b22 = pd.DataFrame({'features': fn_data.b4,
                            'b22 factor': [variance_inflation_factor(fn_data.values, i) for i in range(fn_data.shape[1])]})
        b22.sort_values(b23 = 'b22 factor', ascending=False, inplace=True)
        return b22.iloc[0]
    def fonk9(fn_data, b1 = b20):
        b22 = fonk8(fn_data)
        if b22['b22 factor'] <= b1:
            return
        else:
            fn_data.drop(b22['features'], b24 = 1, inplace=True)
            b21.append(b22['features'])
            fonk9(fn_data, b1 = b20)
    fonk9(data)
    return b21
def fonk10(df, dv, b25 = True, alpha=0.05):
    b26 = [dv]
    b27 = sm.OLS if b25 else sm.Logit
    while True:
        b13 = b27(endog=df[dv].values, exog=df.drop(b26, b24=1).values)
        b28 = b13.fit()
        b29 = list(b28.b29)
        b30 = b29.index(max(b29))
        b31 = df.drop(b26, b24=1).b4[b30]
        if b29[b30] > alpha:
            b26.append(b31)
        else:
            break
    b26.remove(dv)
    return b26