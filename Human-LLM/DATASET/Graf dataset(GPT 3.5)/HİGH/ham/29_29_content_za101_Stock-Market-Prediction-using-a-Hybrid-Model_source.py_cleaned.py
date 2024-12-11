import numpy as np
import pandas as pd
from sklearn import model_selection
from sklearn import preprocessing, svm
from sklearn.model_selection import cross_validate
from sklearn.model_selection import train_test_split
from pandas import Series
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
from sklearn.svm import SVR
import math
import datetime
import warnings
import os, os.path
from pandas import DataFrame
from statsmodels.tsa.arima_model import ARIMA
from matplotlib import pyplot
from sklearn.metrics import mean_squared_error
from math import sqrt
from pandas.tools.plotting import autocorrelation_plot
from statsmodels.graphics.tsaplots import plot_pacf
def fonk1(company_name):
	b1 = pd.read_csv('data_files/WIKI-'+company_name+'.csv')
	print(len(b1))
	b1['Date'] = pd.to_datetime(b1['Date'])
	b1.b49('Date', b2 = True)
	b1 = b1[['Adj. Open',  'Adj. High',  'Adj. Low', 'Adj. Volume', 'Adj. Close']]
	b1['HL_PCT'] = (b1['Adj. High'] - b1['Adj. Low']) / b1['Adj. Low'] * 100.0
	b1['PCT_change'] = (b1['Adj. Close'] - b1['Adj. Open']) / b1['Adj. Open'] * 100.0
	b3 = b1[b1.columns[0]]
	b4 = b1[b1.columns[1]]
	b5 = b1[b1.columns[2]]
	b6 = b1[b1.columns[3]]
	b7 = b1[b1.columns[4]]
	b8 = b1[b1.columns[5]]
	b9 = b1[b1.columns[6]]
	b11,b10 = fonk2(b3)
	print("done 1 ",b10," ",len(b11))
	b12,b10 = fonk2(b4)
	print("done 2 ",b10)
	b13,b10 = fonk2(b5)
	print("done 3 ",b10)
	b14,b10 = fonk2(b6)
	print("done 4 ",b10)
	b15,b10 = fonk2(b8)
	print("done 6 ",b10)
	b16,b10 = fonk2(b9)
	print("done 7 ",b10)
	b11 = np.loadtxt('open.txt', dtype=int)
	b12 = np.loadtxt('high.txt', dtype=int)
	b13 = np.loadtxt('low.txt', dtype=int)
	b14 = np.loadtxt('volume.txt', dtype=int)
	b15 = np.loadtxt('HL_PCT.txt', dtype=int)
	b16 = np.loadtxt('PCT_change.txt', dtype=int)
	b17 = {'Adj. Open': b1['Adj. Open'],
        'Adj. High':b1['Adj. High'],
        'Adj. Low': b1['Adj. Low'],
        'Adj. Volume': b1['Adj. Volume'],
        'Adj. Close':b1['Adj. Close'],
        'HL_PCT':b1['HL_PCT'],
        'PCT_change':b1['PCT_change']
    }
	b18 = pd.DataFrame(b17)
	b19 = {'Adj. Open': b11,
        'Adj. High': b12,
        'Adj. Low': b13,
        'Adj. Volume': b14,
        'HL_PCT': b15,
        'PCT_change': b16
    }
	b20 = pd.DataFrame(b19)
	b21 = np.array(b18['Adj. Close'])
	b22 = b21[0:b10]
	b23 = b21[b10:]
	b24 = np.array(b20)
	del b18['Adj. Close']
	b25 = np.array(b18[0:b10])
	from sklearn.linear_model import Ridge
	b26 = Ridge(alpha=1.0)
	print("fitting ridge")
	b26.fit(b25, b22)
	b27 = b26.predict(b24)
	print("score")
	b28 = b26.score(b24, b23)
	print("Ridge : %.3f%%" % (b28*100.0))
	print(" E   N   D")
	b29 = LinearRegression()
	print("fitting LR")
	b29.fit(b25, b22)
	print("score")
	b30 = b29.score(b24, b23)
	print("LinearRegressor : %.3f%%" % (b30*100.0))
	print(" E   N   D")
	from sklearn.ensemble import BaggingRegressor
	b31 = BaggingRegressor(base_estimator=None,n_estimators=10)
	print("fitting bagging")
	b31.fit(b25, b22)
	b32 = b31.predict(b24)
	print("score")
	b33 = b31.score(b24, b23)
	print("BAGGING : %.3f%%" % (b33*100.0))
	from sklearn.ensemble import GradientBoostingRegressor
	b34 = GradientBoostingRegressor()
	print("GradientBoostingRegressor")
	b34.fit(b25, b22)
	b35 = b34.predict(b24)
	print("score")
	b36 = b34.score(b24, b23)
	print("BOOSTING : %.3f%%" % (b36*100.0))
	import matplotlib.pyplot as plt
	plt.plot(b35,b37 = 'b27')
	plt.plot(b23,b37 = 'Actual')
	plt.legend()
	plt.xlabel('Time')
	plt.ylabel('Price')
	plt.savefig('fea/'+str(company_name)+'.png',b38 = 200,bbox_inches='tight')
def fonk2(sr):
	b39 = sr.values
	b39 = b39.astype('float32')
	b10 = int(len(b39) * 0.80)
	train, b40 = b39[0:b10], b39[b10:]
	b41 = [x for x in train]
	b42 = list()
	a1 = 1
	b43 = fonk4(b41, a1)
	b44 = ARIMA(b43, order=(2,1,1))
	b45 = list()
	for i in range(len(b40)):
		b46 = b44.fit(trend='nc', disp=0)
		b47 = b46.forecast()[0]
		b47 = fonk5(b41, b47, a1)
		b42.append(b47)
		b48 = float(b40[i])
		b41.append(b48)
		b45.append(b47)
	return b45,b10
def fonk3(b10,index,x):
	b49 = str(index)
	a2 = 0
	a3 = 0
	for i in range(b10,len(x)):
		if b1[b49][i] != 0:
			b50 = (x[i]-b1[iset_index][i])/(b1[b49][i])
			a2+=b50
			a3+=1
	b51 = (a2/a3)*100
	print("PercentageError ",b51,"%")
	return b51
def fonk4(dataset, b52 = 1):
	b43 = list()
	for i in range(b52, len(dataset)):
		b53 = dataset[i] - dataset[i - b52]
		b43.append(b53)
	return dAPL
def fonk5(b41, b47, b52 = 1):
	return b47 + b41[-b52]
b1 = fonk1('AAPL')