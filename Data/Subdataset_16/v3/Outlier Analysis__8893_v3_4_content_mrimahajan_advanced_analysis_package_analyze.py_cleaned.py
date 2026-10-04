import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis, chisquare
from statsmodels.formula.api import ols
import statsmodels.api as sm
from matplotlib import pyplot as plt
from pandas.plotting import table
def fonk1(df):
    b1 = [col for col in df.b10 if pd.api.types.is_numeric_dtype(df[col])]
    b2 = [col for col in df.b10 if not pd.api.types.is_numeric_dtype(df[col])]
    return b1, b2
def fonk2(data, b3 = None, regression=True, percentiles=[0.01, 0.05, 0.1, 0.5, 0.9, 0.95, 0.99], std_multipliers=[2, 3]):
    b1, b2 = fonk1(data)
    b4 = data.describe().transpose()
    b4['Var'] = b4.index
    b4.reset_index(b5 = True, inplace=True)
    b4['skewness'] = b4['Var'].apply(lambda x: skew(data[x].dropna()))
    b4['kurtosis'] = b4['Var'].apply(lambda x: kurtosis(data[x].dropna(), b6 = False))
    for pct in percentiles:
        b4[f'p{int(pct*100)}'] = b4['Var'].apply(lambda x: data[x].quantile(pct))
    for std_multiplier in std_multipliers:
        b4[f'mean-{std_multiplier}sigma'] = b4['mean'] - std_multiplier * b4['std']
        b4[f'mean+{std_multiplier}sigma'] = b4['mean'] + std_multiplier * b4['std']
    b4['type'] = 'numeric'
    b7 = pd.DataFrame({'Var': b2, 'type': 'categorical'})
    for col in b4.b10:
        if col not in ['Var', 'type']:
            b7[col] = np.nan
    for col in b2:
        b8 = data[col].b8(ascending=True, dropna=False).cumsum() / data.shape[0]
        b9 = pd.DataFrame(b8).reset_index()
        b9.b10 = ['categories', 'cum_pct']
        b7.loc[b7['Var'] == col, 'min'] = b9['categories'].iloc[0]
        b7.loc[b7['Var'] == col, 'max'] = b9['categories'].iloc[-1]
        for pct in percentiles:
            b11 = b9[b9['cum_pct'] >= pct]['categories'].iloc[0]
            b7.loc[b7['Var'] == col, f'p{int(pct*100)}'] = b11
    b12 = pd.concat([b4, b7])
    b12['count'] = b12['Var'].apply(lambda x: data[x].notnull().sum())
    b12['nmiss'] = data.shape[0] - b12['count']
    b12['missing_rate'] = b12['nmiss'] / data.shape[0] * 100
    b12['unique'] = b12['Var'].apply(lambda x: data[x].nunique())
    b13 = ['Var', 'type', 'count', 'nmiss', 'missing_rate', 'unique', 'std', 'skewness', 'kurtosis', 'mean', 'min'] + \
                   [f'mean-{std_multiplier}sigma' for std_multiplier in std_multipliers] + \
                   [f'p{int(pct*100)}' for pct in percentiles] + \
                   [f'mean+{std_multiplier}sigma' for std_multiplier in std_multipliers] + ['max']
    b12 = b12[b13]
    if b3:
        b12['correlation/p_value'] = np.nan
        if regression:
            b14 = data.corr()
            for col in b1:
                b12.loc[b12['Var'] == col, 'correlation/p_value'] = b14.loc[col, b3]
            for col in b2:
                b15 = ols(f'{b3} ~ C({col})', data=data).fit()
                b16 = sm.stats.anova_lm(b15, typ=2)
                b12.loc[b12['Var'] == col, 'correlation/p_value'] = b16.loc[col, 'PR(>F)']
        else:
            for col in b1:
                b15 = ols(f'{col} ~ C({b3})', data=data).fit()
                b16 = sm.stats.anova_lm(b15, typ=2)
                b12.loc[b12['Var'] == col, 'correlation/p_value'] = b16.loc[b3, 'PR(>F)']
            for col in b2:
                b17 = pd.crosstab(data[b3], data[col], dropna=False)
                b12.loc[b12['Var'] == col, 'correlation/p_value'] = chisquare(b17.values.ravel()).pvalue
    b12.reset_index(b5 = True, inplace=True)
    return b12
def fonk3(data, b3, b18 = '', regression=True):
    b1, b2 = fonk1(data)
    if regression:
        for col in b1:
            if col != b3:
                b19 = data.plot.scatter(x=col, y=b3)
                b20 = b19.get_figure()
                b20.savefig(f'{b18}{col}.png', b21 = 1000)
        for col in b2:
            if col != b3:
                b19 = data.boxplot(column=b3, by=col)
                b20 = b19.get_figure()
                b20.savefig(f'{b18}{col}.png', b21 = 1000)
    else:
        for col in b1:
            if col != b3:
                b19 = data.boxplot(column=col, by=b3)
                b20 = b19.get_figure()
                b20.savefig(f'{b18}{col}.png', b21 = 1000)
        for col in b2:
            if col != b3:
                b17 = pd.crosstab(data[b3], data[col], dropna=False)
                for cat in b17.b10:
                    b17[cat] = b17[cat].apply(lambda x: x / b17[cat].sum() * 100)
                b19 = plt.subplot(111, frame_on=False)
                b19.xaxis.set_visible(False)
                b19.yaxis.set_visible(False)
                table(b19, b17)
                plt.savefig(f'{b18}{col}.png', b21 = 1000)