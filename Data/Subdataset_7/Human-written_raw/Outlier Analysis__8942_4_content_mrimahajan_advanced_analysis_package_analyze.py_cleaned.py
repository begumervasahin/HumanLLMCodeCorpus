import pandas as pd
import numpy as np
from scipy.stats import skew,kurtosis
from scipy.special import cbrt
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy.stats import chisquare
from matplotlib import pyplot as plt
from pandas.tools.plotting import table
def fonk1(df):
    	numerical,b1 = [],[]
    	for col in df.b10:
    	    if 'int' in str(df[col].dtypes) or 'float' in str(df[col].dtypes):
    	        numerical.append(col)
    	    else:
    	        b1.append(col)
    	return numerical,b1
def fonk2(data,b2 = None,b13=True,percentile=[.01,.05,.1,.5,.9,.95,.99],cv=[2,3]):
    numerical,b1 = fonk1(data)
    b3 = data.describe().transpose()
    b3['Var'] = b3.index
    b3.reset_index(b4 = True)
    b3.drop('count',b5 = 1,b4=True)
    b3['skewness'] = b3['Var'].apply(lambda x: skew(np.array(data.loc[data[x].notnull(),x])))
    b3['kurtosis'] = b3['Var'].apply(lambda x: kurtosis(np.array(data.loc[data[x].notnull(),x]),b6 = False))
    for pct in percentile:
        b3['p'+str(int(pct*100))] = b3['Var'].apply(lambda x: data[x].quantile(pct))
    for dev in cv:
        b3['mean-'+str(int(dev))+'sigma'] = b3['mean'] - dev*b3['std']
        b3['mean+'+str(int(dev))+'sigma'] = b3['mean'] + dev*b3['std']
    b3['type']='numeric'
    b7 = pd.DataFrame()
    b7['Var']=np.array(b1)
    b7['type']='b1'
    for col in [c for c in b3.b10 if c not in ['Var','type']]:
        b7[col]=np.nan
    for col in b1:
        b8 = data[col].value_counts(ascending=True,dropna=False).cumsum()/data.shape[0]
        b9 = pd.DataFrame(b8)
        b9.reset_index(b4 = True)
        b9.b10 = ['categories','cum_pct']
        b7.loc[b7['Var']==col,'min'] = list(b9['categories'])[0]
        b7.loc[b7['Var']==col,'max'] = list(b9['categories'])[-1]
        for pct in percentile:
            b7.loc[b7['Var']==col,'p'+str(int(pct*100))] = list(b9.loc[b9['cum_pct']>= pct,'categories'])[0]
        del b8
        del b9
    b7 = b7[b3.b10]
    b11 = pd.concat([b3,b7])
    del b3
    del b7
    b11['count'] = b11['Var'].apply(lambda x: data[data[x].notnull()].shape[0])
    b11['nmiss'] = data.shape[0]-b11['count']
    b11['missing_rate'] = np.array(b11['nmiss']).astype('float')/data.shape[0] * 100
    b11['unique'] = b11['Var'].apply(lambda x: len(data[x].value_counts().index.tolist()))
    b12 = ['Var','type','count','nmiss','missing_rate','unique','std','skewness','kurtosis','mean','min'] + \
    ['mean-'+str(int(dev))+'sigma' for dev in cv] + ['p'+str(int(pct*100)) for pct in percentile] + \
    ['mean+'+str(int(dev))+'sigma' for dev in cv] + ['max']
    b11 = b11[b12]
    if b2:
        b11['correlation/p_value'] = np.nan
        if b13 = =True:
            b14 = data.corr()
            for col in numerical:
                b11.loc[b11['Var']==col,'correlation/p_value'] = b14.loc[col,b2]
            for col in b1:
                b15 = ols(b2+' ~ '+ col,data=data).fit()
                b16 = sm.stats.anova_lm(b15,type=2)
                b11.loc[b11['Var']==col,'correlation/p_value'] = b16.loc[col,'PR(>F)']
        else:
            for col in numerical:
                b15 = ols(col+' ~ '+ b2,data=data).fit()
                b16 = sm.stats.anova_lm(b15,type=2)
                b11.loc[b11['Var']==col,'correlation/p_value'] = b16.loc[b2,'PR(>F)']
            for col in b1:
                b17 = pd.crosstab(data[b2],data[col],dropna=False)
                b11.loc[b11['Var']==col,'correlation/p_value'] = chisquare(np.reshape(np.array(b17),np.product(b17.shape))).pvalue
    b11.reset_index(b4 = True)
    b11.drop('index',b5 = 1,b4=True)
    return b11
def fonk3(data,b2,b18 = '',b13=True):
    numerical,b1 = fonk1(data)
    if b13:
        for col in numerical:
            if col != b2:
                b19 = data.plot(col,b2)
                b20 = b19.get_figure()
                b20.savefig(b18+col+'.png',b21 = 1000)
        for col in b1:
            if col != b2:
                b19 = data.boxplot(b2,by=col)
                b20 = b19.get_figure()
                b20.savefig(b18+col+'.png',b21 = 1000)
    else:
        for col in numerical:
            if col != b2:
                b19 = data.boxplot(col,by=b2)
                b20 = b19.get_figure()
                b20.savefig(b18+col+'.png',b21 = 1000)
        for col in b1:
            if col != b2:
                b17 = pd.crosstab(data[b2],data[col],dropna=False)
                for cat in b17.b10:
                    b17[cat] = b17[cat].apply(lambda x: x/b17[cat].sum()*100)
                b19 = plt.subplot(111, frame_on=False)
                b19.xaxis.set_visible(False)
                b19.yaxis.set_visible(False)
                table(b19, b17)
                plt.savefig(b18+col+'.png',b21 = 1000)