import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from math import sqrt
def format_output_column(data, n_in=1, n_out=1, dropnan=True):
    n_vars = data.shape[1] if isinstance(data, np.ndarray) else 1
    df = pd.DataFrame(data)
    cols, names = [], []
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [f'var{j+1}(t-{i})' for j in range(n_vars)]
    for i in range(n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [f'var{j+1}(t)' for j in range(n_vars)]
        else:
            names += [f'var{j+1}(t+{i})' for j in range(n_vars)]
    agg = pd.concat(cols, axis=1)
    agg.columns = names
    if dropnan:
        agg.dropna(inplace=True)
    return agg
def load_and_preprocess_data(filename):
    dataset = pd.read_csv(filename, header=0, index_col=0)
    values = dataset.values.astype('float32')
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled = scaler.fit_transform(values)
    reframed = format_output_column(scaled, 1, 1)
    reframed.drop(reframed.columns[[6, 7, 8, 9]], axis=1, inplace=True)
    return reframed, scaler
def split_data(reframed, n_train_hours):
    values = reframed.values
    train, test = values[:n_train_hours, :], values[n_train_hours:, :]
    train_X, train_y = train[:, :-1], train[:, -1]
    test_X, test_y = test[:, :-1], test[:, -1]
    train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
    test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))
    return train_X, train_y, test_X, test_y
def build_and_train_model(train_X, train_y, test_X, test_y, epochs=100, batch_size=50):
    model = Sequential()
    model.add(LSTM(300, input_shape=(train_X.shape[1], train_X.shape[2])))
    model.add(Dense(1))
    model.compile(loss='mae', optimizer='adam')
    history = model.fit(train_X, train_y, epochs=epochs, batch_size=batch_size, validation_data=(test_X, test_y), verbose=2, shuffle=False)
    return model, history
def plot_training_history(history):
    plt.plot(history.history['loss'], label='train')
    plt.plot(history.history['val_loss'], label='test')
    plt.legend()
    plt.title('RNN Fitting')
    plt.xlabel('Epochs', fontsize=16)
    plt.ylabel('Value Loss', fontsize=16)
    plt.show()
def invert_scaling(yhat, test_X, scaler):
    test_X = test_X.reshape((test_X.shape[0], test_X.shape[2]))
    inv_yhat = np.concatenate((yhat, test_X[:, 1:]), axis=1)
    inv_yhat = scaler.inverse_transform(inv_yhat)
    return inv_yhat[:, 0]
def plot_forecast_vs_actual(inv_y, inv_yhat):
    plt.plot(inv_y, marker='o', linestyle='-', color='b', label='Actual Price')
    plt.plot(inv_yhat, marker='o', linestyle='-', color='r', label='Forecasted Price using LSTM RNN')
    plt.legend()
    plt.title("Testing over past 30 days")
    plt.xlabel('Days', fontsize=18)
    plt.ylabel('Bitcoin Price ($)', fontsize=16)
    plt.show()
def calculate_rmse(inv_y, inv_yhat):
    rmse = sqrt(mean_squared_error(inv_y, inv_yhat))
    print(f'Test RMSE: {rmse:.3f}')
def main():
    filename = 'ReducedFeatureSet.csv'
    n_train_hours = 365*2 + (365 - 30)
    reframed, scaler = load_and_preprocess_data(filename)
    train_X, train_y, test_X, test_y = split_data(reframed, n_train_hours)
    model, history = build_and_train_model(train_X, train_y, test_X, test_y)
    plot_training_history(history)
    yhat = model.predict(test_X)
    inv_yhat = invert_scaling(yhat, test_X, scaler)
    test_y = test_y.reshape((len(test_y), 1))
    inv_y = np.concatenate((test_y, test_X[:, 1:]), axis=1)
    inv_y = scaler.inverse_transform(inv_y)
    inv_y = inv_y[:, 0]
    plot_forecast_vs_actual(inv_y, inv_yhat)
    calculate_rmse(inv_y, inv_yhat)
if __name__ == "__main__":
    main()