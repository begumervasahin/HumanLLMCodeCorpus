import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from keras.models import Sequential
from keras.layers import Dense, LSTM
def mean_absolute_percentage_error(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    n_vars = 1 if isinstance(data, list) else data.shape[1]
    df = pd.DataFrame(data)
    cols, names = [], []
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [('var%d(t-%d)' % (j + 1, i)) for j in range(n_vars)]
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('var%d(t)' % (j + 1)) for j in range(n_vars)]
        else:
            names += [('var%d(t+%d)' % (j + 1, i)) for j in range(n_vars)]
    agg = pd.concat(cols, axis=1)
    agg.columns = names
    if dropnan:
        agg.dropna(inplace=True)
    return agg
def create_lstm_model(input_shape):
    model = Sequential()
    model.add(LSTM(50, input_shape=input_shape))
    model.add(Dense(1))
    model.compile(loss='mae', optimizer='adam')
    return model
def plot_results(true_values, predicted_values):
    plt.figure(figsize=(10, 6))
    plt.plot(true_values, label='True Values')
    plt.plot(predicted_values, label='Predicted Values')
    plt.title('True vs Predicted Values')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.show()
def main():
    data = np.sin(np.linspace(0, 100, 200))
    data = data.reshape((len(data), 1))
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data)
    n_in = 3
    n_out = 1
    reframed = series_to_supervised(scaled_data, n_in, n_out)
    values = reframed.values
    n_train = int(len(values) * 0.67)
    train = values[:n_train, :]
    test = values[n_train:, :]
    n_obs = n_in
    train_X, train_y = train[:, :n_obs], train[:, -n_out]
    test_X, test_y = test[:, :n_obs], test[:, -n_out]
    train_X = train_X.reshape((train_X.shape[0], n_in, 1))
    test_X = test_X.reshape((test_X.shape[0], n_in, 1))
    model = create_lstm_model((train_X.shape[1], train_X.shape[2]))
    model.fit(train_X, train_y, epochs=50, batch_size=72, validation_data=(test_X, test_y), verbose=2, shuffle=False)
    yhat = model.predict(test_X)
    test_X = test_X.reshape((test_X.shape[0], n_in))
    inv_yhat = np.concatenate((yhat, test_X[:, 1:]), axis=1)
    inv_yhat = scaler.inverse_transform(inv_yhat)
    inv_yhat = inv_yhat[:, 0]
    test_y = test_y.reshape((len(test_y), 1))
    inv_y = np.concatenate((test_y, test_X[:, 1:]), axis=1)
    inv_y = scaler.inverse_transform(inv_y)
    inv_y = inv_y[:, 0]
    mae = mean_absolute_error(inv_y, inv_yhat)
    mse = mean_squared_error(inv_y, inv_yhat)
    mape = mean_absolute_percentage_error(inv_y, inv_yhat)
    print(f'MAE: {mae}')
    print(f'MSE: {mse}')
    print(f'MAPE: {mape}')
    plot_results(inv_y, inv_yhat)
if __name__ == "__main__":
    main()