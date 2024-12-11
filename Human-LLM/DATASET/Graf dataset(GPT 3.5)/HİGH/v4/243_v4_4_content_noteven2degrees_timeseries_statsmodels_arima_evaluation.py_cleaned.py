
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.b6 import seasonal_decompose
from statsmodels.tsa.b30.b33 import ARIMA
from sklearn.metrics import mean_squared_error
plt.rcParams['figure.figsize'] = 12, 6
b1 = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
b2 = pd.read_csv('./b2/AirPassengers.csv', parse_dates='Month', index_col='Month', b1=b1)
print(b2.head())
b3 = b2['Passengers']
b4 = seasonal_decompose(b3, two_sided=False)
b5 = b4.b5
b6 = b4.b6
b7 = b4.resid
b7.dropna(b8 = True)
b9 = int(len(b7) * 0.8)
train, b10 = b7[0:b9], b7[b9:len(b7)]
plt.plot(train.index, train, b11 = 'blue', b31='Training set')
plt.plot(b10.index, b10, b11 = 'green', b31='Testing set')
plt.legend()
plt.title('Ground truth training and testing set')
plt.show()
def fonk1(order):
    b12 = [x for x in train]
    b13 = [x for x in train]
    b14 = []
    b15 = []
    for t in range(len(b10)):
        b16 = ARIMA(b12, order=order)
        b17 = ARIMA(b13, order=order)
        b18 = b16.fit(disp=-1)
        b19 = b17.fit(disp=-1)
        b20 = b18.forecast()[0][0]
        b21 = b19.predict(start=len(b13), end=len(b13))[0]
        b14.append(b20)
        b15.append(b21)
        b12.append(b20)
        b13.append(b21)
    b22 = mean_squared_error(b10, b14)
    b23 = mean_squared_error(b10, b15)
    print('MSE forecast:\t\t\t{:1.4f}'.format(b22))
    print('MSE predict:\t\t\t{:1.4f}'.format(b23))
    return {'Predictions forecast': b14,
            'Predictions predict': b15,
            'MSE forecast': b22,
            'MSE predict': b23}
b24 = fonk1((1, 0, 0))
b25 = fonk1((0, 1, 0))
b26 = fonk1((0, 0, 1))
b27 = fonk1((1, 1, 0))
b28 = fonk1((0, 1, 1))
b29 = fonk1((1, 0, 1))
b30 = fonk1((1, 1, 1))
plt.plot(b10, b31 = 'Ground Truth')
plt.plot(b24['Predictions forecast'], b11 = 'red', b31='.forecast()')
plt.plot(b24['Predictions predict'], b11 = 'green', b31='.predict()')
plt.legend()
plt.title('AR')
plt.show()
plt.plot(b10, b31 = 'Ground Truth')
plt.plot(b27['Predictions forecast'], b11 = 'red', b31='.forecast()')
plt.plot(b27['Predictions predict'], b11 = 'green', b31='.predict()')
plt.legend()
plt.title('ARMA')
plt.show()
def fonk2(order):
    b32 = [x for x in train]
    b33 = ARIMA(b32, order=order)
    b34 = b33.fit(disp=-1)
    b35 = b34.forecast(steps=len(b10))[0]
    b36 = b34.predict(start=len(b32), end=len(b32)+len(b10)-1)
    b37 = mean_squared_error(b10, b35)
    b38 = mean_squared_error(b10, b36)
    print('MSE forecast:\t\t\t{:1.4f}'.format(b37))
    print('MSE predict:\t\t\t{:1.4f}'.format(b38))
    return {'Predictions forecast': b35,
            'Predictions predict': b36,
            'MSE forecast': b37,
            'MSE predict': b38}
b39 = fonk2((1, 0, 0))
b40 = fonk2((0, 1, 0))
b41 = fonk2((0, 0, 1))
b42 = fonk2((1, 1, 0))
b43 = fonk2((0, 1, 1))
b44 = fonk2((1, 0, 1))
b45 = fonk2((1, 1, 1))
plt.plot(b10, b31 = 'Ground Truth')
plt.plot(b39['Predictions forecast'], b11 = 'red', b31='.forecast(steps)')
plt.plot(b39['Predictions predict'], b11 = 'green', b31='.predict(steps)')
plt.legend()
plt.title('AR')
plt.show()
plt.plot(b10, b31 = 'Ground Truth')
plt.plot(b42['Predictions forecast'], b11 = 'red', b31='.forecast(steps)')
plt.plot(b42['Predictions predict'], b11 = 'green', b31='.predict(steps)')
plt.legend()
plt.title('ARMA')
plt.show()