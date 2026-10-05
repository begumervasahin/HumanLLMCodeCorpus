import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis, chisquare
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
def fonk1(df):
    b1 = []
    b2 = []
    for col in df.b11:
        if df[col].dtype in ['int64', 'float64', 'int32', 'float32']:
            b1.append(col)
        else:
            b2.append(col)
    return b1, b2
def fonk2(data):
    b3 = data.describe().transpose()
    b3['Var'] = b3.index
    b3.reset_index(b4 = True)
    b3.drop('count', b5 = 1, b4=True)
    b3['skewness'] = b3['Var'].apply(lambda x: skew(np.array(data.loc[data[x].notnull(), x])))
    b3['kurtosis'] = b3['Var'].apply(
        lambda x: kurtosis(np.array(data.loc[data[x].notnull(), x]), b6 = False)))
    return b3
def fonk3(data, percentile):
    b7 = {}
    for pct in percentile:
        b7['p' + str(int(pct * 100))] = data.quantile(pct)
    return b7
def fonk4(data, cv):
    b7 = {}
    for dev in cv:
        b7['mean-' + str(int(dev)) + 'sigma'] = data['mean'] - dev * data['std']
        b7['mean+' + str(int(dev)) + 'sigma'] = data['mean'] + dev * data['std']
    return b7
def fonk5(data, b2, percentile):
    b8 = pd.DataFrame()
    b8['Var'] = np.array(b2)
    b8['type'] = 'b2'
    for col in b2:
        b9 = data[col].value_counts(ascending=True, dropna=False).cumsum() / data.shape[0]
        b10 = pd.DataFrame(b9)
        b10.reset_index(b4 = True)
        b10.b11 = ['categories', 'cum_pct']
        b8.loc[b8['Var'] == col, 'min'] = list(b10['categories'])[0]
        b8.loc[b8['Var'] == col, 'max'] = list(b10['categories'])[-1]
        for pct in percentile:
            b8.loc[b8['Var'] == col, 'p' + str(int(pct * 100))] = \
                list(b10.loc[b10['cum_pct'] >= pct, 'categories'])[0]
        del b9
        del b10
    return b8
def fonk6(data, b13):
    b13['count'] = b13['Var'].apply(lambda x: data[data[x].notnull()].shape[0])
    b13['nmiss'] = data.shape[0] - b13['count']
    b13['missing_rate'] = np.array(b13['nmiss']).astype('float') / data.shape[0] * 100
    return b13
def fonk7(data, b12 = None, regression=True, percentile=[.01, .05, .1, .5, .9, .95, .99], cv=[2, 3]):
    b1, b2 = fonk1(data)
    b3 = fonk2(data)
    b3['type'] = 'numeric'
    b8 = fonk5(data, b2, percentile)
    b13 = pd.concat([b3, b8])
    b13 = fonk6(data, b13)
    if b12:
        b13['correlation/p_value'] = np.nan
        if regression:
            b14 = data.corr()
            for col in b1:
                b13.loc[b13['Var'] == col, 'correlation/p_value'] = b14.loc[col, b12]
            for col in b2:
                b15 = ols(b12 + ' ~ ' + col, data=data).fit()
                b16 = sm.stats.anova_lm(b15, type=2)
                b13.loc[b13['Var'] == col, 'correlation/p_value'] = b16.loc[col, 'PR(>F)']
        else:
            for col in b1:
                b15 = ols(col + ' ~ ' + b12, data=data).fit()
                b16 = sm.stats.anova_lm(b15, type=2)
                b13.loc[b13['Var'] == col, 'correlation/p_value'] = b16.loc[b12, 'PR(>F)']
            for col in b2:
                b17 = pd.crosstab(data[b12], data[col], dropna=False)
                b13.loc[b13['Var'] == col, 'correlation/p_value'] = chisquare(
                    np.reshape(np.array(b17), np.product(b17.shape))).pvalue
    b13.reset_index(b4 = True, drop=True)
    return b13
def fonk8(data, b12, b18 = '', regression=True):
    b1, b2 = fonk1(data)
    if regression:
        for col in b1:
            if col != b12:
                b19 = data.plot(col, b12)
                b20 = b19.get_figure()
                b20.savefig(b18 + col + '.png', b21 = 1000)
                plt.close(b20)
        for col in b2:
            if col != b12:
                b19 = data.boxplot(b12, by=col)
                b20 = b19.get_figure()
                b20.savefig(b18 + col + '.png', b21 = 1000)
                plt.close(b20)
    else:
        for col in b1:
            if col != b12:
                b19 = data.boxplot(col, by=b12)
                b20 = b19.get_figure()
                b20.savefig(b18 + col + '.png', b21 = 1000)
                plt.close(b20)
        for col in b2:
            if col != b12:
                b17 = pd.crosstab(data[b12], data[col], dropna=False)
                for cat in b17.b11:
                    b17[cat] = b17[cat].apply(lambda x: x / b17[cat].sum() * 100)
                b19 = plt.subplot(111, frame_on=False)
                b19.xaxis.set_visible(False)
                b19.yaxis.set_visible(False)
                table(b19, b17)
                plt.savefig(b18 + col + '.png', b21 = 1000)
                plt.close()
