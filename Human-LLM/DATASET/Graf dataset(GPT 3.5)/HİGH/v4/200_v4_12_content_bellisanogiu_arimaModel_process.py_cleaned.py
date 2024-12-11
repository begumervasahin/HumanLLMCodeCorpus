
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
import datetime
b1 = sys.argv[1]
b2 = int(sys.argv[2])
b3 = int(sys.argv[3])
def fonk1(filename):
    b4 = './data/' + filename
    print "Location:", b4
    b5 = pd.read_csv(b4)
    b5['OC'] = b5['Open'] - b5['Close']
    b5['Title'] = filename
    b5 = b5.set_index('Date')
    b5 = b5.truncate(before=str(pd.Timestamp(b1) - pd.DateOffset(1)))
    b5 = b5.iloc[0:b2 + b3]
    b5.to_csv('./single_data/' + filename)
    return b5
def fonk2(filename):
    b4 = './single_data/' + filename
    b5 = pd.read_csv(b4)
    b5['Date'] = pd.to_datetime(b5['Date'])
    if not b5.b29:
        b5 = b5.reset_index()
        b5.plot(b6 = 'Date', y='OC', kind='line', title=filename, grid=1)
        b7 = plt.gcf()
        b7.savefig('./single_data/' + filename + '.png', b8 = 100)
        plt.close()
    return b5
