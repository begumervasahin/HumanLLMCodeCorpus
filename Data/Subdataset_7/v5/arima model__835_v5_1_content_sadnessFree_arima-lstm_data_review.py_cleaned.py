import math
import matplotlib.pyplot as plt
from pandas import read_csv, datetime
def fonk1(x):
    return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
def fonk2(y_true, y_pred):
    b1 = sum(math.fabs(pred - true) / true for true, pred in zip(y_true, y_pred))
    return b1 / len(y_true)
b2 = '/Users/daihanru/Desktop/arima-lstm/DataSet/FEB15.csv'
b3 = [2, 3]
b4 = 'DateColumn'
b5 = read_csv(b2, usecols=b3, header=0,
                  b6 = [b4], index_col=b4,
                  b7 = True, date_parser=parse_date)
b8 = b5.head(1000)
plt.plot(b8, '-', b9 = "Real Flow")
plt.legend(b10 = 'upper right')
plt.xlabel("Period (15-minute intervals)")
plt.ylabel("Volume (vehicles/period)")
plt.show()