import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
start_date = sys.argv[1]
days_training = int(sys.argv[2])
nr_forecasting = int(sys.argv[3])
def process_single_file(file_name):
    file_location = f'./data/{file_name}'
    print(f"Processing file: {file_location}")
    df = pd.read_csv(file_location)
    df['OC'] = df['Open'] - df['Close']
    df['Title'] = file_name
    df = df.set_index('Date')
    df = df.truncate(before=str(pd.Timestamp(start_date) - pd.DateOffset(1)))
    df = df.iloc[:days_training + nr_forecasting]
    df.to_csv(f'./single_data/{file_name}')
    return df
def plot_and_save(file_name):
    location = f'./single_data/{file_name}'
    df = pd.read_csv(location)
    df['Date'] = pd.to_datetime(df['Date'])
    if not df.empty:
        df = df.reset_index()
        df.plot(x='Date', y='OC', kind='line', title=file_name, grid=True)
        plt.savefig(f'./single_data/{file_name}.png', dpi=100)
        plt.close()
    return df
def arima_forecast(file_name):
    location = f'./single_data/{file_name}'
    series_orig = pd.read_csv(location)
    series = series_orig[['Date', 'OC']].set_index('Date')
    size = len(series)
    train = series.iloc[:size - nr_forecasting].values
    test = series.iloc[size - nr_forecasting:].values
    p, d, q = 4, 2, 1
    while True:
        try:
            model = ARIMA(train, order=(p, d, q))
            model_fit = model.fit(disp=0)
            predictions = model_fit.forecast(steps=len(test))[0].reshape(len(test), 1)
            break
        except Exception as e:
            print("ARIMA Error:", e)
            p = (p + 1) % 6
            if p == 0:
                d = (d + 1) % 6
                if d == 0:
                    q = (q + 1) % 6
    series['Predicted'] = np.nan
    series.iloc[-len(test):, 1:2] = predictions
    series['Title'] = file_name
    series['Expected_OC_perc'] = series_orig['OC'] / series_orig['Open']
    series['Predicted_OC_perc'] = series['Predicted'] / series_orig['Open']
    series = series.iloc[size - len(test):size]
    series.to_csv(f'test/{file_name}')
    plt.plot(test)
    plt.plot(predictions, color='red')
    plt.title(file_name)
    plt.legend(['Expected', 'Predicted'])
    plt.savefig(f'test/{file_name}.png')
    plt.close()
if __name__ == "__main__":
    file_names = [f for f in os.listdir("./data/") if f.endswith(".csv")]
    for file in file_names[:20]:
        process_single_file(file)
        plot_and_save(file)
        arima_forecast(file)
