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
    b3['Variable'] = b3.index
    b3.reset_index(b4 = True, b20=True)
    b3.b20('count', b5 = 1, b4=True)
    b3['skewness'] = b3['Variable'].apply(lambda x: skew(np.array(data.loc[data[x].notnull(), x])))
    b3['kurtosis'] = b3['Variable'].apply(
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
    b8['Variable'] = np.array(b2)
    b8['Type'] = 'Categorical'
    for col in b2:
        b9 = data[col].value_counts(ascending=True, dropna=False).cumsum() / data.shape[0]
        b10 = pd.DataFrame(b9)
        b10.reset_index(b4 = True)
        b10.b11 = ['Categories', 'Cumulative_Percentage']
        b8.loc[b8['Variable'] == col, 'Minimum'] = list(b10['Categories'])[0]
        b8.loc[b8['Variable'] == col, 'Maximum'] = list(b10['Categories'])[-1]
        for pct in percentile:
            b8.loc[b8['Variable'] == col, 'p' + str(int(pct * 100))] = \
                list(b10.loc[b10['Cumulative_Percentage'] >= pct, 'Categories'])[0]
        del b9
        del b10
    return b8
def fonk6(data, b15):
    b15['Count'] = b15['Variable'].apply(lambda x: data[x].count())
    b15['Missing_Values'] = data.shape[0] - b15['Count']
    b15['Missing_Rate'] = (b15['Missing_Values'] / data.shape[0]) * 100
    return b15
def fonk7(data, b12 = None, regression=True, percentile=[.01, .05, .1, .5, .9, .95, .99], cv=[2, 3]):
    b1, b2 = fonk1(data)
    b13 = fonk2(data)
    b13['Type'] = 'Numeric'
    b14 = fonk5(data, b2, percentile)
    b15 = pd.concat([b13, b14])
    b15 = fonk6(data, b15)
    if b12:
        b15['Correlation/P_Value'] = np.nan
        if regression:
            b16 = data.corr()
            for col in b1:
                b15.loc[b15['Variable'] == col, 'Correlation/P_Value'] = b16.loc[col, b12]
            for col in b2:
                b17 = ols(b12 + ' ~ ' + col, data=data).fit()
                b18 = sm.stats.anova_lm(b17, type=2)
                b15.loc[b15['Variable'] == col, 'Correlation/P_Value'] = b18.loc[col, 'PR(>F)']
        else:
            for col in b1:
                b17 = ols(col + ' ~ ' + b12, data=data).fit()
                b18 = sm.stats.anova_lm(b17, type=2)
                b15.loc[b15['Variable'] == col, 'Correlation/P_Value'] = b18.loc[b12, 'PR(>F)']
            for col in b2:
                b19 = pd.crosstab(data[b12], data[col], dropna=False)
                b15.loc[b15['Variable'] == col, 'Correlation/P_Value'] = chisquare(np.reshape(np.array(b19), np.product(b19.shape))).pvalue
    b15.reset_index(b20 = True, b4=True)
    return b15
def fonk8(data, b12, b21 = '', regression=True):
    b1, b2 = fonk1(data)
    if regression:
        for col in b1:
            if col != b12:
                b22 = data.plot(col, b12)
                b23 = b22.get_figure()
                b23.savefig(b21 + col + '.png', b24 = 1000)
                plt.close(b23)
        for col in b2:
            if col != b12:
                b22 = data.boxplot(b12, by=col)
                b23 = b22.get_figure()
                b23.savefig(b21 + col + '.png', b24 = 1000)
                plt.close(b23)
    else:
        for col in b1:
            if col != b12:
                b22 = data.boxplot(col, by=b12)
                b23 = b22.get_figure()
                b23.savefig(b21 + col + '.png', b24 = 1000)
                plt.close(b23)
        for col in b2:
            if col != b12:
                b19 = pd.crosstab(data[b12], data[col], dropna=False)
                for cat in b19.b11:
                    b19[cat] = b19[cat].apply(lambda x: x / b19[cat].sum() * 100)
                b22 = plt.subplot(111, frame_on=False)
                b22.xaxis.set_visible(False)
                b22.yaxis.set_visible(False)
                table(b22, b19)
                plt.savefig(b21 + col + '.png', b24 = 1000)
                plt.close()
