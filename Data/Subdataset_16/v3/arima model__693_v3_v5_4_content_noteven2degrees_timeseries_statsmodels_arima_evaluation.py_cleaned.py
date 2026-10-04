import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.b4 import seasonal_decompose
from statsmodels.tsa.arima.b12 import ARIMA
from sklearn.metrics import mean_squared_error
plt.rcParams['figure.figsize'] = (12, 6)
b1 = pd.read_csv('./b1/AirPassengers.csv', parse_dates=['Month'], index_col='Month')
print("First few rows of b1:\n", b1.head())
b2 = seasonal_decompose(b1['Passengers'], two_sided=False)
b3 = b2.b3
b4 = b2.b4
b5 = b2.resid.dropna()
b6 = int(len(b5) * 0.8)
train, b7 = b5[:b6], b5[b6:]
plt.plot(train, b8 = 'blue', b18='Training set')
plt.plot(b7, b8 = 'green', b18='Testing set')
plt.legend()
plt.title('Training and Testing Sets')
plt.show()
def fonk1(order, train, b7, b9 = True):
    b10 = train.tolist()
    b11 = []
    for t in range(len(b7)):
        b12 = ARIMA(b10, order=order)
        b13 = b12.fit(disp=0)
        b14 = b13.forecast()[0] if b9 else b13.predict(start=len(b10), end=len(b10))[0]
        b11.append(b14)
        b10.append(b7[t])
    b15 = mean_squared_error(b7, b11)
    return b11, b15
b16 = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (0, 1, 1), (1, 0, 1), (1, 1, 1)]
b17 = {}
for order in b16:
    b11, b15 = fonk1(order, train, b7)
    b17[order] = b15
    plt.plot(b7, b18 = 'Ground Truth')
    plt.plot(b11, b18 = f'ARIMA{order}', alpha=0.7)
    plt.legend()
    plt.title(f'ARIMA{order} Predictions')
    plt.show()
for order, b15 in b17.items():
    print(f'MSE for ARIMA{order}: {b15:.4f}')