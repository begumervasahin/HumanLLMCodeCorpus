import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.b15 import ARIMA
from sklearn.metrics import mean_squared_error
b1 = sys.argv[1]
b2 = int(sys.argv[2])
b3 = int(sys.argv[3])
def fonk1(file_name):
    b4 = f'./data/{file_name}'
    print(f"Processing file: {b4}")
    b5 = pd.read_csv(b4)
    b5['OC'] = b5['Open'] - b5['Close']
    b5['Title'] = file_name
    b5 = b5.set_index('Date')
    b5 = b5.truncate(before=str(pd.Timestamp(b1) - pd.DateOffset(1)))
    b5 = b5.iloc[:b2 + b3]
    b5.to_csv(f'./single_data/{file_name}')
    return b5
def fonk2(file_name):
    b6 = f'./single_data/{file_name}'
    b5 = pd.read_csv(b6)
    b5['Date'] = pd.to_datetime(b5['Date'])
    if not b5.empty:
        b5 = b5.reset_index()
        b5.plot(b7 = 'Date', y='OC', kind='line', title=file_name, grid=True)
        plt.savefig(f'./single_data/{file_name}.png', b8 = 100)
        plt.close()
    return b5
def fonk3(file_name):
    b6 = f'./single_data/{file_name}'
    b9 = pd.read_csv(b6)
    b10 = b9[['Date', 'OC']].set_index('Date')
    b11 = len(b10)
    b12 = b10.iloc[:b11 - b3].values
    b13 = b10.iloc[b11 - b3:].values
    b18, b19, b14 = 4, 2, 1
    while True:
        try:
            b15 = ARIMA(b12, order=(b18, b19, b14))
            b16 = b15.fit(disp=0)
            b17 = b16.forecast(steps=len(b13))[0].reshape(len(b13), 1)
            break
        except Exception as e:
            print("ARIMA Error:", e)
            b18 = (b18 + 1) % 6
            if b18 = = 0:
                b19 = (b19 + 1) % 6
                if b19 = = 0:
                    b14 = (b14 + 1) % 6
    b10['Predicted'] = np.nan
    b10.iloc[-len(b13):, 1:2] = b17
    b10['Title'] = file_name
    b10['Expected_OC_perc'] = b9['OC'] / b9['Open']
    b10['Predicted_OC_perc'] = b10['Predicted'] / b9['Open']
    b10 = b10.iloc[b11 - len(b13):b11]
    b10.to_csv(f'b13/{file_name}')
    plt.plot(b13)
    plt.plot(b17, b20 = 'red')
    plt.title(file_name)
    plt.legend(['Expected', 'Predicted'])
    plt.savefig(f'b13/{file_name}.png')
    plt.close()
if b21 = = "__main__":
    b22 = [f for f in os.listdir("./data/") if f.endswith(".csv")]
    for file in b22[:20]:
        fonk1(file)
        fonk2(file)
        fonk3(file)
