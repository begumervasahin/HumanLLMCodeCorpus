import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA
import datetime
b1 = sys.argv[1]
b2 = int(sys.argv[2])
b3 = int(sys.argv[3])
def fonk1(filename):
    b4 = f'./data/{filename}'
    print("Reading data from:", b4)
    b5 = pd.read_csv(b4)
    b5['OC'] = b5['Open'] - b5['Close']
    b5['Title'] = filename
    b5 = b5.set_index('Date')
    b5 = b5.truncate(before=str(pd.Timestamp(b1) - pd.DateOffset(1)))
    b5 = b5.iloc[0:b2 + b3]
    b5.to_csv(f'./single_data/{filename}')
    return b5
def fonk2(filename):
    b4 = f'./single_data/{filename}'
    b5 = pd.read_csv(b4)
    b5['Date'] = pd.to_datetime(b5['Date'])
    if not b5.empty:
        b5 = b5.reset_index()
        b5.plot(b6 = 'Date', y='OC', kind='line', title=filename, grid=1)
        plt.savefig(f'./single_data/{filename}.png', b7 = 100)
        plt.close()
    return b5
def fonk3(filename):
    b4 = f'./single_data/{filename}'
    b8 = pd.read_csv(b4)
    b9 = b8[['Date', 'OC']].set_index('Date')
    b10 = len(b9)
    print("Size:", b10)
    b11 = b9.iloc[0:(b10 - b3)].values
    b12 = b9.iloc[(b10 - b3):b10].values
    print("Training:", len(b11), " days")
    print("Testing:", len(b12))
    b13 = [b6 for b6 in b11]
    a1 = 4
    a2 = 2
    a3 = 1
    while True:
        try:
            b14 = ARIMA(b13, order=(a1, a2, a3))
            b15 = b14.fit(disp=0)
            b16 = b15.forecast(steps=len(b12))
            b17 = b16[0].reshape(len(b12), 1)
            break
        except:
            a1 = (a1 + 1) % 6
            if a1 = = 0:
                a2 = (a2 + 1) % 6
                if a2 = = 0:
                    a3 = (a3 + 1) % 6
            print("ARIMA Combination:", a1, a2, a3)
            print("ARIMA Error for filename:", filename)
            print(sys.exc_info())
    b9['Predicted'] = np.nan
    b9.iloc[-len(b12):, 1:2] = b17
    b9['Title'] = filename
    b9['Expected_OC_perc'] = 0
    b9['Predicted_OC_perc'] = 0
    for date, oc_value in b9.T.iteritems():
        if b13:
            b18 = b8.loc[date, 'Open']
            b9.loc[date, 'Expected_OC_perc'] = b8.loc[date, 'OC'] / b18
            b9.loc[date, 'Predicted_OC_perc'] = oc_value / b18
    b9 = b9[(b10 - len(b12)):b10]
    b9.to_csv(f'b12/{filename}')
    plt.plot(b12)
    plt.plot(b17, b19 = 'red')
    plt.title(filename)
    plt.legend(['Expected', 'Predicted'])
    plt.savefig(f'b12/{filename}.png')
    plt.close()
def fonk4(filename):
    b4 = f'b12/{filename}'
    b5 = pd.read_csv(b4)
    return b5
if b20 = = "__main__":
    b21 = [file for file in os.listdir("./data/") if file.endswith(".csv")]
    for filename in b21[:20]:
        fonk1(filename)
        fonk2(filename)
    b22 = fonk2(b21[0]).iloc[20]['Date']
    for filename in b21[:20]:
        fonk3(filename)
    b5 = [fonk4(filename) for filename in b21[:20]]
    b23 = pd.concat(b5)
    if b23.empty:
        sys.exit(1)
