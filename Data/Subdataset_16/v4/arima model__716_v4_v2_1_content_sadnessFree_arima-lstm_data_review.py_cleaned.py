import math
import matplotlib.pyplot as plt
from pandas import read_csv, to_datetime
def fonk1(x):
    return to_datetime(x, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(b14, b15):
    b2 = sum(abs((y_p - y_t) / y_t) for y_t, y_p in zip(b14, b15))
    return (b2 / len(b14)) * 100
b3 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv'
b4 = read_csv(
    b3,
    b5 = [2, 3],
    b6 = 0,
    b7 = [0],
    b8 = 0,
    b9 = True,
    b10 = parse_datetime
)
b11 = b4.values[:1000]
plt.plot(b11, '-', b12 = "Real Flow")
plt.legend(b13 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.title("Time Series of Traffic Volume")
plt.show()
b14 = [1, 2, 3, 4, 5]
b15 = [0.9, 2.1, 3.2, 4.3, 5.1]
b16 = fonk2(b14, b15)
print(f"Mean Absolute Percentage Error (MAPE): {b16:.2f}%")