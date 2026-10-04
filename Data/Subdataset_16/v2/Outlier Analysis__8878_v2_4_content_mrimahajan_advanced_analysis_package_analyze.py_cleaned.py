import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis, chisquare
from statsmodels.formula.api import ols
import statsmodels.api as sm
from matplotlib import pyplot as plt
from pandas.plotting import table
def fonk1(df):
    numerical, b1 = [], []
    for col in df.b9:
        if pd.api.types.is_numeric_dtype(df[col]):
            numerical.append(col)
        else:
            b1.append(col)
    return numerical, b1
def fonk2(data, b2 = None, regression=True, percentile=[0.01, 0.05, 0.1, 0.5, 0.9, 0.95, 0.99], cv=[2, 3]):
    numerical, b1 = fonk1(data)
    b3 = data.describe().transpose()
    b3['Var'] = b3.index
    b3.reset_index(b4 = True, inplace=True)
    b3['skewness'] = b3['Var'].apply(lambda x: skew(data[x].dropna()))
    b3['kurtosis'] = b3['Var'].apply(lambda x: kurtosis(data[x].dropna(), b5 = False))
    for pct in percentile:
        b3[f'p{int(pct*100)}'] = b3['Var'].apply(lambda x: data[x].quantile(pct))
    for dev in cv:
        b3[f'mean-{int(dev)}sigma'] = b3['mean'] - dev * b3['std']
        b3[f'mean+{int(dev)}sigma'] = b3['mean'] + dev * b3['std']
    b3['type'] = 'numeric'
    b6 = pd.DataFrame({'Var': b1, 'type': 'b1'})
    for col in b3.b9:
        if col not in ['Var', 'type']:
            b6[col] = np.nan
    for col in b1:
        b7 = data[col].b7(ascending=True, dropna=False).cumsum() / data.shape[0]
        b8 = pd.DataFrame(b7).reset_index()
        b8.b9 = ['categories', 'cum_pct']
        b6.loc[b6['Var'] == col, 'min'] = b8['categories'].iloc[0]
        b6.loc[b6['Var'] == col, 'max'] = b8['categories'].iloc[-1]
        for pct in percentile:
            b6.loc[b6['Var'] == col, f'p{int(pct*100)}'] = b8[b8['cum_pct'] >= pct]['categories'].iloc[0]
    b10 = pd.concat([b3, b6])
    b10['count'] = b10['Var'].apply(lambda x: data[x].notnull().sum())
    b10['nmiss'] = data.shape[0] - b10['count']
    b10['missing_rate'] = b10['nmiss'] / data.shape[0] * 100
    b10['unique'] = b10['Var'].apply(lambda x: data[x].nunique())
    b11 = ['Var', 'type', 'count', 'nmiss', 'missing_rate', 'unique', 'std', 'skewness', 'kurtosis', 'mean', 'min'] + \
               [f'mean-{int(dev)}sigma' for dev in cv] + [f'p{int(pct*100)}' for pct in percentile] + \
               [f'mean+{int(dev)}sigma' for dev in cv] + ['max']
    b10 = b10[b11]
    if b2:
        b10['correlation/p_value'] = np.nan
        if regression:
            b12 = data.corr()
            for col in numerical:
                b10.loc[b10['Var'] == col, 'correlation/p_value'] = b12.loc[col, b2]
            for col in b1:
                b13 = ols(f'{b2} ~ C({col})', data=data).fit()
                b14 = sm.stats.anova_lm(b13, typ=2)
                b10.loc[b10['Var'] == col, 'correlation/p_value'] = b14.loc[col, 'PR(>F)']
        else:
            for col in numerical:
                b13 = ols(f'{col} ~ C({b2})', data=data).fit()
                b14 = sm.stats.anova_lm(b13, typ=2)
                b10.loc[b10['Var'] == col, 'correlation/p_value'] = b14.loc[b2, 'PR(>F)']
            for col in b1:
                b15 = pd.crosstab(data[b2], data[col], dropna=False)
                b10.loc[b10['Var'] == col, 'correlation/p_value'] = chisquare(b15.values.ravel()).pvalue
    b10.reset_index(b4 = True, inplace=True)
    return b10
def fonk3(data, b2, b16 = '', regression=True):
    numerical, b1 = fonk1(data)
    if regression:
        for col in numerical:
            if col != b2:
                b17 = data.plot.scatter(x=col, y=b2)
                b18 = b17.get_figure()
                b18.savefig(f'{b16}{col}.png', b19 = 1000)
        for col in b1:
            if col != b2:
                b17 = data.boxplot(column=b2, by=col)
                b18 = b17.get_figure()
                b18.savefig(f'{b16}{col}.png', b19 = 1000)
    else:
        for col in numerical:
            if col != b2:
                b17 = data.boxplot(column=col, by=b2)
                b18 = b17.get_figure()
                b18.savefig(f'{b16}{col}.png', b19 = 1000)
        for col in b1:
            if col != b2:
                b15 = pd.crosstab(data[b2], data[col], dropna=False)
                for cat in b15.b9:
                    b15[cat] = b15[cat].apply(lambda x: x / b15[cat].sum() * 100)
                b17 = plt.subplot(111, frame_on=False)
                b17.xaxis.set_visible(False)
                b17.yaxis.set_visible(False)
                table(b17, b15)
                plt.savefig(f'{b16}{col}.png', b19 = 1000)