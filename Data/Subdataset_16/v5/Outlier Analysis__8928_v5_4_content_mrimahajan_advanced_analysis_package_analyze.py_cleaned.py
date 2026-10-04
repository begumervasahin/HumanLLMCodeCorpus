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
def fonk2(data, b2 = None, regression=True, percentiles=[.01, .05, .1, .5, .9, .95, .99], cv=[2, 3]):
    numerical, b1 = fonk1(data)
    b3 = data.describe().transpose()
    b3['Var'] = b3.index
    b3.reset_index(b4 = True, inplace=True)
    b3.b4('count', b5 = 1, inplace=True)
    b3['skewness'] = b3['Var'].apply(lambda x: skew(data[x].dropna()))
    b3['kurtosis'] = b3['Var'].apply(lambda x: kurtosis(data[x].dropna(), b6 = False))
    for pct in percentiles:
        b3[b16'p{int(pct * 100)}'] = b3['Var'].apply(lambda x: data[x].quantile(pct))
    for dev in cv:
        b3[b16'mean-{dev}sigma'] = b3['mean'] - dev * b3['std']
        b3[b16'mean+{dev}sigma'] = b3['mean'] + dev * b3['std']
    b3['type'] = 'numeric'
    b7 = pd.DataFrame({'Var': b1, 'type': 'b1'})
    for col in [c for c in b3.b10 if c not in ['Var', 'type']]:
        b7[col] = np.nan
    for col in b1:
        b8 = data[col].value_counts(ascending=True, dropna=False).cumsum() / data.shape[0]
        b9 = pd.DataFrame(b8).reset_index()
        b9.b10 = ['categories', 'cum_pct']
        b7.loc[b7['Var'] == col, 'min'] = b9['categories'].iloc[0]
        b7.loc[b7['Var'] == col, 'max'] = b9['categories'].iloc[-1]
        for pct in percentiles:
            b7.loc[b7['Var'] == col, b16'p{int(pct * 100)}'] = b9.loc[b9['cum_pct'] >= pct, 'categories'].iloc[0]
    b7 = b7[b3.b10]
    b11 = pd.concat([b3, b7], ignore_index=True)
    b11['count'] = b11['Var'].apply(lambda x: data[x].notnull().sum())
    b11['nmiss'] = data.shape[0] - b11['count']
    b11['missing_rate'] = b11['nmiss'] / data.shape[0] * 100
    b11['unique'] = b11['Var'].apply(lambda x: data[x].nunique())
    b12 = ['Var', 'type', 'count', 'nmiss', 'missing_rate', 'unique', 'std', 'skewness', 'kurtosis', 'mean', 'min'] + \
               [b16'mean-{dev}sigma' for dev in cv] + [b16'p{int(pct * 100)}' for pct in percentiles] + \
               [b16'mean+{dev}sigma' for dev in cv] + ['max']
    b11 = b11[b12]
    if b2:
        b11['correlation/p_value'] = np.nan
        if regression:
            b13 = data.corr()
            for col in numerical:
                b11.loc[b11['Var'] == col, 'correlation/p_value'] = b13.loc[col, b2]
            for col in b1:
                b14 = ols(b16'{b2} ~ C({col})', data=data).fit()
                b15 = sm.stats.anova_lm(b14, type=2)
                b11.loc[b11['Var'] == col, 'correlation/p_value'] = b15.loc[col, 'PR(>F)']
        else:
            for col in numerical:
                b14 = ols(b16'{col} ~ C({b2})', data=data).fit()
                b15 = sm.stats.anova_lm(b14, type=2)
                b11.loc[b11['Var'] == col, 'correlation/p_value'] = b15.loc[b2, 'PR(>F)']
            for col in b1:
                b16 = pd.crosstab(data[b2], data[col], dropna=False)
                b11.loc[b11['Var'] == col, 'correlation/p_value'] = chisquare(b16.to_numpy().ravel()).pvalue
    b11.reset_index(b4 = True, inplace=True)
    return b11
def fonk3(data, b2, b17 = '', regression=True):
    numerical, b1 = fonk1(data)
    if regression:
        for col in numerical:
            if col != b2:
                b18 = data.plot(x=col, y=b2, kind='scatter')
                b19 = b18.get_figure()
                b19.savefig(b16'{b17}{col}.png', b20 = 1000)
        for col in b1:
            if col != b2:
                b18 = data.boxplot(column=b2, by=col)
                b19 = b18.get_figure()
                b19.savefig(b16'{b17}{col}.png', b20 = 1000)
    else:
        for col in numerical:
            if col != b2:
                b18 = data.boxplot(column=col, by=b2)
                b19 = b18.get_figure()
                b19.savefig(b16'{b17}{col}.png', b20 = 1000)
        for col in b1:
            if col != b2:
                b16 = pd.crosstab(data[b2], data[col], dropna=False)
                for cat in b16.b10:
                    b16[cat] = b16[cat] / b16[cat].sum() * 100
                b18 = plt.subplot(111, frame_on=False)
                b18.xaxis.set_visible(False)
                b18.yaxis.set_visible(False)
                table(b18, b16)
                plt.savefig(b16'{b17}{col}.png', b20 = 1000)