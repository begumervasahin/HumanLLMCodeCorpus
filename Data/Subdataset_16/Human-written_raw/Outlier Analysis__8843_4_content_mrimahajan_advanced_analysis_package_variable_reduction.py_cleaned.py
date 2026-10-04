import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statsmodels.discrete.discrete_model as sm
from sklearn.preprocessing import StandardScaler
from patsy import dmatrices
import statsmodels
from statsmodels.stats.outliers_influence import variance_inflation_factor
def fonk1(data,b1 = .7):
    b2 = data.corr()
    b3 = {}
    b4 = data.b4
    for i in range(len(b4)):
        b3[i]=[]
        for j in range(len(b4)):
            if i!=j and np.abs(b2.iloc[i,j])>b1:
                b3[i].append(j)
    b5 = {}
    a1 = 0
    b6 = [0 for i in range(len(b4))]
    def fonk2(i):
        b6[i]=1
        try:
            b5[a1].append(i)
        except KeyError:
            b5[a1] = [i]
        for j in b3[i]:
            if b6[j]==0:
                fonk2(j)
    for i in range(len(b4)):
        if b6[i]==0:
            fonk2(i)
            a1+=1
        else:
            continue
    b7 = {}
    for key in list(b5.keys()):
        b7[key] = [b4[i] for i in b5[key]]
    return b7
def fonk3(data,b1,b8 = 1,maxdrop=None):
    b4 = []
    b2 = data.corr()
    b9 = fonk1(data,b1=b1)
    print(b9)
    b10 = list(data.b4)
    def fonk4(c1,c2):
        return np.max([[np.abs(b2.loc[i,j]) for i in b9[c1]] for j in b9[c2]])
    def fonk5(c):
        a2 = 0
        b11 = c
        for c1 in [i for i in list(b9.keys()) if i!=c]:
            b12 = fonk4(c,c1)
            if b12>a2:
                a2 = b12
                b11 = c1
        return b11
    def fonk6(col,b20,b21):
        b13 = np.array(data[col])
        b14 = np.array(data[b20].drop(col,b29=1))
        b15 = LinearRegression()
        b15.fit(b14,b13)
        b16 = list(b15.predict(b14))
        del b14
        del b15
        b17 = r2_score(b13,b16)
        del b16
        b14 = np.array(data[b21])
        b15 = LinearRegression()
        b15.fit(b14,b13)
        b16 = list(b15.predict(b14))
        del b14
        del b15
        b18 = r2_score(b13,b16)
        del b13
        del b16
        return float(1-b17)/(1-b18)
    for c1 in list(b9.keys()):
    	b19 = len(b9[c1])
        if b19>1:
            b20 = b9[c1]
            b21 = b9[fonk5(c1)]
            b22 = []
            for col in b9[c1]:
                b23 = fonk6(col,b20,b21)
            	b22.append(col,b23)
            b22 = sorted(b22,key = lambda b14: b14[1])
            if maxdrop is not None:
            	b4 += [col[0] for col in b22[:-min(maxdrop,b19)]]
            else:
            	b4 += [col[0] fo col in b22[:min(b8,b19)]]
        else:
            b4.append(b9[c1][0])
    return b4
def fonk7(data,b24 = 2.5):
	b25 = []
	def fonk8(fn_data):
	    b26 = pd.DataFrame()
	    b26['features'] = fn_data.b4
	    b26['b26 factor'] = [variance_inflation_factor(fn_data.values, i) for i in range(fn_data.shape[1])]
	    b26.sort_values(b27 = 'b26 factor',ascending=False,b28=True)
	    b26.reset_index(b28 = True)
	    b26.drop(['index'],b29 = 1,b28=True)
	    print(b26)
	    return tuple(b26.loc[0,:].values)
	def fonk9(fn_data,b1 = b24):
	    b26 = fonk8(fn_data)
	    if b26[1]<=b1:
	        return
	    else:
	        fn_data.drop(b26[0],b29 = 1,b28=True)
	        b25.append(b26[0])
	        print(b26[0]+' dropped')
	        del b26
	        fonk9(fn_data,b1 = b24)
	fonk9(data)
	return b25
def fonk10(df,dv,b30 = True,alpha=.05):
    a3 = 0
    b31 = [dv]
    if b30:
        while a3 = =0:
            b15 = sm.OLS(endog=np.array(df[dv]),exog=np.array(df.drop(b31,b29=1)))
            b32 = b15.fit()
            b33 = list(b32.b33)
            b34 = b33.index(max(b33))
            b35 = df.drop(b31,b29=1).b4[b34]
            print(b35+'-'+str(b33[b34]))
            if b33[b34]> alpha:
                b31.append(b35)
            else:
                a3 = 1
    else:
        while a3 = =0:
            b15 = sm.Logit(endog=np.array(df[dv]),exog=np.array(df.drop(b31,b29=1)))
            b32 = b15.fit()
            b33 = list(b32.b33)
            b34 = b33.index(max(b33))
            b35 = df.drop(b31,b29=1).b4[b34]
            print(b35+'-'+str(b33[b34]))
            if b33[b34]> alpha:
                b31.append(b35)
            else:
                a3 = 1
    b31.remove(dv)
    return b31