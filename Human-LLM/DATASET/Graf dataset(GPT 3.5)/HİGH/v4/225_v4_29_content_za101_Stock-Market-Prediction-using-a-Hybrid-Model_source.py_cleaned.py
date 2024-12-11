import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import BaggingRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima_model import ARIMA
def fonk1(company_name):
    b1 = pd.read_csv('data_files/WIKI-' + company_name + '.csv')
    b1['Date'] = pd.to_datetime(b1['Date'])
    b1.set_index('Date', b2 = True)
    b1 = b1[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Volume', 'Adj. Close']]
    b1['HL_PCT'] = (b1['Adj. High'] - b1['Adj. Low']) / b1['Adj. Low'] * 100.0
    b1['PCT_change'] = (b1['Adj. Close'] - b1['Adj. Open']) / b1['Adj. Open'] * 100.0
    b3 = b1['Adj. Open']
    b4 = b1['Adj. High']
    b5 = b1['Adj. Low']
    b6 = b1['Adj. Volume']
    b7 = b1['Adj. Close']
    b8 = b1['HL_PCT']
    b9 = b1['PCT_change']
    x1, b10 = fonk2(b3)
    x2, b11 = fonk2(b4)
    x3, b11 = fonk2(b5)
    x4, b11 = fonk2(b6)
    x6, b11 = fonk2(b8)
    x7, b11 = fonk2(b9)
    b12 = {
        'Adj. Open': x1,
        'Adj. High': x2,
        'Adj. Low': x3,
        'Adj. Volume': x4,
        'HL_PCT': x6,
        'PCT_change': x7
    }
    b13 = pd.DataFrame(b12)
    b14 = np.array(b1['Adj. Close'])
    b15 = b14[:b10]
    b16 = b14[b10:]
    b17 = b1.drop(columns=['Adj. Close'])
    b18 = np.array(b17[:b10])
    b19 = Ridge(alpha=1.0)
    b20 = LinearRegression()
    b21 = BaggingRegressor(base_estimator=None, n_estimators=10)
    b22 = GradientBoostingRegressor()
    b23 = [('Ridge', b19), ('LinearRegressor', b20),
              ('Bagging', b21), ('GradientBoostingRegressor', b22)]
    for name, b33 in b23:
        b33.fit(b18, b15)
        b24 = b33.predict(b13)
        b25 = b33.score(b13, b16)
        print(f"{name} Confidence: {b25 * 100:.3f}%")
        plt.plot(b24, b26 = 'Predicted')
        plt.plot(b16, b26 = 'Actual')
        plt.legend()
        plt.xlabel('Time')
        plt.ylabel('Price')
        plt.savefig(f'fea/{company_name}.png', b27 = 200, bbox_inches='tight')
        plt.clf()
def fonk2(sr):
    b28 = sr.values.astype('float32')
    b10 = int(len(b28) * 0.80)
    train, b29 = b28[:b10], b28[b10:]
    b30 = [x for x in train]
    b31 = []
    a1 = 1
    for i in range(len(b29)):
        b32 = fonk3(b30, a1)
        b33 = ARIMA(b32, order=(2, 1, 1))
        b34 = b33.fit(trend='nc', disp=0)
        b35 = b34.forecast()[0]
        b35 = fonk4(b30, b35, a1)
        b31.append(b35)
        b36 = float(b29[i])
        b30.append(b36)
    return b31, b10
def fonk3(dataset, b37 = 1):
    b32 = []
    for i in range(b37, len(dataset)):
        b38 = dataset[i] - dataset[i - b37]
        b32.append(b38)
    return b32
def fonk4(b30, b35, b37 = 1):
    return b35 + b30[-b37]
fonk1('AAPL')