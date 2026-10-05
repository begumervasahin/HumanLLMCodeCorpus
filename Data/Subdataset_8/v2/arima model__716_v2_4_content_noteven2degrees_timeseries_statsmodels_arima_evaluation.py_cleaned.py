import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
rcParams['figure.figsize'] = 12, 6
data = pd.read_csv('./data/AirPassengers.csv')
data['Month'] = pd.to_datetime(data['Month'], format='%Y-%m')
data.set_index('Month', inplace=True)
ts = data['Passengers']
decomposition = seasonal_decompose(ts, two_sided=False)
trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid
residual.dropna(inplace=True)
train_size = int(len(residual) * 0.8)
train, test = residual[:train_size], residual[train_size:]
plt.plot(train.index, train, color='blue', label='Training set')
plt.plot(test.index, test, color='green', label='Testing set')
plt.legend()
plt.title('Ground truth training and testing set')
plt.show()
def compare_ARIMA_modes_testing(order):
    history = train.tolist()
    predictions_f = []
    predictions_p = []
    for t in range(len(test)):
        model = ARIMA(history, order=order)
        model_fit = model.fit(disp=-1)
        yhat_f = model_fit.forecast()[0]
        yhat_p = model_fit.predict(start=len(history), end=len(history))[0]
        predictions_f.append(yhat_f)
        predictions_p.append(yhat_p)
        history.append(test[t])
    error_f = mean_squared_error(test, predictions_f)
    error_p = mean_squared_error(test, predictions_p)
    print('MSE forecast:    {:.4f}'.format(error_f))
    print('MSE predict:     {:.4f}'.format(error_p))
    return {'Predictions forecast': predictions_f,
            'Predictions predict': predictions_p,
            'MSE forecast': error_f,
            'MSE predict': error_p}
ar_testing = compare_ARIMA_modes_testing((1, 0, 0))
ma_testing = compare_ARIMA_modes_testing((0, 1, 0))
ig_testing = compare_ARIMA_modes_testing((0, 0, 1))
arma_testing = compare_ARIMA_modes_testing((1, 1, 0))
igma_testing = compare_ARIMA_modes_testing((0, 1, 1))
arig_testing = compare_ARIMA_modes_testing((1, 0, 1))
arima_testing = compare_ARIMA_modes_testing((1, 1, 1))
plt.plot(test, label='Ground Truth')
plt.plot(ar_testing['Predictions forecast'], color='red', label='.forecast()')
plt.plot(ar_testing['Predictions predict'], color='green', label='.predict()')
plt.legend()
plt.title('AR')
plt.show()
plt.plot(test, label='Ground Truth')
plt.plot(arma_testing['Predictions forecast'], color='red', label='.forecast()')
plt.plot(arma_testing['Predictions predict'], color='green', label='.predict()')
plt.legend()
plt.title('ARMA')
plt.show()