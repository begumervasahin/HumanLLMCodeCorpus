import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statsmodels.discrete.discrete_model as sm
from sklearn.preprocessing import StandardScaler
from patsy import dmatrices
from statsmodels.stats.outliers_influence import variance_inflation_factor
def fonk1(data, b1 = 0.7):
    b2 = data.corr()
    b3 = {}
    b4 = data.b4
    for i in range(len(b4)):
        b3[i] = []
        for j in range(len(b4)):
            if i != j and np.abs(b2.iloc[i, j]) > b1:
                b3[i].append(j)
    b5 = {}
    a1 = 0
    b6 = [0] * len(b4)
    def fonk2(i):
        b6[i] = 1
        try:
            b5[a1].append(i)
        except KeyError:
            b5[a1] = [i]
        for j in b3[i]:
            if b6[j] == 0:
                fonk2(j)
    for i in range(len(b4)):
        if b6[i] == 0:
            fonk2(i)
            a1 += 1
        else:
            continue
    b7 = {}
    for key in list(b5.keys()):
        b7[key] = [b4[i] for i in b5[key]]
    return b7
def fonk3(data, b1, b8 = 1, maxdrop=None):
    b4 = []
    b9 = fonk1(data, b1=b1)
    def fonk4(c1, c2):
        return np.max([[np.abs(b2.loc[i, j]) for i in b9[c1]] for j in b9[c2]])
    def fonk5(c):
        a2 = 0
        b10 = c
        for c1 in [i for i in list(b9.keys()) if i != c]:
            b11 = fonk4(c, c1)
            if b11 > a2:
                a2 = b11
                b10 = c1
        return b10
    def fonk6(col, b19, b20):
        b12 = np.array(data[col])
        b13 = np.array(data[b19].drop(col, b28=1))
        b14 = LinearRegression()
        b14.fit(b13, b12)
        b15 = list(b14.predict(b13))
        b16 = r2_score(b12, b15)
        del b13, b14
        b13 = np.array(data[b20])
        b14 = LinearRegression()
        b14.fit(b13, b12)
        b15 = list(b14.predict(b13))
        b17 = r2_score(b12, b15)
        del b12, b15, b14
        return float(1 - b16) / (1 - b17)
    for c1 in list(b9.keys()):
        b18 = len(b9[c1])
        if b18 > 1:
            b19 = b9[c1]
            b20 = b9[fonk5(c1)]
            b21 = []
            for col in b9[c1]:
                b22 = fonk6(col, b19, b20)
                b21.append((col, b22))
            b21 = sorted(b21, key=lambda b13: b13[1])
            if maxdrop is not None:
                b4 += [col[0] for col in b21[:-min(maxdrop, b18)]]
            else:
                b4 += [col[0] for col in b21[:min(b8, b18)]]
        else:
            b4.append(b9[c1][0])
    return b4
def fonk7(data, b23 = 2.5):
    b24 = []
    def fonk8(fn_data):
        b25 = pd.DataFrame()
        b25['features'] = fn_data.b4
        b25['b25 factor'] = [variance_inflation_factor(fn_data.values, i) for i in range(fn_data.shape[1])]
        b25.sort_values(b26 = 'b25 factor', ascending=False, b27=True)
        b25.reset_index(b27 = True, drop=True)
        print(b25)
        return tuple(b25.loc[0, :].values)
    def fonk9(fn_data, b1 = b23):
        b25 = fonk8(fn_data)
        if b25[1] <= b1:
            return
        else:
            fn_data.drop(b25[0], b28 = 1, b27=True)
            b24.append(b25[0])
            print(b25[0] + ' dropped')
            del b25
            fonk9(fn_data, b1 = b23)
    fonk9(data)
    return b24
def fonk10(df, dv, b29 = True, alpha=0.05):
    a3 = 0
    b30 = [dv]
    while a3 = = 0:
        if b29:
            b14 = sm.OLS(endog=np.array(df[dv]), exog=np.array(df.drop(b30, b28=1)))
        else:
            b14 = sm.Logit(endog=np.array(df[dv]), exog=np.array(df.drop(b30, b28=1)))
        b31 = b14.fit()
        b32 = list(b31.b32)
        b33 = b32.index(max(b32))
        b34 = df.drop(b30, b28=1).b4[b33]
        print(b34 + '-' + str(b32[b33]))
        if b32[b33] > alpha:
            b30.append(b34)
        else:
            a3 = 1
    b30.remove(dv)
    return b30
if b35 = = "__main__":
    b9 = fonk1(data, b1=0.7)
    print(b9)
    b36 = fonk3(data, b1=0.7)
    print(b36)
    b37 = fonk7(data, b23=2.5)
    print(b37)
    b38 = fonk10(data, dv='target_variable', b29=True, alpha=0.05)
    print(b38)