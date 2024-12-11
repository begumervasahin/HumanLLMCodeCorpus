import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge, LinearRegression
from sklearn.ensemble import BaggingRegressor, GradientBoostingRegressor
import matplotlib.pyplot as plt
def fonk1(company_name):
    b1 = pd.read_csv('data_files/WIKI-' + company_name + '.csv')
    b1['Date'] = pd.to_datetime(b1['Date'])
    b1.set_index('Date', b2 = True)
    b1['HL_PCT'] = (b1['Adj. High'] - b1['Adj. Low']) / b1['Adj. Low'] * 100.0
    b1['PCT_change'] = (b1['Adj. Close'] - b1['Adj. Open']) / b1['Adj. Open'] * 100.0
    return b1[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Volume', 'Adj. Close', 'HL_PCT', 'PCT_change']]
def fonk2(data, b8):
    return data[:b8], data[b8:]
def fonk3(x_train, y_train, b12, b11):
    b3 = {
        'Ridge': Ridge(),
        'Linear Regression': LinearRegression(),
        'Bagging Regressor': BaggingRegressor(),
        'Gradient Boosting Regressor': GradientBoostingRegressor()
    }
    for name, clf in b3.items():
        print(f"Fitting {name}")
        clf.fit(x_train, y_train)
        b4 = clf.predict(b12)
        b5 = clf.score(b12, b11)
        print(f"{name}: Confidence: {b5 * 100.0:.3f}%")
        plt.plot(b4, b6 = 'Predicted')
        plt.plot(b11, b6 = 'Actual')
        plt.legend()
        plt.xlabel('Time')
        plt.ylabel('Price')
        plt.savefig(f'fea/{company_name}_{name}.png', b7 = 200, bbox_inches='tight')
        plt.clf()
    print("END")
def fonk4(company_name):
    b1 = fonk1(company_name)
    x, b8 = fonk5(b1['Adj. Open'])
    b9 = pd.DataFrame({
        'Adj. Open': x[0],
        'Adj. High': x[1],
        'Adj. Low': x[2],
        'Adj. Volume': x[3],
        'HL_PCT': x[4],
        'PCT_change': x[5]
    })
    b10 = np.array(b1['Adj. Close'])
    y_train, b11 = b10[:b8], b10[b8:]
    x_train, b12 = fonk2(b9, b8)
    fonk3(x_train, y_train, b12, b11)
def fonk5(sr):
    pass
fonk4('AAPL')