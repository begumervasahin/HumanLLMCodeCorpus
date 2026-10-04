import math
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from keras.models import Sequential
from keras.layers import Dense, LSTM
def mean_a_p_e(y_true, y_pred):
    sum_error = 0
    for i in range(len(y_true)):
        sum_error += abs(y_pred[i] - y_true[i]) / y_true[i]
    return sum_error / len(y_true)
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    n_vars = 1 if isinstance(data, list) else data.shape[1]
    df = pd.DataFrame(data)
    cols, names = list(), list()
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [(f'var{j+1}(t-{i})') for j in range(n_vars)]
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [(f'var{j+1}(t)') for j in range(n_vars)]
        else:
            names += [(f'var{j+1}(t+{i})') for j in range(n_vars)]
    agg = pd.concat(cols, axis=1)
    agg.columns = names
    if dropnan:
        agg.dropna(inplace=True)
    return agg
def load_and_preprocess_data(filepath):
    data = pd.read_csv(filepath, header=0, index_col=0)
    values = data.values
    values = values.astype('float32')
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled = scaler.fit_transform(values)
    return scaled, scaler
def prepare_data_for_lstm(scaled, n_train_hours, n_input, n_output):
    reframed = series_to_supervised(scaled, n_input, n_output)
    reframed.drop(reframed.columns[[4, 5, 6, 7]], axis=1, inplace=True)
    values = reframed.values
    train = values[:n_train_hours, :]
    test = values[n_train_hours:, :]
    train_X, train_y = train[:, :-1], train[:, -1]
    test_X, test_y = test[:, :-1], test[:, -1]
    train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
    test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))
    return train_X, train_y, test_X, test_y
def build_and_train_lstm(train_X, train_y, test_X, test_y, epochs=50, batch_size=72):
    model = Sequential()
    model.add(LSTM(50, input_shape=(train_X.shape[1], train_X.shape[2])))
    model.add(Dense(1))
    model.compile(loss='mae', optimizer='adam')
    history = model.fit(train_X, train_y, epochs=epochs, batch_size=batch_size, validation_data=(test_X, test_y), verbose=2, shuffle=False)
    return model, history
def plot_history(history):
    plt.plot(history.history['loss'], label='train')
    plt.plot(history.history['val_loss'], label='test')
    plt.legend()
    plt.show()
def invert_scaling(scaler, yhat, test_X):
    inv_yhat = np.concatenate((yhat, test_X[:, 1:]), axis=1)
    inv_yhat = scaler.inverse_transform(inv_yhat)
    inv_yhat = inv_yhat[:, 0]
    return inv_yhat
def calculate_errors(inv_y, inv_yhat):
    rmse = math.sqrt(mean_squared_error(inv_y, inv_yhat))
    print(f'Test RMSE: {rmse:.3f}')
    mape = mean_a_p_e(inv_y, inv_yhat)
    print(f'Test MAPE: {mape:.3f}')
def main(filepath, n_train_hours=365*24, n_input=1, n_output=1, epochs=50, batch_size=72):
    scaled, scaler = load_and_preprocess_data(filepath)
    train_X, train_y, test_X, test_y = prepare_data_for_lstm(scaled, n_train_hours, n_input, n_output)
    model, history = build_and_train_lstm(train_X, train_y, test_X, test_y, epochs, batch_size)
    plot_history(history)
    yhat = model.predict(test_X)
    test_X = test_X.reshape((test_X.shape[0], test_X.shape[2]))
    inv_yhat = invert_scaling(scaler, yhat, test_X)
    test_y = test_y.reshape((len(test_y), 1))
    inv_y = np.concatenate((test_y, test_X[:, 1:]), axis=1)
    inv_y = scaler.inverse_transform(inv_y)
    inv_y = inv_y[:, 0]
    calculate_errors(inv_y, inv_yhat)
if __name__ == "__main__":
    main('path_to_your_dataset.csv')