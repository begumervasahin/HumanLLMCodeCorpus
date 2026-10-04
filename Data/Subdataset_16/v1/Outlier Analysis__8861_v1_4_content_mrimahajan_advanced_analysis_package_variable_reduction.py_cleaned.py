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
    def fonk2(i, a1):
        b5[i] = True
        b4[a1].append(i)
        for j in b3[i]:
            if not b5[j]:
                fonk2(j, a1)
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
    def fonk4(c1, c2):
        return np.max([[np.abs(b2.loc[i, j]) for i in b7[c1]] for j in b7[c2]])
    def fonk5(c):
        a2 = 0
        b9 = c
        for c1 in [i for i in b7.keys() if i != c]:
            b10 = fonk4(c, c1)
            if b10 > a2:
                a2 = b10
                b9 = c1
        return b9
    def fonk6(col, b19, b20):
        b11 = np.array(data[col])
        b12 = np.array(data[b19].drop(b8=[col]))
        b13 = np.array(data[b20])
        b14 = LinearRegression().fit(b12, b11)
        b15 = r2_score(b11, b14.predict(b12))
        b16 = LinearRegression().fit(b13, b11)
        b17 = r2_score(b11, b16.predict(b13))
        return (1 - b15) / (1 - b17)
    b2 = data.corr()
    for c1 in b7.keys():
        b18 = len(b7[c1])
        if b18 > 1:
            b19 = b7[c1]
            b20 = b7[fonk5(c1)]
            b21 = [(col, fonk6(col, b19, b20)) for col in b7[c1]]
            b21.sort(b22 = lambda x: x[1])
            if maxdrop is not None:
                b8 += [col[0] for col in b21[:-min(maxdrop, b18)]]
            else:
                b8 += [col[0] for col in b21[:min(maxkeep, b18)]]
        else:
            b8.append(b7[c1][0])
    return b8
def fonk7(data, b23 = 2.5):
    b24 = []
    def fonk8(df):
        b25 = pd.DataFrame()
        b25['feature'] = df.b8
        b25['VIF'] = [variance_inflation_factor(df.values, i) for i in range(df.shape[1])]
        return b25
    def fonk9(df, b1 = b23):
        b25 = fonk8(df)
        while b25['VIF'].max() > b1:
            b26 = b25.loc[b25['VIF'].idxmax(), 'feature']
            df.drop(b8 = [b26], inplace=True)
            b24.append(b26)
            b25 = fonk8(df)
    fonk9(data)
    return b24
def fonk10(df, dependent_var, b27 = True, alpha=0.05):
    b28 = [dependent_var]
    while True:
        if b27:
            b29 = sm.OLS(df[dependent_var], df.drop(b8=b28)).fit()
        else:
            b29 = sm.Logit(df[dependent_var], df.drop(b8=b28)).fit()
        b30 = b29.b30
        b31 = b30.max()
        if b31 > alpha:
            b32 = b30.idxmax()
            b28.append(b32)
        else:
            break
    b28.remove(dependent_var)
    return b28