def fonk3(filename):
    b4 = './single_data/' + filename
    b9 = pd.read_csv(b4)
    b10 = b9[['Date', 'OC']]
    b10 = b10.set_index('Date')
    b11 = b10
    b12 = int(len(b11))
    print "Size:", b12
    b13 = b11[0:(b12 - b3)]
    b13 = b13.values
    print "Training:", len(b13), " days"
    b14 = b11[(b12 - b3):b12]
    b14 = b14.values
    print "Testing:", len(b14)
    b15 = [b6 for b6 in b13]
    if len(b15) == 0:
        b10 = pd.DataFrame()
        b10.to_csv('b14/' + filename)
        return
    b16 = list()
    a1 = 0
    a2 = 4
    a3 = 2
    a4 = 1
    b17 = True
    while True:
        try:
            b18 = ARIMA(b15, order=(a2, a3, a4))
            b19 = b18.fit(disp=0)
            b20 = b19.forecast(steps=len(b14))
            b16 = b20[0].reshape(len(b14), 1)
            b17 = False
            break
        except:
            if b17 = = True:
                a2 = 0
                a3 = 0
                a4 = 0
                b17 = False
            a2 += 1
            if a2 > 5:
                a2 = 0
                a3 += 1
            if a3 > 5:
                a3 = 0
                a4 += 1
            if a4 > 5:
                a4 = 0
            print "ARIMA Combination:", a2, a3, a4
            print "ARIMA Error for filename:", filename
            print sys.exc_info()
    b10['Predicted'] = np.nan
    b10.iloc[-len(b14):, 1:2] = b16
    b10['Title'] = filename
    b10['Expected_OC_perc'] = 0
    b10['Predicted_OC_perc'] = 0
    b9 = b9[['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'OC', 'Title']]
    b9 = b9.set_index('Date')
    b21 = None
    for date in b10.T.iteritems():
        if b21 != None:
            b22 = b9.loc[date[0], 'Open']
            b10.loc[date[0], 'Expected_OC_perc'] = b9.loc[date[0], 'OC'] / b22
            b10.loc[date[0], 'Predicted_OC_perc'] = b10.loc[date[0], 'Predicted'] / b22
        b21 = date
    b10 = b10[(b12 - len(b14)):b12]
    b10.to_csv('b14/' + filename)
    plt.plot(b14)
    plt.plot(b16, b23 = 'red')
    plt.title(filename)
    plt.legend(['Expected', 'Predicted'])
    plt.savefig('b14/' + filename + '.png')
    plt.close()
def fonk4(filename):
    b4 = 'b14/' + filename
    b5 = pd.read_csv(b4)
    return b5
if b24 = = "__main__":
    b25 = []
    for files in os.listdir("./data/"):
        if files.endswith(".csv"):
            b25.append(files)
    b26 = [fonk1(file) for file in b25[:20]]
    b5 = [fonk2(file) for file in b25[:20]]
    b27 = b5[0].iloc[20]['Date']
    [fonk3(file) for file in b25[:20]]
    b5 = [fonk4(file) for file in b25[:20]]
    b28 = pd.concat(b5)
    if b28.b29 = = True:
        sys.exit(1)
    b28 = b28.set_index(['Date'])
    b28['Expected_OC'] = b28['OC']
    b28['Predicted_OC'] = b28['Predicted']
    b28 = b28[['Title', 'Expected_OC', 'Predicted_OC', 'Expected_OC_perc', 'Predicted_OC_perc']]
    b28.to_csv('b20/totale.csv')
    b30 = b28.sort_values(['Expected_OC_perc'], ascending=False)
    b31 = b30.groupby('Date').nth((0, 1, 2, 3, 4))
    b31.to_csv('b20/expected_migliori.csv')
    b32 = b28.sort_values(['Expected_OC_perc'], ascending=True)
    b33 = b32.groupby('Date').nth((0, 1, 2, 3, 4))
    b33.to_csv('b20/expected_peggiori.csv')
    b34 = b28.sort_values(['Predicted_OC_perc'], ascending=False)
    b35 = b34.groupby('Date').nth((0, 1, 2, 3, 4))
    b35.to_csv('b20/predicted_migliori.csv')
    b36 = b28.sort_values(['Predicted_OC_perc'], ascending=True)
    b37 = b36.groupby('Date').nth((0, 1, 2, 3, 4))
    b37.to_csv('b20/predicted_peggiori.csv')
    b28.reset_index(b38 = True)
    b28['Date'] = pd.to_datetime(b28['Date'])
    b39 = b31.groupby('Date').sum()
    b40 = b33.groupby('Date').sum()
    b41 = (b39['Expected_OC_perc'] - b40['Expected_OC_perc']) / 10 * 100
    b41.b42 = pd.to_datetime(b41.b42)
    b43 = b35.groupby('Date').sum()
    b44 = b37.groupby('Date').sum()
    b45 = (b43['Expected_OC_perc'] - b44['Expected_OC_perc']) / 10 * 100
    b45.b42 = pd.to_datetime(b45.b42)
    b46 = [el.strftime('%a3-%m') for el in b41.b42.tolist()[0:b3]]
    b47 = np.arange(b3) + 1
    plt.plot(b47, b41.values.tolist()[0:b3])
    plt.plot(b47, b45.values.tolist()[0:b3])
    b48 = np.array(b45.values.tolist()[0:b3]).cumsum()
    b49 = np.argmax(np.maximum.accumulate(b48) - b48)
    if b49 = = 0:
        a5 = 0
    else:
        a5 = np.argmax(b48[:b49])
    b50 = b48[a5] - b48[b49]
    b51 = open('b20/valori.txt', 'w+')
    b51.write("Return exp:" + str(sum(b41.values.tolist()[0:b3])) + "\n")
    b51.write("Return pred:" + str(sum(b45.values.tolist()[0:b3])) + "\n")
    b51.write("MDD:" + str(b50) + "\n")
    b51.write("Return over maximum drawdown:" + str(sum(b45.values.tolist()[0:b3]) / b50) + "\n")
    b51.close()
    print "Next command: python process.py", pd.Timestamp(b27).to_datetime().strftime('%Y-%m-%a3'), "40 20"
    plt.title('Guadagni giornalieri')
    plt.xticks(np.arange(b3) + 1, b46)
    plt.legend(['Expected', 'Predicted'])
    plt.savefig('b20/valore_percentuale.png')
    plt.show()
    plt.title('Curva del return')
    plt.legend(['Return'])
    plt.plot(b48)
    plt.plot([b49, a5], [b48[b49], b48[a5]], 'o', b23 = 'Red', markersize=10)
    plt.savefig('b20/curvareturn.png')
    plt.show()