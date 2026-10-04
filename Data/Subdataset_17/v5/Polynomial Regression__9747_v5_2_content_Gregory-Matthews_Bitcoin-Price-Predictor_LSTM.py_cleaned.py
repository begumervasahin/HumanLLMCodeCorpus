from keras.models import Sequential
from keras.layers import Dense, LSTM
from math import sqrt
from numpy import concatenate
from pandas import DataFrame, read_csv, concat
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot as plt
def format_output_column(data, n_in=1, n_out=1, dropnan=True):
    n_vars = 1 if type(data) is list else data.shape[1]
    df = DataFrame(data)
    cols, names = [], []
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
    for i in range(n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
        else:
            names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
    agg = concat(cols, axis=1)
    agg.columns = names
    if dropnan:
        agg.dropna(inplace=True)
    return agg
def load_and_preprocess_data(file_path):
    dataset = read_csv(file_path, header=0, index_col=0)
    values = dataset.values.astype('float32')
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled = scaler.fit_transform(values)
    return scaled, scaler
def split_data(values, n_train_hours):
    train = values[:n_train_hours, :]
    test = values[n_train_hours:, :]
    train_X, train_y = train[:, :-1], train[:, -1]
    test_X, test_y = test[:, :-1], test[:, -1]
    return train_X, train_y, test_X, test_y
def reshape_data(train_X, test_X):
    train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
    test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))
    return train_X, test_X
def design_and_fit_lstm(train_X, train_y, test_X, test_y):
    model = Sequential()
    model.add(LSTM(300, input_shape=(train_X.shape[1], train_X.shape[2])))
    model.add(Dense(1))
    model.compile(loss='mae', optimizer='adam')
    history = model.fit(train_X, train_y, epochs=100, batch_size=50, validation_data=(test_X, test_y), verbose=2, shuffle=False)
    return model, history
def plot_training_history(history):
    plt.plot(history.history['loss'], label='train')
    plt.plot(history.history['val_loss'], label='test')
    plt.legend()
    plt.title('RNN Fitting')
    plt.xlabel('Epochs', fontsize=16)
    plt.ylabel('Value Loss', fontsize=16)
    plt.show()
def invert_scaling_and_calculate_rmse(scaler, yhat, test_X, test_y):
    test_X = test_X.reshape((test_X.shape[0], test_X.shape[2]))
    inv_yhat = concatenate((yhat, test_X[:, 1:]), axis=1)
    inv_yhat = scaler.inverse_transform(inv_yhat)
    inv_yhat = inv_yhat[:, 0]
    test_y = test_y.reshape((len(test_y), 1))
    inv_y = concatenate((test_y, test_X[:, 1:]), axis=1)
    inv_y = scaler.inverse_transform(inv_y)
    inv_y = inv_y[:, 0]
    rmse = sqrt(mean_squared_error(inv_y, inv_yhat))
    return inv_y, inv_yhat, rmse
def plot_actual_vs_predicted(actual, predicted):
    plt.plot(actual, marker='o', linestyle='-', color='b', label='Actual Price')
    plt.plot(predicted, marker='o', linestyle='-', color='r', label='Forecasted Price using LSTM RNN')
    plt.legend()
    plt.title("Testing over past 30 days")
    plt.xlabel('Days', fontsize=18)
    plt.ylabel('Bitcoin Price ($)', fontsize=16)
    plt.show()
def main():
    file_path = 'ReducedFeatureSet.csv'
    scaled, scaler = load_and_preprocess_data(file_path)
    reframed = format_output_column(scaled, 1, 1)
    reframed.drop(reframed.columns[[6, 7, 8, 9]], axis=1, inplace=True)
    values = reframed.values
    n_train_hours = 365*2 + (365 - 30)
    train_X, train_y, test_X, test_y = split_data(values, n_train_hours)
    train_X, test_X = reshape_data(train_X, test_X)
    model, history = design_and_fit_lstm(train_X, train_y, test_X, test_y)
    plot_training_history(history)
    yhat = model.predict(test_X)
    inv_y, inv_yhat, rmse = invert_scaling_and_calculate_rmse(scaler, yhat, test_X, test_y)
    plot_actual_vs_predicted(inv_y, inv_yhat)
    print('Test RMSE: %.3f' % rmse)
if __name__ == "__main__":
    main()