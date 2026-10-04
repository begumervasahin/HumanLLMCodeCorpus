import math
import matplotlib.pyplot as plt
import pandas as pd
def parser(x):
    return pd.to_datetime(x, format='%Y-%m-%d %H:%M:%S')
def mean_absolute_percentage_error(y_true, y_pred):
    sum_error = 0
    for i in range(len(y_true)):
        sum_error += math.fabs((y_pred[i] - y_true[i]) / y_true[i])
    return sum_error / len(y_true) * 100
csv_file_path = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv'
series = pd.read_csv(
    csv_file_path,
    usecols=[2, 3],
    header=0,
    parse_dates=[0],
    index_col=0,
    squeeze=True,
    date_parser=parser
)
X = series.values[:1000]
plt.figure(figsize=(10, 6))
plt.plot(X, '-', label="Real Flow")
plt.legend(loc='upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.title("Traffic Volume Time Series")
plt.show()
y_true = [1, 2, 3, 4, 5]
y_pred = [0.9, 2.1, 3.2, 4.3, 5.1]
mape = mean_absolute_percentage_error(y_true, y_pred)
print(f"Mean Absolute Percentage Error (MAPE): {mape:.2f}%")