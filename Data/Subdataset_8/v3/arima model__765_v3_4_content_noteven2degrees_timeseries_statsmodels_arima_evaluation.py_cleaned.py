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
passenger_data = data['Passengers']
decomposition = seasonal_decompose(passenger_data, two_sided=False)
trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid
residual.dropna(inplace=True)
train_size = int(len(residual) * 0.8)
train_data, test_data = residual[:train_size], residual[train_size:]
plt.plot(train_data.index, train_data, color='blue', label='Training set')
plt.plot(test_data.index, test_data, color='green', label='Testing set')
plt.legend()
plt.title('Ground truth training and testing set')
plt.show()
def compare_ARIMA_modes_testing(order):
    history = train_data.tolist()
    predictions_forecast = []
    predictions_predict = []
    for t in range(len(test_data)):
        model = ARIMA(history, order=order)
        model_fit = model.fit(disp=-1)
        forecast = model_fit.forecast()[0]
        prediction = model_fit.predict(start=len(history), end=len(history))[0]
        predictions_forecast.append(forecast)
        predictions_predict.append(prediction)
        history.append(test_data[t])
    mse_forecast = mean_squared_error(test_data, predictions_forecast)
    mse_predict = mean_squared_error(test_data, predictions_predict)
    print('MSE forecast:    {:.4f}'.format(mse_forecast))
    print('MSE predict:     {:.4f}'.format(mse_predict))
    return {'Predictions forecast': predictions_forecast,
            'Predictions predict': predictions_predict,
            'MSE forecast': mse_forecast,
            'MSE predict': mse_predict}
ar_testing = compare_ARIMA_modes_testing((1, 0, 0))
ma_testing = compare_ARIMA_modes_testing((0, 1, 0))
ig_testing = compare_ARIMA_modes_testing((0, 0, 1))
arma_testing = compare_ARIMA_modes_testing((1, 1, 0))
igma_testing = compare_ARIMA_modes_testing((0, 1, 1))
arig_testing = compare_ARIMA_modes_testing((1, 0, 1))
arima_testing = compare_ARIMA_modes_testing((1, 1, 1))
plt.plot(test_data, label='Ground Truth')
plt.plot(ar_testing['Predictions forecast'], color='red', label='.forecast()')
plt.plot(ar_testing['Predictions predict'], color='green', label='.predict()')
plt.legend()
plt.title('AR')
plt.show()
plt.plot(test_data, label='Ground Truth')
plt.plot(arma_testing['Predictions forecast'], color='red', label='.forecast()')
plt.plot(arma_testing['Predictions predict'], color='green', label='.predict()')
plt.legend()
plt.title('ARMA')
plt.show()