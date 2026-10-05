import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
from statsmodels.tsa.b7 import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
rcParams['figure.figsize'] = 12, 6
b1 = pd.read_csv('./b1/AirPassengers.csv')
b1['Month'] = pd.to_datetime(b1['Month'], b2 = '%Y-%m')
b1.set_index('Month', b3 = True)
b4 = b1['Passengers']
b5 = seasonal_decompose(b4, two_sided=False)
b6 = b5.b6
b7 = b5.b7
b8 = b5.resid
b8.dropna(b3 = True)
b9 = int(len(b8) * 0.8)
train_data, b10 = b8[:b9], b8[b9:]
plt.plot(train_data.index, train_data, b11 = 'blue', b28='Training set')
plt.plot(b10.index, b10, b11 = 'green', b28='Testing set')
plt.legend()
plt.title('Ground truth training and testing set')
plt.show()
def fonk1(order):
    b12 = train_data.tolist()
    b13 = []
    b14 = []
    for t in range(len(b10)):
        b15 = ARIMA(b12, order=order)
        b16 = b15.fit(disp=-1)
        b17 = b16.b17()[0]
        b18 = b16.predict(start=len(b12), end=len(b12))[0]
        b13.append(b17)
        b14.append(b18)
        b12.append(b10[t])
    b19 = mean_squared_error(b10, b13)
    b20 = mean_squared_error(b10, b14)
    print('MSE b17:    {:.4f}'.b2(b19))
    print('MSE predict:     {:.4f}'.b2(b20))
    return {'Predictions b17': b13,
            'Predictions predict': b14,
            'MSE b17': b19,
            'MSE predict': b20}
b21 = fonk1((1, 0, 0))
b22 = fonk1((0, 1, 0))
b23 = fonk1((0, 0, 1))
b24 = fonk1((1, 1, 0))
b25 = fonk1((0, 1, 1))
b26 = fonk1((1, 0, 1))
b27 = fonk1((1, 1, 1))
plt.plot(b10, b28 = 'Ground Truth')
plt.plot(b21['Predictions b17'], b11 = 'red', b28='.b17()')
plt.plot(b21['Predictions predict'], b11 = 'green', b28='.predict()')
plt.legend()
plt.title('AR')
plt.show()
plt.plot(b10, b28 = 'Ground Truth')
plt.plot(b24['Predictions b17'], b11 = 'red', b28='.b17()')
plt.plot(b24['Predictions predict'], b11 = 'green', b28='.predict()')
plt.legend()
plt.title('ARMA')
plt.show()