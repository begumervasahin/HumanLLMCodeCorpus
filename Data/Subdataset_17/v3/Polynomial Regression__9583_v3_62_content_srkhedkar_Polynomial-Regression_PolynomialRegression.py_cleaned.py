import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
def calculate_CAGR(first, last, periods):
    return ((last / first) ** (1 / periods) - 1) * 100
def load_data(file_path):
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df.index = (df.index - pd.to_datetime('1970-01-01')).days
    return df
def prepare_data(df):
    y = np.asarray(df['Close'])
    x = np.asarray(df.index.values)
    return x, y
def fit_polynomial_regression(x, y, degree=5):
    poly = PolynomialFeatures(degree)
    X_transform = poly.fit_transform(x.reshape(-1, 1))
    regression_model = LinearRegression()
    regression_model.fit(X_transform, y.reshape(-1, 1))
    return regression_model, poly
def predict_future_values(regression_model, poly, x, future_periods=3650):
    future_index = np.asarray(pd.RangeIndex(start=x[-1], stop=x[-1] + future_periods))
    X_extended_transform = poly.fit_transform(future_index.reshape(-1, 1))
    y_predict = regression_model.predict(X_extended_transform)
    return y_predict, future_index
def plot_results(x_dates, y_actual, y_learned, future_dates, y_predict):
    plt.figure(figsize=(16, 8))
    plt.plot(x_dates, y_actual, label='Close Price History')
    plt.plot(x_dates, y_learned, color='r', label='Mathematical Model')
    plt.plot(future_dates, y_predict, color='g', label='Future Predictions')
    plt.suptitle('Stock Market Predictions', fontsize=16)
    plt.legend()
    fig = plt.gcf()
    fig.canvas.manager.set_window_title('Stock Market Predictions')
    plt.show()
def main():
    file_path = 'D:\\python3\\data\\SensexHistoricalData.csv'
    df = load_data(file_path)
    x, y = prepare_data(df)
    regression_model, poly = fit_polynomial_regression(x, y)
    y_learned = regression_model.predict(poly.fit_transform(x.reshape(-1, 1)))
    y_predict, future_index = predict_future_values(regression_model, poly, x)
    print("Closing price at 2029 would be around ", y_predict[-1][0])
    cagr = calculate_CAGR(y[-1], y_predict[-1][0], 10)
    print('Your investments will have a CAGR of ', cagr, '%')
    x_dates = pd.to_datetime(df.index, origin='1970-01-01', unit='D')
    future_dates = pd.to_datetime(future_index, origin='1970-01-01', unit='D')
    plot_results(x_dates, df['Close'], y_learned, future_dates, y_predict)
if __name__ == "__main__":
    main()