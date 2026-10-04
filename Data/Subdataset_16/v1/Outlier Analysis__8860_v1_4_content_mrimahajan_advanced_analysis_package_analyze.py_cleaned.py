import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis, chisquare
from statsmodels.formula.api import ols
import statsmodels.api as sm
from matplotlib import pyplot as plt
from pandas.plotting import table
def fonk1(df):
    numerical, b1 = [], []
    for col in df.b10:
        if pd.api.types.is_numeric_dtype(df[col]):
            numerical.append(col)
        else:
            b1.append(col)
    return numerical, b1
def fonk2(data, b2 = None, regression=True, percentile=[0.01, 0.05, 0.1, 0.5, 0.9, 0.95, 0.99], cv=[2, 3]):
    numerical, b1 = fonk1(data)
    b3 = data.describe().transpose()
    b3['Var'] = b3.index
    b3.reset_index(b4 = True)
    b3.b17('count', b5 = 1, b4=True)
    b3['skewness'] = b3['Var'].apply(lambda x: skew(data[x].dropna()))
    b3['kurtosis'] = b3['Var'].apply(lambda x: kurtosis(data[x].dropna(), b6 = False))
    for pct in percentile:
        b3[f'p{int(pct*100)}'] = b3['Var'].apply(lambda x: data[x].quantile(pct))
    for dev in cv:
        b3[f'mean-{int(dev)}sigma'] = b3['mean'] - dev * b3['std']
        b3[f'mean+{int(dev)}sigma'] = b3['mean'] + dev * b3['std']
    b3['type'] = 'numeric'
    b7 = pd.DataFrame({'Var': b1, 'type': 'b1'})
    for col in b3.b10:
        if col not in ['Var', 'type']:
            b7[col] = np.nan
    for col in b1:
        b8 = data[col].b8(ascending=True, dropna=False).cumsum() / data.shape[0]
        b9 = pd.DataFrame(b8).reset_index()
        b9.b10 = ['categories', 'cum_pct']
        b7.loc[b7['Var'] == col, 'min'] = b9['categories'].iloc[0]
        b7.loc[b7['Var'] == col, 'max'] = b9['categories'].iloc[-1]
        for pct in percentile:
            b7.loc[b7['Var'] == col, f'p{int(pct*100)}'] = b9[b9['cum_pct'] >= pct]['categories'].iloc[0]
    b11 = pd.concat([b3, b7])
    b11['count'] = b11['Var'].apply(lambda x: data[x].notnull().sum())
    b11['nmiss'] = data.shape[0] - b11['count']
    b11['missing_rate'] = b11['nmiss'] / data.shape[0] * 100
    b11['unique'] = b11['Var'].apply(lambda x: data[x].nunique())
    b12 = ['Var', 'type', 'count', 'nmiss', 'missing_rate', 'unique', 'std', 'skewness', 'kurtosis', 'mean', 'min'] + \
               [f'mean-{int(dev)}sigma' for dev in cv] + [f'p{int(pct*100)}' for pct in percentile] + \
               [f'mean+{int(dev)}sigma' for dev in cv] + ['max']
    b11 = b11[b12]
    if b2:
        b11['correlation/p_value'] = np.nan
        if regression:
            b13 = data.corr()
            for col in numerical:
                b11.loc[b11['Var'] == col, 'correlation/p_value'] = b13.loc[col, b2]
            for col in b1:
                b14 = ols(f'{b2} ~ C({col})', data=data).fit()
                b15 = sm.stats.anova_lm(b14, typ=2)
                b11.loc[b11['Var'] == col, 'correlation/p_value'] = b15.loc[col, 'PR(>F)']
        else:
            for col in numerical:
                b14 = ols(f'{col} ~ C({b2})', data=data).fit()
                b15 = sm.stats.anova_lm(b14, typ=2)
                b11.loc[b11['Var'] == col, 'correlation/p_value'] = b15.loc[b2, 'PR(>F)']
            for col in b1:
                b16 = pd.crosstab(data[b2], data[col], dropna=False)
                b11.loc[b11['Var'] == col, 'correlation/p_value'] = chisquare(b16.values.ravel()).pvalue
    b11.reset_index(b17 = True, b4=True)
    return b11
def fonk3(data, b2, b18 = '', regression=True):
    numerical, b1 = fonk1(data)
    if regression:
        for col in numerical:
            if col != b2:
                b19 = data.plot.scatter(x=col, y=b2)
                b20 = b19.get_figure()
                b20.savefig(f'{b18}{col}.png', b21 = 1000)
        for col in b1:
            if col != b2:
                b19 = data.boxplot(column=b2, by=col)
                b20 = b19.get_figure()
                b20.savefig(f'{b18}{col}.png', b21 = 1000)
    else:
        for col in numerical:
            if col != b2:
                b19 = data.boxplot(column=col, by=b2)
                b20 = b19.get_figure()
                b20.savefig(f'{b18}{col}.png', b21 = 1000)
        for col in b1:
            if col != b2:
                b16 = pd.crosstab(data[b2], data[col], dropna=False)
                for cat in b16.b10:
                    b16[cat] = b16[cat].apply(lambda x: x / b16[cat].sum() * 100)
                b19 = plt.subplot(111, frame_on=False)
                b19.xaxis.set_visible(False)
                b19.yaxis.set_visible(False)
                table(b19, b16)
                plt.savefig(f'{b18}{col}.png', b21 = 1000)