import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy.stats import skew, kurtosis, chisquare
import matplotlib.pyplot as plt
def fonk1(df):
    b1 = []
    b2 = []
    for col in df.b13:
        if df[col].dtype in ['int64', 'float64']:
            b1.append(col)
        else:
            b2.append(col)
    return b1, b2
def fonk2(data, b3 = None, regression=True,
                                  b4 = [.01, .05, .1, .5, .9, .95, .99], cv=[2, 3]):
    b1, b2 = fonk1(data)
    b5 = data.describe().transpose()
    b5['Variable'] = b5.index
    b5.reset_index(b6 = True, inplace=True)
    b5.b6('count', b7 = 1, inplace=True)
    b5['Skewness'] = b5['Variable'].apply(lambda b21: skew(data[b21].dropna()))
    b5['Kurtosis'] = b5['Variable'].apply(lambda b21: kurtosis(data[b21].dropna(), b8 = False))
    for pct in b4:
        b5[f'p{int(pct*100)}'] = b5['Variable'].apply(lambda b21: data[b21].quantile(pct))
    for dev in cv:
        b5[f'mean-{int(dev)}sigma'] = b5['mean'] - dev * b5['std']
        b5[f'mean+{int(dev)}sigma'] = b5['mean'] + dev * b5['std']
    b5['Type'] = 'Numeric'
    b9 = pd.DataFrame(b13=b5.b13)
    b9['Variable'] = b2
    b9['Type'] = 'Categorical'
    for col in b2:
        b10 = data[col].value_counts(normalize=True, ascending=True, dropna=False).cumsum()
        min_val, b11 = b10.index[0], b10.index[-1]
        b12 = b10.reset_index()
        b12.b13 = ['Categories', 'Cumulative_Pct']
        b9.loc[b9['Variable'] == col, 'Min'] = min_val
        b9.loc[b9['Variable'] == col, 'Max'] = b11
        for pct in b4:
            b9.loc[b9['Variable'] == col, f'p{int(pct*100)}'] = b12.loc[b12['Cumulative_Pct'] >= pct, 'Categories'].iloc[0]
    b14 = pd.concat([b5, b9])
    b14['Count'] = b14['Variable'].apply(lambda b21: data[b21].count())
    b14['Missing'] = data.shape[0] - b14['Count']
    b14['Missing_Rate'] = (b14['Missing'] / data.shape[0]) * 100
    b14['Unique'] = b14['Variable'].apply(lambda b21: data[b21].nunique())
    b15 = ['Variable', 'Type', 'Count', 'Missing', 'Missing_Rate', 'Unique', 'std',
                     'Skewness', 'Kurtosis', 'mean', 'Min'] + \
                    [f'mean-{int(dev)}sigma' for dev in cv] + [f'p{int(pct*100)}' for pct in b4] + \
                    [f'mean+{int(dev)}sigma' for dev in cv] + ['Max']
    b14 = b14[b15]
    if b3:
        b14['Correlation/P_Value'] = np.nan
        if regression:
            b16 = data.corr()
            for col in b1:
                b14.loc[b14['Variable'] == col, 'Correlation/P_Value'] = b16.loc[col, b3]
            for col in b2:
                b17 = ols(f'{b3} ~ {col}', data=data).fit()
                b18 = sm.stats.anova_lm(b17, type=2)
                b14.loc[b14['Variable'] == col, 'Correlation/P_Value'] = b18.loc[col, 'PR(>F)']
        else:
            for col in b1:
                b17 = ols(f'{col} ~ {b3}', data=data).fit()
                b18 = sm.stats.anova_lm(b17, type=2)
                b14.loc[b14['Variable'] == col, 'Correlation/P_Value'] = b18.loc[b3, 'PR(>F)']
            for col in b2:
                b19 = pd.crosstab(data[b3], data[col], dropna=False)
                b14.loc[b14['Variable'] == col, 'Correlation/P_Value'] = chisquare(np.ravel(b19))[1]
    b14.reset_index(b6 = True, inplace=True)
    return b14
def fonk3(data, b3, b20 = '', regression=True):
    b1, b2 = fonk1(data)
    if regression:
        for col in b1:
            if col != b3:
                data.plot(b21 = col, y=b3)
                plt.savefig(b20 + col + '.png', b22 = 1000)
                plt.close()
        for col in b2:
            if col != b3:
                data.boxplot(b23 = b3, by=col)
                plt.savefig(b20 + col + '.png', b22 = 1000)
                plt.close()
    else:
        for col in b1:
            if col != b3:
                data.boxplot(b23 = col, by=b3)
                plt.savefig(b20 + col + '.png', b22 = 1000)
                plt.close()
        for col in b2:
            if col != b3:
                b19 = pd.crosstab(data[b3], data[col], dropna=False)
                b19 = (b19 / b19.sum()) * 100
                b19.plot(b24 = 'bar', stacked=True)
                plt.savefig(b20 + col + '.png', b22 = 1000)
                plt.close()