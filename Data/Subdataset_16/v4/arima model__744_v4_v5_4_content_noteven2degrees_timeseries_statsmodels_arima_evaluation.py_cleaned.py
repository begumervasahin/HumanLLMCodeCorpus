import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.b4 import seasonal_decompose
from statsmodels.tsa.arima.b13 import ARIMA
from sklearn.metrics import mean_squared_error
plt.rcParams['figure.figsize'] = [12, 6]
b1 = pd.read_csv('./b1/AirPassengers.csv', parse_dates=['Month'], index_col='Month')
print("First few rows of b1:\n", b1.head())
b2 = seasonal_decompose(b1['Passengers'], two_sided=False)
b3 = b2.b3
b4 = b2.b4
b5 = b2.resid
b5.dropna(b6 = True)
b7 = int(len(b5) * 0.8)
train, b8 = b5[:b7], b5[b7:]
plt.plot(train, b9 = 'blue', b19='Training set')
plt.plot(b8, b9 = 'green', b19='Testing set')
plt.legend()
plt.title('Training and Testing Sets')
plt.show()
def fonk1(order, b10 = True):
    b11 = [x for x in train]
    b12 = []
    for t in range(len(b8)):
        b13 = ARIMA(b11, order=order)
        b14 = b13.fit(disp=0)
        if b10:
            b15 = b14.forecast()[0]
        else:
            b15 = b14.predict(start=len(b11), end=len(b11))[0]
        b12.append(b15)
        b11.append(b8[t])
    b16 = mean_squared_error(b8, b12)
    return b12, b16
b17 = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (0, 1, 1), (1, 0, 1), (1, 1, 1)]
b18 = {}
for order in b17:
    b12, b16 = fonk1(order)
    b18[order] = b16
    plt.plot(b8, b19 = 'Ground Truth')
    plt.plot(b12, b19 = f'ARIMA{order}', alpha=0.7)
    plt.legend()
    plt.title(f'ARIMA{order} Predictions')
    plt.show()
for order, b16 in b18.items():
    print(f'MSE for ARIMA{order}: {b16:.4f}')