import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import BaggingRegressor, GradientBoostingRegressor
from statsmodels.tsa.arima_model import ARIMA
def preprocess_time_series(sr):
    X = sr.values.astype('float32')
    train_size = int(len(X) * 0.80)
    train, test = X[:train_size], X[train_size:]
    history = [x for x in train]
    predictions = []
    months_in_year = 1
    for i in range(len(test)):
        diff = difference(history, months_in_year)
        model = ARIMA(diff, order=(2, 1, 1))
        model_fit = model.fit(trend='nc', disp=0)
        yhat = model_fit.forecast()[0]
        yhat = inverse_difference(history, yhat, months_in_year)
        predictions.append(yhat)
        obs = float(test[i])
        history.append(obs)
    return predictions, train_size
def difference(dataset, interval=1):
    diff = []
    for i in range(interval, len(dataset)):
        value = dataset[i] - dataset[i - interval]
        diff.append(value)
    return diff
def inverse_difference(history, yhat, interval=1):
    return yhat + history[-interval]
def analyze_time_series(company_name):
    df = pd.read_csv(f'data_files/WIKI-{company_name}.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Volume', 'Adj. Close']]
    df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Low'] * 100.0
    df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
    time_series_data = {}
    for column in ['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Volume', 'HL_PCT', 'PCT_change']:
        predictions, train_size = preprocess_time_series(df[column])
        time_series_data[column] = predictions
    df_test = pd.DataFrame(time_series_data)
    y = df['Adj. Close'].values
    y_train = y[:train_size]
    y_test = y[train_size:]
    df_train = df.drop(columns=['Adj. Close'])
    x_train = df_train.values[:train_size]
    models = [
        ('Ridge', Ridge(alpha=1.0)),
        ('LinearRegressor', LinearRegression()),
        ('Bagging', BaggingRegressor(base_estimator=None, n_estimators=10)),
        ('GradientBoostingRegressor', GradientBoostingRegressor())
    ]
    for name, model in models:
        model.fit(x_train, y_train)
        predicted = model.predict(df_test)
        confidence = model.score(df_test, y_test)
        print(f"{name} Confidence: {confidence * 100:.3f}%")
        plt.plot(predicted, label='Predicted')
        plt.plot(y_test, label='Actual')
        plt.legend()
        plt.xlabel('Time')
        plt.ylabel('Price')
        plt.savefig(f'fea/{company_name}.png', dpi=200, bbox_inches='tight')
        plt.clf()
analyze_time_series('AAPL')