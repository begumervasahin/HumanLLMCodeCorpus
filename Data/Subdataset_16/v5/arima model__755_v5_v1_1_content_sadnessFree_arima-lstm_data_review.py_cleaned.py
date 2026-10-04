import math
import matplotlib.pyplot as plt
import pandas as pd
def fonk1(x):
    return pd.to_datetime(x, b1 = '%Y-%m-%d %H:%M:%S')
def fonk2(b14, b15):
    a1 = 0
    for i in range(len(b14)):
        a1 += math.fabs((b15[i] - b14[i]) / b14[i])
    return a1 / len(b14) * 100
b2 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv'
b3 = pd.read_csv(
    b2,
    b4 = [2, 3],
    b5 = 0,
    b6 = [0],
    b7 = 0,
    b8 = True,
    b9 = parser
)
b10 = b3.values[:1000]
plt.figure(b11 = (10, 6))
plt.plot(b10, '-', b12 = "Real Flow")
plt.legend(b13 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicle/period)")
plt.title("Traffic Volume Time Series")
plt.show()
b14 = [1, 2, 3, 4, 5]
b15 = [0.9, 2.1, 3.2, 4.3, 5.1]
b16 = fonk2(b14, b15)
print(f"Mean Absolute Percentage Error (MAPE): {b16:.2f}%")