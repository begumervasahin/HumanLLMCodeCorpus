import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge, LinearRegression
from sklearn.ensemble import BaggingRegressor, GradientBoostingRegressor
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
def fonk1(company_name):
    b1 = pd.read_csv('data_files/WIKI-'+company_name+'.csv')
    b1['Date'] = pd.to_datetime(b1['Date'])
    b1.set_index('Date', b2 = True)
    b1 = b1[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Volume', 'Adj. Close']]
    b1['HL_PCT'] = (b1['Adj. High'] - b1['Adj. Low']) / b1['Adj. Low'] * 100.0
    b1['PCT_change'] = (b1['Adj. Close'] - b1['Adj. Open']) / b1['Adj. Open'] * 100.0
    x1, b3 = fonk2(b1['Adj. Open'])
    x2, b4 = fonk2(b1['Adj. High'])
    x3, b4 = fonk2(b1['Adj. Low'])
    x4, b4 = fonk2(b1['Adj. Volume'])
    x6, b4 = fonk2(b1['HL_PCT'])
    x7, b4 = fonk2(b1['PCT_change'])
    b5 = {
        'Adj. Open': x1,
        'Adj. High': x2,
        'Adj. Low': x3,
        'Adj. Volume': x4,
        'HL_PCT': x6,
        'PCT_change': x7
    }
    b6 = pd.DataFrame(b5)
    b7 = np.array(b1['Adj. Close'])
    b8 = b7[:b3]
    b9 = b7[b3:]
    b10 = b6[:b3]
    b11 = b6[b3:]
    b12 = {
        'Ridge': Ridge(),
        'Linear Regression': LinearRegression(),
        'Bagging Regressor': BaggingRegressor(),
        'Gradient Boosting Regressor': GradientBoostingRegressor()
    }
    for name, clf in b12.items():
        print("Fitting", name)
        clf.fit(b10, b8)
        b13 = clf.predict(b11)
        b14 = clf.score(b11, b9)
        print(name + ":", "Confidence: %.3f%%" % (b14 * 100.0))
        plt.plot(b13, b15 = 'Predicted')
        plt.plot(b9, b15 = 'Actual')
        plt.legend()
        plt.xlabel('Time')
        plt.ylabel('Price')
        plt.savefig('fea/'+str(company_name)+'b4'+name+'.png', b16 = 200, bbox_inches='tight')
        plt.clf()
    print("END")
def fonk2(sr):
    pass
fonk1('AAPL')