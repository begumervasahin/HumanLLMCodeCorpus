import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
from statsmodels.tsa.b6 import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
rcParams['figure.figsize'] = 12, 6
b1 = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
b2 = pd.read_csv('./b2/AirPassengers.csv', parse_dates='Month', index_col='Month', date_parser=b1)
b3 = b2['Passengers']
b4 = seasonal_decompose(b3, two_sided=False)
b5 = b4.b5
b6 = b4.b6
b7 = b4.resid
b7.dropna(b8 = True)
b9 = int(len(b7) * 0.8)
train, b10 = b7[0:b9], b7[b9:len(b7)]
plt.plot(train.index, train, b11 = 'blue', b28='Training set')
plt.plot(b10.index, b10, b11 = 'green', b28='Testing set')
plt.legend()
plt.title('Ground truth training and testing set')
plt.show()
def fonk1(order):
    b12 = [x for x in train]
    b13 = list()
    b14 = list()
    for t in range(len(b10)):
        b15 = ARIMA(b12, order=order)
        b16 = b15.fit(disp=-1)
        b17 = b16.forecast()[0][0]
        b18 = b16.predict(start=len(b12), end=len(b12))[0]
        b13.append(b17)
        b14.append(b18)
        b12.append(b10[t])
    b19 = mean_squared_error(b10, b13)
    b20 = mean_squared_error(b10, b14)
    print('MSE forecast:\t\t\t{:1.4f}'.format(b19))
    print('MSE predict:\t\t\t{:1.4f}'.format(b20))
    return {'Predictions forecast': b13,
            'Predictions predict': b14,
            'MSE forecast': b19,
            'MSE predict': b20}
b21 = fonk1((1, 0, 0))
b22 = fonk1((0, 1, 0))
b23 = fonk1((0, 0, 1))
b24 = fonk1((1, 1, 0))
b25 = fonk1((0, 1, 1))
b26 = fonk1((1, 0, 1))
b27 = fonk1((1, 1, 1))
plt.plot(b10, b28 = 'Ground Truth')
plt.plot(b21['Predictions forecast'], b11 = 'red', b28='.forecast()')
plt.plot(b21['Predictions predict'], b11 = 'green', b28='.predict()')
plt.legend()
plt.title('AR')
plt.show()
plt.plot(b10, b28 = 'Ground Truth')
plt.plot(b24['Predictions forecast'], b11 = 'red', b28='.forecast()')
plt.plot(b24['Predictions predict'], b11 = 'green', b28='.predict()')
plt.legend()
plt.title('ARMA')
plt.show()