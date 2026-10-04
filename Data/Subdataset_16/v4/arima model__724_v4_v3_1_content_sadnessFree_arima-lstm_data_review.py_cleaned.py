
import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
def fonk1(x):
    return to_datetime(x, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    b2 = sum(math.fabs((predicted - actual) / actual) for actual, predicted in zip(y_true, y_pred))
    return (b2 / len(y_true)) * 100
b3 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv'
b4 = read_csv(b3, usecols=[2, 3], header=0, parse_dates=[0],
                  b5 = 0, squeeze=True, date_parser=parse_datetime)
b6 = b4.values[:1000]
plt.figure(b7 = (10, 6))
plt.plot(b6, '-', b8 = "Real Flow")
plt.legend(b9 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.title("Time Series of Traffic Flow")
plt.grid(True)
plt.show()
b10 = [1, 2, 3, 4, 5]
b11 = [0.9, 2.1, 3.2, 4.3, 5.1]
b12 = fonk2(b10, b11)
print(f"Mean Absolute Percentage Error (MAPE): {b12:.2f}%")