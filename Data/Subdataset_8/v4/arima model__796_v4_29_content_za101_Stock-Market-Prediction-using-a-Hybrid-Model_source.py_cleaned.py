import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import BaggingRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima_model import ARIMA
def analyze_time_series(company_name):
    df = pd.read_csv('data_files/WIKI-' + company_name + '.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Volume', 'Adj. Close']]
    df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Low'] * 100.0
    df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
    df_timeseries_open = df['Adj. Open']
    df_timeseries_high = df['Adj. High']
    df_timeseries_low = df['Adj. Low']
    df_timeseries_vol = df['Adj. Volume']
    df_timeseries_close = df['Adj. Close']
    df_timeseries_HL_PCT = df['HL_PCT']
    df_timeseries_PCT_change = df['PCT_change']
    x1, train_size = preprocess_time_series(df_timeseries_open)
    x2, _ = preprocess_time_series(df_timeseries_high)
    x3, _ = preprocess_time_series(df_timeseries_low)
    x4, _ = preprocess_time_series(df_timeseries_vol)
    x6, _ = preprocess_time_series(df_timeseries_HL_PCT)
    x7, _ = preprocess_time_series(df_timeseries_PCT_change)
    data = {
        'Adj. Open': x1,
        'Adj. High': x2,
        'Adj. Low': x3,
        'Adj. Volume': x4,
        'HL_PCT': x6,
        'PCT_change': x7
    }
    df_test = pd.DataFrame(data)
    y = np.array(df['Adj. Close'])
    y_train = y[:train_size]
    y_test = y[train_size:]
    df_train = df.drop(columns=['Adj. Close'])
    x_train = np.array(df_train[:train_size])
    ridge_model = Ridge(alpha=1.0)
    linear_reg_model = LinearRegression()
    bagging_model = BaggingRegressor(base_estimator=None, n_estimators=10)
    boosting_model = GradientBoostingRegressor()
    models = [('Ridge', ridge_model), ('LinearRegressor', linear_reg_model),
              ('Bagging', bagging_model), ('GradientBoostingRegressor', boosting_model)]
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
analyze_time_series('AAPL')