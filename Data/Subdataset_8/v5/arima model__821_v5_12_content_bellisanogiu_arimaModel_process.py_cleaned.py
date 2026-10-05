import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA
import datetime
start_date = sys.argv[1]
days_training = int(sys.argv[2])
nr_forecasting = int(sys.argv[3])
def preprocess_data(filename):
    location = f'./data/{filename}'
    print("Reading data from:", location)
    df = pd.read_csv(location)
    df['OC'] = df['Open'] - df['Close']
    df['Title'] = filename
    df = df.set_index('Date')
    df = df.truncate(before=str(pd.Timestamp(start_date) - pd.DateOffset(1)))
    df = df.iloc[0:days_training + nr_forecasting]
    df.to_csv(f'./single_data/{filename}')
    return df
def plot_data(filename):
    location = f'./single_data/{filename}'
    df = pd.read_csv(location)
    df['Date'] = pd.to_datetime(df['Date'])
    if not df.empty:
        df = df.reset_index()
        df.plot(x='Date', y='OC', kind='line', title=filename, grid=1)
        plt.savefig(f'./single_data/{filename}.png', dpi=100)
        plt.close()
    return df
def perform_arima_forecasting(filename):
    location = f'./single_data/{filename}'
    seriesOrig = pd.read_csv(location)
    series = seriesOrig[['Date', 'OC']].set_index('Date')
    size = len(series)
    print("Size:", size)
    train = series.iloc[0:(size - nr_forecasting)].values
    test = series.iloc[(size - nr_forecasting):size].values
    print("Training:", len(train), " days")
    print("Testing:", len(test))
    history = [x for x in train]
    p = 4
    d = 2
    q = 1
    while True:
        try:
            model = ARIMA(history, order=(p, d, q))
            model_fit = model.fit(disp=0)
            output = model_fit.forecast(steps=len(test))
            predictions = output[0].reshape(len(test), 1)
            break
        except:
            p = (p + 1) % 6
            if p == 0:
                d = (d + 1) % 6
                if d == 0:
                    q = (q + 1) % 6
            print("ARIMA Combination:", p, d, q)
            print("ARIMA Error for filename:", filename)
            print(sys.exc_info())
    series['Predicted'] = np.nan
    series.iloc[-len(test):, 1:2] = predictions
    series['Title'] = filename
    series['Expected_OC_perc'] = 0
    series['Predicted_OC_perc'] = 0
    for date, oc_value in series.T.iteritems():
        if history:
            denominator = seriesOrig.loc[date, 'Open']
            series.loc[date, 'Expected_OC_perc'] = seriesOrig.loc[date, 'OC'] / denominator
            series.loc[date, 'Predicted_OC_perc'] = oc_value / denominator
    series = series[(size - len(test)):size]
    series.to_csv(f'test/{filename}')
    plt.plot(test)
    plt.plot(predictions, color='red')
    plt.title(filename)
    plt.legend(['Expected', 'Predicted'])
    plt.savefig(f'test/{filename}.png')
    plt.close()
def get_arima_results(filename):
    location = f'test/{filename}'
    df = pd.read_csv(location)
    return df
if __name__ == "__main__":
    FileNames = [file for file in os.listdir("./data/") if file.endswith(".csv")]
    for filename in FileNames[:20]:
        preprocess_data(filename)
        plot_data(filename)
    nextdate = plot_data(FileNames[0]).iloc[20]['Date']
    for filename in FileNames[:20]:
        perform_arima_forecasting(filename)
    df = [get_arima_results(filename) for filename in FileNames[:20]]
    dftot = pd.concat(df)
    if dftot.empty:
        sys.exit(1)
