import pandas as pd
import numpy as np
from scipy.stats import skew,kurtosis
from scipy.special import cbrt
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy.stats import chisquare
from matplotlib import pyplot as plt
from pandas.tools.plotting import table
import os
import pickle
from sklearn.linear_model import LinearRegression
def fonk1(data,s,b1 = .5,b4=True,b7=True):
    p1,p5,p95,b2 = data[s].quantile(.01),data[s].quantile(.05),data[s].quantile(.95),data[s].quantile(.99)
    if b1<=0 or b1>=1:
        raise ValueError('b1 should be between 0 and 1')
    data.sort_values(s,b3 = True,inplace=True)
    if b4 = =True:
        def fonk2(array,b1):
            b5 = array[0]
            a1 = 1
            while a1 < len(array):
                b5 = b1*array[a1]+(1-b1)*b5
                a1+=1
            return b5
        b6 = fonk2(list(np.array(data.loc[(data[s]>=p95) & (data[s]<=b2) & (data[s].notnull()),s])),b1)
        for a1 in data[(data[s]>b2) & (data[s].notnull())].index.tolist():
            data.loc[a1,s] = b1*data.loc[a1,s] + (1-b1)*b6
            b6 = data.loc[a1,s]
        if b7 = =True:
            def fonk3(array,b1):
                b5 = array[-1]
                a1 = len(array)-2
                while a1 > 0:
                    b5 = b1*array[a1+1]+(1-b1)*b5
                    a1-=1
                return b5
            b6 = fonk3(list(np.array(data.loc[(data[s]>=p1) & (data[s]<=p5) & (data[s].notnull()),s])),b1)
            for a1 in data[(data[s]<p1) & (data[s].notnull())].index.tolist()[::-1]:
                data.loc[a1,s] = b1*data[s].loc[a1,s] + (1-b1)*b6
                b6 = data.loc[a1,s]
def fonk4(data,s,a,b,b4 = True,b7=True):
    if b4 = =True:
        data.loc[(data[s]>a) & (data[s].notnull()),s] =a
    if b7 = =True:
        data.loc[(data[s]<b) & (data[s].notnull()),s] = b
def fonk5(data,s):
    b8 = []
    b9 = pd.DataFrame()
    b9['counts'] = data[s].value_counts(b10 = False)
    b9.sort_values(b11 = 'counts',b3=False,inplace=True)
    for category in b9.index.tolist()[:-1]:
        b8.append(category)
        data[s+'_dum_'+str(category)] = 0
        data.loc[data[s]==category,s+'_dum_'+str(category)]=1
    return b8
def fonk6(data,s):
    b9 = pd.DataFrame()
    b9['counts']=data[s].value_counts(b10 = False)
    b12 = b9.index.tolist()
    b13 = len(b12)
    b14 = len(str(int(bin(b13)[2:],10)))
    b15 = []
    for a1 in range(b13):
        b15.append(int(bin(a1)[2:],10))
    b16 = []
    for a1,cat in enumerate(b12):
        b16.append((cat,b15[a1]))
    for j in range(b14):
        data[s+'_dum_'+str(j)]=0
        for a1,cat in enumerate(b12):
            data.loc[data[s]==cat,s+'_dum_'+str(j)]=b15[a1]%10
            b15[a1]=b15[a1]
    return b16