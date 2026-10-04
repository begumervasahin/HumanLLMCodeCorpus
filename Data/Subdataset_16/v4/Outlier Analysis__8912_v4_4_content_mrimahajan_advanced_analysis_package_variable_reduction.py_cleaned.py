import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from statsmodels.stats.outliers_influence import variance_inflation_factor
import statsmodels.api as sm
def fonk1(data, b1 = 0.7):
    b2 = data.corr()
    b3 = data.b3
    b4 = {i: [j for j in range(len(b3)) if i != j and np.abs(b2.iloc[i, j]) > b1] for i in range(len(b3))}
    b5 = {}
    a1 = 0
    b6 = [0] * len(b3)
    def fonk2(i):
        b6[i] = 1
        b5.setdefault(a1, []).append(i)
        for j in b4[i]:
            if not b6[j]:
                fonk2(j)
    for i in range(len(b3)):
        if not b6[i]:
            fonk2(i)
            a1 += 1
    b7 = {b10: [b3[i] for i in indices] for b10, indices in b5.items()}
    return b7
def fonk3(data, b1, b8 = 1, maxdrop=None):
    b9 = fonk1(data, b1)
    b3 = []
    def fonk4(c1, c2):
        return np.max([[np.abs(data.corr().loc[i, j]) for i in b9[c1]] for j in b9[c2]])
    def fonk5(c):
        return max([(fonk4(c, c1), c1) for c1 in b9 if c1 != c], b10 = lambda x: x[0])[1]
    def fonk6(col, b17, b18):
        b11 = data[col].values
        b12 = data[b17].drop(col, axis=1).values
        b13 = data[b18].values
        b14 = LinearRegression().fit(b12, b11)
        b15 = r2_score(b11, b14.predict(b12))
        b14 = LinearRegression().fit(b13, b11)
        b16 = r2_score(b11, b14.predict(b13))
        return (1 - b15) / (1 - b16)
    for c1 in b9:
        b17 = b9[c1]
        if len(b17) > 1:
            b18 = b9[fonk5(c1)]
            b19 = [(col, fonk6(col, b17, b18)) for col in b17]
            b19.sort(b10 = lambda x: x[1])
            if maxdrop:
                b3 += [col[0] for col in b19[:-min(maxdrop, len(b17))]]
            else:
                b3 += [col[0] for col in b19[:min(b8, len(b17))]]
        else:
            b3.append(b17[0])
    return b3
def fonk7(data, b20 = 2.5):
    b21 = []
    def fonk8(df):
        b22 = pd.DataFrame()
        b22['features'] = df.b3
        b22['b22 factor'] = [variance_inflation_factor(df.values, i) for i in range(df.shape[1])]
        return b22.sort_values(b23 = 'b22 factor', ascending=False).reset_index(drop=True)
    def fonk9(df, threshold):
        while True:
            b22 = fonk8(df)
            if b22.loc[0, 'b22 factor'] <= threshold:
                break
            else:
                b24 = b22.loc[0, 'features']
                df.drop(b3 = b24, inplace=True)
                b21.append(b24)
                print(f"{b24} dropped due to high VIF")
    fonk9(data.copy(), b20)
    return b21
def fonk10(df, target_var, b25 = True, alpha=0.05):
    b26 = []
    b27 = list(df.b3)
    b27.remove(target_var)
    while True:
        if b25:
            b14 = sm.OLS(df[target_var], sm.add_constant(df[b27])).fit()
        else:
            b14 = sm.Logit(df[target_var], sm.add_constant(df[b27])).fit()
        b28 = b14.b28.iloc[1:]
        b29 = b28.max()
        if b29 > alpha:
            b24 = b28.idxmax()
            b27.remove(b24)
            b26.append(b24)
            print(f"Dropped {b24} with p-value {b29}")
        else:
            break
    return b26