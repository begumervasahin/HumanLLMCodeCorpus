import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import BaggingRegressor, GradientBoostingRegressor
from statsmodels.tsa.arima_model import ARIMA
def fonk1(sr):
    b1 = sr.values.astype('float32')
    b2 = int(len(b1) * 0.80)
    train, b3 = b1[:b2], b1[b2:]
    b4 = [x for x in train]
    b5 = []
    a1 = 1
    for i in range(len(b3)):
        b6 = fonk2(b4, a1)
        b7 = ARIMA(b6, order=(2, 1, 1))
        b8 = b7.fit(trend='nc', disp=0)
        b9 = b8.forecast()[0]
        b9 = fonk3(b4, b9, a1)
        b5.append(b9)
        b10 = float(b3[i])
        b4.append(b10)
    return b5, b2
def fonk2(dataset, b11 = 1):
    b6 = []
    for i in range(b11, len(dataset)):
        b12 = dataset[i] - dataset[i - b11]
        b6.append(b12)
    return b6
def fonk3(b4, b9, b11 = 1):
    return b9 + b4[-b11]
def fonk4(company_name):
    b13 = pd.read_csv(f'data_files/WIKI-{company_name}.csv')
    b13['Date'] = pd.to_datetime(b13['Date'])
    b13.set_index('Date', b14 = True)
    b13 = b13[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Volume', 'Adj. Close']]
    b13['HL_PCT'] = (b13['Adj. High'] - b13['Adj. Low']) / b13['Adj. Low'] * 100.0
    b13['PCT_change'] = (b13['Adj. Close'] - b13['Adj. Open']) / b13['Adj. Open'] * 100.0
    b15 = {}
    for column in ['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Volume', 'HL_PCT', 'PCT_change']:
        b5, b2 = fonk1(b13[column])
        b15[column] = b5
    b16 = pd.DataFrame(b15)
    b17 = b13['Adj. Close'].values
    b18 = b17[:b2]
    b19 = b17[b2:]
    b20 = b13.drop(columns=['Adj. Close'])
    b21 = b20.values[:b2]
    b22 = [
        ('Ridge', Ridge(b23 = 1.0)),
        ('LinearRegressor', LinearRegression()),
        ('Bagging', BaggingRegressor(b24 = None, n_estimators=10)),
        ('GradientBoostingRegressor', GradientBoostingRegressor())
    ]
    for name, b7 in b22:
        b7.fit(b21, b18)
        b25 = b7.predict(b16)
        b26 = b7.score(b16, b19)
        print(f"{name} Confidence: {b26 * 100:.3f}%")
        plt.plot(b25, b27 = 'Predicted')
        plt.plot(b19, b27 = 'Actual')
        plt.legend()
        plt.xlabel('Time')
        plt.ylabel('Price')
        plt.savefig(f'fea/{company_name}.png', b28 = 200, bbox_inches='tight')
        plt.clf()
fonk4('AAPL')