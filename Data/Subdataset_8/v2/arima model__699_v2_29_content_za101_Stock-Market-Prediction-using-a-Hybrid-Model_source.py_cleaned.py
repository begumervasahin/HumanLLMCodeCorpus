import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge, LinearRegression
from sklearn.ensemble import BaggingRegressor, GradientBoostingRegressor
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
def load_data(company_name):
    df = pd.read_csv('data_files/WIKI-' + company_name + '.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    return df
def preprocess_data(df):
    df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Low'] * 100.0
    df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
    return df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Volume', 'Adj. Close', 'HL_PCT', 'PCT_change']]
def split_data(data, train_size):
    train_data = data[:train_size]
    test_data = data[train_size:]
    return train_data, test_data
def train_models(x_train, y_train, x_test, y_test):
    models = {
        'Ridge': Ridge(),
        'Linear Regression': LinearRegression(),
        'Bagging Regressor': BaggingRegressor(),
        'Gradient Boosting Regressor': GradientBoostingRegressor()
    }
    for name, clf in models.items():
        print("Fitting", name)
        clf.fit(x_train, y_train)
        predicted = clf.predict(x_test)
        confidence = clf.score(x_test, y_test)
        print(name + ":", "Confidence: %.3f%%" % (confidence * 100.0))
        plt.plot(predicted, label='Predicted')
        plt.plot(y_test, label='Actual')
        plt.legend()
        plt.xlabel('Time')
        plt.ylabel('Price')
        plt.savefig('fea/' + str(company_name) + '_' + name + '.png', dpi=200, bbox_inches='tight')
        plt.clf()
    print("END")
def timeseries(company_name):
    df = load_data(company_name)
    df = preprocess_data(df)
    x, train_size = timer(df['Adj. Open'])
    data = {
        'Adj. Open': x[0],
        'Adj. High': x[1],
        'Adj. Low': x[2],
        'Adj. Volume': x[3],
        'HL_PCT': x[4],
        'PCT_change': x[5]
    }
    df_test = pd.DataFrame(data)
    y = np.array(df['Adj. Close'])
    y_train = y[:train_size]
    y_test = y[train_size:]
    x_train, x_test = split_data(df_test, train_size)
    train_models(x_train, y_train, x_test, y_test)
def timer(sr):
    pass
timeseries('AAPL')