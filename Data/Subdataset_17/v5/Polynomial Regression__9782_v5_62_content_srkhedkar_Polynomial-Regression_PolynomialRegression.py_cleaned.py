import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
def calculate_CAGR(initial_value, final_value, periods):
    return ((final_value / initial_value) ** (1 / periods) - 1) * 100
file_path = 'D:\\python3\\data\\SensexHistoricalData.csv'
df = pd.read_csv(file_path)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
days_since_epoch = (df.index - pd.to_datetime('1970-01-01')).days
df.index = days_since_epoch
closing_prices = df['Close'].values
days = df.index.values
poly_features = PolynomialFeatures(degree=5)
X_poly = poly_features.fit_transform(days.reshape(-1, 1))
model = LinearRegression()
model.fit(X_poly, closing_prices.reshape(-1, 1))
learned_values = model.predict(X_poly)
future_days = np.arange(days[-1], days[-1] + 3650)
future_X_poly = poly_features.fit_transform(future_days.reshape(-1, 1))
future_predictions = model.predict(future_X_poly)
closing_price_2029 = future_predictions[-1][0]
print(f"Closing price at 2029 would be around {closing_price_2029:.2f}")
cagr_value = calculate_CAGR(closing_prices[-1], closing_price_2029, 10)
print(f"Your investments will have a CAGR of {cagr_value:.2f}%")
historical_dates = pd.to_datetime(df.index, origin='1970-01-01', unit='D')
future_dates = pd.to_datetime(future_days, origin='1970-01-01', unit='D')
plt.figure(figsize=(16, 8))
plt.plot(historical_dates, df['Close'], label='Close Price History')
plt.plot(historical_dates, learned_values, color='r', label='Mathematical Model')
plt.plot(future_dates, future_predictions, color='g', label='Future Predictions')
plt.suptitle('Stock Market Predictions', fontsize=16)
fig = plt.gcf()
fig.canvas.manager.set_window_title('Stock Market Predictions')
plt.legend()
plt.show()