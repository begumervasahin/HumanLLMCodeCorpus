
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
import datetime
start_date = sys.argv[1]
days_training = int(sys.argv[2])
nr_forecasting = int(sys.argv[3])
def GetFile(filename):
    location = './data/' + filename
    print "Location:", location
    df = pd.read_csv(location)
    df['OC'] = df['Open'] - df['Close']
    df['Title'] = filename
    df = df.set_index('Date')
    df = df.truncate(before=str(pd.Timestamp(start_date) - pd.DateOffset(1)))
    df = df.iloc[0:days_training + nr_forecasting]
    df.to_csv('./single_data/' + filename)
    return df
def PlotFile(filename):
    location = './single_data/' + filename
    df = pd.read_csv(location)
    df['Date'] = pd.to_datetime(df['Date'])
    if not df.empty:
        df = df.reset_index()
        df.plot(x='Date', y='OC', kind='line', title=filename, grid=1)
        fig = plt.gcf()
        fig.savefig('./single_data/' + filename + '.png', dpi=100)
        plt.close()
    return df
def ArimaSingleFile(filename):
    location = './single_data/' + filename
    seriesOrig = pd.read_csv(location)
    series = seriesOrig[['Date', 'OC']]
    series = series.set_index('Date')
    X = series
    size = int(len(X))
    print "Size:", size
    train = X[0:(size - nr_forecasting)]
    train = train.values
    print "Training:", len(train), " days"
    test = X[(size - nr_forecasting):size]
    test = test.values
    print "Testing:", len(test)
    history = [x for x in train]
    if len(history) == 0:
        series = pd.DataFrame()
        series.to_csv('test/' + filename)
        return
    predictions = list()
    cont = 0
    p = 4
    d = 2
    q = 1
    error_flag = True
    while True:
        try:
            model = ARIMA(history, order=(p, d, q))
            model_fit = model.fit(disp=0)
            output = model_fit.forecast(steps=len(test))
            predictions = output[0].reshape(len(test), 1)
            error_flag = False
            break
        except:
            if error_flag == True:
                p = 0
                d = 0
                q = 0
                error_flag = False
            p += 1
            if p > 5:
                p = 0
                d += 1
            if d > 5:
                d = 0
                q += 1
            if q > 5:
                q = 0
            print "ARIMA Combination:", p, d, q
            print "ARIMA Error for filename:", filename
            print sys.exc_info()
    series['Predicted'] = np.nan
    series.iloc[-len(test):, 1:2] = predictions
    series['Title'] = filename
    series['Expected_OC_perc'] = 0
    series['Predicted_OC_perc'] = 0
    seriesOrig = seriesOrig[['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'OC', 'Title']]
    seriesOrig = seriesOrig.set_index('Date')
    previous = None
    for date in series.T.iteritems():
        if previous != None:
            denominator = seriesOrig.loc[date[0], 'Open']
            series.loc[date[0], 'Expected_OC_perc'] = seriesOrig.loc[date[0], 'OC'] / denominator
            series.loc[date[0], 'Predicted_OC_perc'] = series.loc[date[0], 'Predicted'] / denominator
        previous = date
    series = series[(size - len(test)):size]
    series.to_csv('test/' + filename)
    plt.plot(test)
    plt.plot(predictions, color='red')
    plt.title(filename)
    plt.legend(['Expected', 'Predicted'])
    plt.savefig('test/' + filename + '.png')
    plt.close()
def GetArimaSingleFile(filename):
    location = 'test/' + filename
    df = pd.read_csv(location)
    return df
if __name__ == "__main__":
    FileNames = []
    for files in os.listdir("./data/"):
        if files.endswith(".csv"):
            FileNames.append(files)
    listFiles = [GetFile(file) for file in FileNames[:20]]
    df = [PlotFile(file) for file in FileNames[:20]]
    nextdate = df[0].iloc[20]['Date']
    [ArimaSingleFile(file) for file in FileNames[:20]]
    df = [GetArimaSingleFile(file) for file in FileNames[:20]]
    dftot = pd.concat(df)
    if dftot.empty == True:
        sys.exit(1)
    dftot = dftot.set_index(['Date'])
    dftot['Expected_OC'] = dftot['OC']
    dftot['Predicted_OC'] = dftot['Predicted']
    dftot = dftot[['Title', 'Expected_OC', 'Predicted_OC', 'Expected_OC_perc', 'Predicted_OC_perc']]
    dftot.to_csv('output/totale.csv')
    dftot_1 = dftot.sort_values(['Expected_OC_perc'], ascending=False)
    migliori_exp = dftot_1.groupby('Date').nth((0, 1, 2, 3, 4))
    migliori_exp.to_csv('output/expected_migliori.csv')
    dftot_2 = dftot.sort_values(['Expected_OC_perc'], ascending=True)
    peggiori_exp = dftot_2.groupby('Date').nth((0, 1, 2, 3, 4))
    peggiori_exp.to_csv('output/expected_peggiori.csv')
    dftot_3 = dftot.sort_values(['Predicted_OC_perc'], ascending=False)
    migliori_pred = dftot_3.groupby('Date').nth((0, 1, 2, 3, 4))
    migliori_pred.to_csv('output/predicted_migliori.csv')
    dftot_4 = dftot.sort_values(['Predicted_OC_perc'], ascending=True)
    peggiori_pred = dftot_4.groupby('Date').nth((0, 1, 2, 3, 4))
    peggiori_pred.to_csv('output/predicted_peggiori.csv')
    dftot.reset_index(inplace=True)
    dftot['Date'] = pd.to_datetime(dftot['Date'])
    incr_bydate_exp = migliori_exp.groupby('Date').sum()
    decr_bydate_exp = peggiori_exp.groupby('Date').sum()
    valore_giornaliero_exp = (incr_bydate_exp['Expected_OC_perc'] - decr_bydate_exp['Expected_OC_perc']) / 10 * 100
    valore_giornaliero_exp.index = pd.to_datetime(valore_giornaliero_exp.index)
    incr_bydate_pred = migliori_pred.groupby('Date').sum()
    decr_bydate_pred = peggiori_pred.groupby('Date').sum()
    valore_giornaliero_pred = (incr_bydate_pred['Expected_OC_perc'] - decr_bydate_pred['Expected_OC_perc']) / 10 * 100
    valore_giornaliero_pred.index = pd.to_datetime(valore_giornaliero_pred.index)
    x_labstr = [el.strftime('%d-%m') for el in valore_giornaliero_exp.index.tolist()[0:nr_forecasting]]
    x_lab = np.arange(nr_forecasting) + 1
    plt.plot(x_lab, valore_giornaliero_exp.values.tolist()[0:nr_forecasting])
    plt.plot(x_lab, valore_giornaliero_pred.values.tolist()[0:nr_forecasting])
    xspred = np.array(valore_giornaliero_pred.values.tolist()[0:nr_forecasting]).cumsum()
    ipred = np.argmax(np.maximum.accumulate(xspred) - xspred)
    if ipred == 0:
        jpred = 0
    else:
        jpred = np.argmax(xspred[:ipred])
    mddpred = xspred[jpred] - xspred[ipred]
    f = open('output/valori.txt', 'w+')
    f.write("Return exp:" + str(sum(valore_giornaliero_exp.values.tolist()[0:nr_forecasting])) + "\n")
    f.write("Return pred:" + str(sum(valore_giornaliero_pred.values.tolist()[0:nr_forecasting])) + "\n")
    f.write("MDD:" + str(mddpred) + "\n")
    f.write("Return over maximum drawdown:" + str(sum(valore_giornaliero_pred.values.tolist()[0:nr_forecasting]) / mddpred) + "\n")
    f.close()
    print "Next command: python process.py", pd.Timestamp(nextdate).to_datetime().strftime('%Y-%m-%d'), "40 20"
    plt.title('Guadagni giornalieri')
    plt.xticks(np.arange(nr_forecasting) + 1, x_labstr)
    plt.legend(['Expected', 'Predicted'])
    plt.savefig('output/valore_percentuale.png')
    plt.show()
    plt.title('Curva del return')
    plt.legend(['Return'])
    plt.plot(xspred)
    plt.plot([ipred, jpred], [xspred[ipred], xspred[jpred]], 'o', color='Red', markersize=10)
    plt.savefig('output/curvareturn.png')
    plt.show()