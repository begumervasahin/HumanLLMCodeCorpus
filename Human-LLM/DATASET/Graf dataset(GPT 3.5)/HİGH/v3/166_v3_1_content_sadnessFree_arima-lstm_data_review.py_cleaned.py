import math
import matplotlib.pyplot as plt
from pandas import read_csv, datetime
def fonk1(x):
    return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    b1 = sum(math.fabs((predicted - actual) / actual) for actual, predicted in zip(y_true, y_pred))
    return (b1 / len(y_true)) * 100
b2 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv'
b3 = read_csv(b2, usecols=[2, 3], header=0, parse_dates=[0],
                  b4 = 0, squeeze=True, date_parser=parse_datetime)
b5 = b3.values[:1000]
plt.plot(b5, '-', b6 = "Real Flow")
plt.legend(b7 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.show()
b8 = [1, 2, 3, 4, 5]
b9 = [0.9, 2.1, 3.2, 4.3, 5.1]
b10 = fonk2(b8, b9)
print(f"Mean Absolute Percentage Error (MAPE): {b10:.2f}%")