import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
def CAGR(first, last, periods):
    return ((last / first) ** (1 / periods) - 1) * 100
df = pd.read_csv('D:\\python3\\data\\SensexHistoricalData.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df.index = (df.index - pd.to_datetime('1970-01-01')).days
y = df['Close'].values
x = df.index.values
regression_model = LinearRegression()
poly = PolynomialFeatures(5)
X_transform = poly.fit_transform(x.reshape(-1, 1))
regression_model.fit(X_transform, y.reshape(-1, 1))
y_learned = regression_model.predict(X_transform)
newindex = np.arange(x[-1], x[-1] + 3650)
X_extended_transform = poly.fit_transform(newindex.reshape(-1, 1))
y_predict = regression_model.predict(X_extended_transform)
closing_price_2029 = y_predict[-1][0]
print(f"Closing price at 2029 would be around {closing_price_2029:.2f}")
cagr_value = CAGR(y[-1], closing_price_2029, 10)
print(f"Your investments will have a CAGR of {cagr_value:.2f}%")
x_dates = pd.to_datetime(df.index, origin='1970-01-01', unit='D')
future_x_dates = pd.to_datetime(newindex, origin='1970-01-01', unit='D')
plt.figure(figsize=(16, 8))
plt.plot(x_dates, df['Close'], label='Close Price History')
plt.plot(x_dates, y_learned, color='r', label='Mathematical Model')
plt.plot(future_x_dates, y_predict, color='g', label='Future Predictions')
plt.suptitle('Stock Market Predictions', fontsize=16)
fig = plt.gcf()
fig.canvas.manager.set_window_title('Stock Market Predictions')
plt.legend()
plt.show()