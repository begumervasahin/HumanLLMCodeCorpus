import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error
def parser(x):
    return to_datetime(x, format='%Y-%m-%d %H:%M:%S')
def mean_absolute_percentage_error(y_true, y_pred):
    return sum(abs(y_pred[i] - y_true[i]) / y_true[i] for i in range(len(y_true))) / len(y_true)
series = read_csv('/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15-2.csv',
                  usecols=[2, 3], header=0, parse_dates=[0], index_col=0,
                  date_parser=parser)
X = series.values.astype('float32')
start = 2000
size = 1100
test_size = 500
line_test_size = 300
windows_size = 10
test_start = line_test_size + windows_size - 1
arima_train, arima_test = X[start:start + size], X[start + size:start + size + test_size]
history = list(arima_train)
predictions = []
for t in range(len(arima_test)):
    model = ARIMA(history, order=(4, 1, 0))
    model_fit = model.fit()
    yhat = model_fit.forecast()[0]
    predictions.append(yhat)
    obs = arima_test[t]
    history.append(obs)
    print(f'predicted={yhat:.6f}, expected={obs:.6f}')
mse = mean_squared_error(arima_test, predictions)
mae = mean_absolute_error(arima_test, predictions)
mape = mean_absolute_percentage_error(arima_test, predictions)
print(f'ARIMA Test MAE: {mae:.3f}, MSE: {mse:.3f}, RMSE: {math.sqrt(mse):.3f}, MAPE: {mape:.3f}')
plt.figure(figsize=(12, 6))
plt.plot(arima_test[test_start:], '-', label="Real flow")
plt.plot(predictions[test_start:], '--', color='red', label="ARIMA")
plt.legend(loc='upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.ylim(0, 800)
plt.show()