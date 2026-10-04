import math
import matplotlib.pyplot as plt
from pandas import read_csv
from pandas import datetime
def fonk1(x):
    return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
def fonk2(b7, b8):
    a1 = 0
    for i in range(len(b7)):
        a1 += math.fabs((b8[i] - b7[i]) / b7[i])
    return a1 / len(b7) * 100
b1 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv'
b2 = read_csv(b1, usecols=[2, 3], header=0, parse_dates=[0],
                  b3 = 0, squeeze=True, date_parser=parser)
b4 = b2.values[0:1000]
plt.plot(b4, '-', b5 = "real flow")
plt.legend(b6 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.title("Traffic Volume Time Series")
plt.show()
b7 = [1, 2, 3, 4, 5]
b8 = [0.9, 2.1, 3.2, 4.3, 5.1]
b9 = fonk2(b7, b8)
print(f"Mean Absolute Percentage Error (MAPE): {b9:.2f}%")