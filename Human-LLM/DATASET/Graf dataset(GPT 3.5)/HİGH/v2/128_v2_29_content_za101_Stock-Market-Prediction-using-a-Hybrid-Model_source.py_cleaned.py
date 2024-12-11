import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge, LinearRegression
from sklearn.ensemble import BaggingRegressor, GradientBoostingRegressor
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
def fonk1(company_name):
    b1 = pd.read_csv('data_files/WIKI-' + company_name + '.csv')
    b1['Date'] = pd.to_datetime(b1['Date'])
    b1.set_index('Date', b2 = True)
    return b1
def fonk2(b1):
    b1['HL_PCT'] = (b1['Adj. High'] - b1['Adj. Low']) / b1['Adj. Low'] * 100.0
    b1['PCT_change'] = (b1['Adj. Close'] - b1['Adj. Open']) / b1['Adj. Open'] * 100.0
    return b1[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Volume', 'Adj. Close', 'HL_PCT', 'PCT_change']]
def fonk3(b11, b10):
    b3 = b11[:b10]
    b4 = b11[b10:]
    return b3, b4
def fonk4(x_train, b14, b16, b15):
    b5 = {
        'Ridge': Ridge(),
        'Linear Regression': LinearRegression(),
        'Bagging Regressor': BaggingRegressor(),
        'Gradient Boosting Regressor': GradientBoostingRegressor()
    }
    for name, clf in b5.items():
        print("Fitting", name)
        clf.fit(x_train, b14)
        b6 = clf.predict(b16)
        b7 = clf.score(b16, b15)
        print(name + ":", "Confidence: %.3f%%" % (b7 * 100.0))
        plt.plot(b6, b8 = 'Predicted')
        plt.plot(b15, b8 = 'Actual')
        plt.legend()
        plt.xlabel('Time')
        plt.ylabel('Price')
        plt.savefig('fea/' + str(company_name) + '_' + name + '.png', b9 = 200, bbox_inches='tight')
        plt.clf()
    print("END")
def fonk5(company_name):
    b1 = fonk1(company_name)
    b1 = fonk2(b1)
    x, b10 = fonk6(b1['Adj. Open'])
    b11 = {
        'Adj. Open': x[0],
        'Adj. High': x[1],
        'Adj. Low': x[2],
        'Adj. Volume': x[3],
        'HL_PCT': x[4],
        'PCT_change': x[5]
    }
    b12 = pd.DataFrame(b11)
    b13 = np.array(b1['Adj. Close'])
    b14 = b13[:b10]
    b15 = b13[b10:]
    x_train, b16 = fonk3(b12, b10)
    fonk4(x_train, b14, b16, b15)
def fonk6(sr):
    pass
fonk5('AAPL')