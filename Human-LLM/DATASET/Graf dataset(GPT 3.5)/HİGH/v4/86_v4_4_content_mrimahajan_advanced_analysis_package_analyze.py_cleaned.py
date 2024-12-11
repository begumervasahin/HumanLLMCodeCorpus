import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy.stats import skew, kurtosis, chisquare
from matplotlib import pyplot as plt
def fonk1(df):
    numerical, b1 = [], []
    for col in df.b11:
        if df[col].dtype in ['int64', 'float64']:
            numerical.append(col)
        else:
            b1.append(col)
    return numerical, b1
def fonk2(data, b2 = None, regression=True, percentile=[.01, .05, .1, .5, .9, .95, .99], cv=[2, 3]):
    numerical, b1 = fonk1(data)
    b3 = data.describe().transpose()
    b3['Var'] = b3.index
    b3.reset_index(b4 = True)
    b3.b18('count', b5 = 1, b4=True)
    b3['skewness'] = b3['Var'].apply(lambda b20: skew(np.array(data.loc[data[b20].notnull(), b20])))
    b3['kurtosis'] = b3['Var'].apply(lambda b20: kurtosis(np.array(data.loc[data[b20].notnull(), b20]), b6 = False))
    for pct in percentile:
        b3['p'+str(int(pct*100))] = b3['Var'].apply(lambda b20: data[b20].quantile(pct))
    for dev in cv:
        b3['mean-'+str(int(dev))+'sigma'] = b3['mean'] - dev * b3['std']
        b3['mean+'+str(int(dev))+'sigma'] = b3['mean'] + dev * b3['std']
    b3['type'] = 'numeric'
    b7 = pd.DataFrame(b11=b3.b11)
    b7['Var'] = b1
    b7['type'] = 'b1'
    for col in b1:
        b8 = data[col].value_counts(normalize=True, ascending=True, dropna=False).cumsum()
        min_val, b9 = b8.index[0], b8.index[-1]
        b10 = b8.reset_index()
        b10.b11 = ['categories', 'cum_pct']
        b7.loc[b7['Var'] == col, 'min'] = min_val
        b7.loc[b7['Var'] == col, 'max'] = b9
        for pct in percentile:
            b7.loc[b7['Var'] == col, 'p'+str(int(pct*100))] = b10.loc[b10['cum_pct'] >= pct, 'categories'].iloc[0]
    b12 = pd.concat([b3, b7])
    b12['count'] = b12['Var'].apply(lambda b20: data[b20].count())
    b12['nmiss'] = data.shape[0] - b12['count']
    b12['missing_rate'] = (b12['nmiss'] / data.shape[0]) * 100
    b12['unique'] = b12['Var'].apply(lambda b20: data[b20].nunique())
    b13 = ['Var', 'type', 'count', 'nmiss', 'missing_rate', 'unique', 'std', 'skewness', 'kurtosis', 'mean', 'min'] + \
               ['mean-'+str(int(dev))+'sigma' for dev in cv] + ['p'+str(int(pct*100)) for pct in percentile] + \
               ['mean+'+str(int(dev))+'sigma' for dev in cv] + ['max']
    b12 = b12[b13]
    if b2:
        b12['correlation/p_value'] = np.nan
        if regression:
            b14 = data.corr()
            for col in numerical:
                b12.loc[b12['Var'] == col, 'correlation/p_value'] = b14.loc[col, b2]
            for col in b1:
                b15 = ols(b17'{b2} ~ {col}', data=data).fit()
                b16 = sm.stats.anova_lm(b15, type=2)
                b12.loc[b12['Var'] == col, 'correlation/p_value'] = b16.loc[col, 'PR(>F)']
        else:
            for col in numerical:
                b15 = ols(b17'{col} ~ {b2}', data=data).fit()
                b16 = sm.stats.anova_lm(b15, type=2)
                b12.loc[b12['Var'] == col, 'correlation/p_value'] = b16.loc[b2, 'PR(>F)']
            for col in b1:
                b17 = pd.crosstab(data[b2], data[col], dropna=False)
                b12.loc[b12['Var'] == col, 'correlation/p_value'] = chisquare(np.reshape(np.array(b17), np.product(b17.shape))).pvalue
    b12.reset_index(b18 = True, b4=True)
    return b12
def fonk3(data, b2, b19 = '', regression=True):
    numerical, b1 = fonk1(data)
    if regression:
        for col in numerical:
            if col != b2:
                data.plot(b20 = col, y=b2)
                plt.savefig(b19 + col + '.png', b21 = 1000)
                plt.close()
        for col in b1:
            if col != b2:
                data.boxplot(b22 = b2, by=col)
                plt.savefig(b19 + col + '.png', b21 = 1000)
                plt.close()
    else:
        for col in numerical:
            if col != b2:
                data.boxplot(b22 = col, by=b2)
                plt.savefig(b19 + col + '.png', b21 = 1000)
                plt.close()
        for col in b1:
            if col != b2:
                b17 = pd.crosstab(data[b2], data[col], dropna=False)
                b17 = (b17 / b17.sum()) * 100
                b17.plot(b23 = 'bar', stacked=True)
                plt.savefig(b19 + col + '.png', b21 = 1000)
                plt.close()