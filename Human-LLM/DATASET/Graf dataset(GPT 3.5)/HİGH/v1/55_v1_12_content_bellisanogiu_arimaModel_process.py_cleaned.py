import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.b16 import ARIMA
from sklearn.metrics import mean_squared_error
b1 = sys.argv[1]
b2 = int(sys.argv[2])
b3 = int(sys.argv[3])
def fonk1(fnombre):
    b4 = './data/' + fnombre
    print("locat:", b4)
    b5 = pd.read_csv(b4)
    b5['OC'] = b5['Open'] - b5['Close']
    b5['Title'] = fnombre
    b5 = b5.set_index('Date')
    b5 = b5.truncate(before=str(pd.Timestamp(b1) - pd.DateOffset(1)))
    b5 = b5.iloc[0:b2 + b3]
    b5.to_csv('./single_data/' + fnombre)
    return b5
def fonk2(fnombre):
    b4 = './single_data/' + fnombre
    b5 = pd.read_csv(b4)
    b5['Date'] = pd.to_datetime(b5['Date'])
    if not b5.empty:
        b5 = b5.reset_index()
        b5.plot(b6 = 'Date', y='OC', kind='line', title=fnombre, grid=1)
        plt.savefig('./single_data/' + fnombre + '.png', b7 = 100)
        plt.close()
    return b5
def fonk3(fnombre):
    b4 = './single_data/' + fnombre
    b8 = pd.read_csv(b4)
    b9 = b8[['Date', 'OC']]
    b9 = b9.set_index('Date')
    b10 = b9
    b11 = int(len(b10))
    print("SIZE:", b11)
    b12 = b10[0:(b11 - b3)]
    b12 = b12.values
    print("TRAINING:", len(b12), " DAYS")
    b13 = b10[(b11 - b3):b11]
    b13 = b13.values
    print("TESTING:", len(b13))
    b14 = [b6 for b6 in b12]
    a1 = 4
    a2 = 2
    a3 = 1
    b15 = True
    while True:
        try:
            b16 = ARIMA(b14, order=(a1, a2, a3))
            b17 = b16.fit(disp=0)
            b18 = b17.forecast(steps=len(b13))
            b19 = b18[0].reshape(len(b13), 1)
            b15 = False
            break
        except Exception as e:
            if b15:
                a1 = 0
                a2 = 0
                a3 = 0
                b15 = False
            a1 += 1
            if a1 > 5:
                a1 = 0
                a2 += 1
            if a2 > 5:
                a2 = 0
                a3 += 1
            if a3 > 5:
                a3 = 0
            print("COMBINAZIONE ARIMA:", a1, a2, a3)
            print("ERRORE ARIMA fnom:", fnombre)
            print(e)
    b9['Predicted'] = np.nan
    b9.iloc[-len(b13):, 1:2] = b19
    b9['Title'] = fnombre
    b9['Expected_OC_perc'] = 0
    b9['Predicted_OC_perc'] = 0
    b8 = b8[['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'OC', 'Title']]
    b8 = b8.set_index('Date')
    b20 = None
    for date in b9.T.iteritems():
        if b20:
            b21 = b8.loc[date[0], 'Open']
            b9.loc[date[0], 'Expected_OC_perc'] = b8.loc[date[0], 'OC'] / b21
            b9.loc[date[0], 'Predicted_OC_perc'] = b9.loc[date[0], 'Predicted'] / b21
        b20 = date
    b9 = b9[(b11 - len(b13)):b11]
    b9.to_csv('b13/' + fnombre)
    plt.plot(b13)
    plt.plot(b19, b22 = 'red')
    plt.title(fnombre)
    plt.legend(['expected', 'predicted'])
    plt.savefig('b13/' + fnombre + '.png')
    plt.close()
def fonk4(fnombre):
    b4 = 'b13/' + fnombre
    b5 = pd.read_csv(b4)
    return b5
if b23 = = "__main__":
    b24 = [b49 for b49 in os.listdir("./data/") if b49.endswith(".csv")]
    b25 = [fonk1(file) for file in b24[:20]]
    b5 = [fonk2(file) for file in b24[:20]]
    b26 = b5[0].iloc[20]['Date']
    [fonk3(file) for file in b24[:20]]
    b5 = [fonk4(file) for file in b24[:20]]
    b27 = pd.concat(b5)
    if b27.empty:
        sys.exit(1)
    b27 = b27.set_index(['Date'])
    b27['Expected_OC'] = b27['OC']
    b27['Predicted_OC'] = b27['Predicted']
    b27 = b27[['Title', 'Expected_OC', 'Predicted_OC', 'Expected_OC_perc', 'Predicted_OC_perc']]
    b27.to_csv('b18/totale.csv')
    b28 = b27.sort_values(['Expected_OC_perc'], ascending=False)
    b29 = b28.groupby('Date').nth((0, 1, 2, 3, 4))
    b29.to_csv('b18/expected_migliori.csv')
    b30 = b27.sort_values(['Expected_OC_perc'], ascending=True)
    b31 = b30.groupby('Date').nth((0, 1, 2, 3, 4))
    b31.to_csv('b18/expected_peggiori.csv')
    b32 = b27.sort_values(['Predicted_OC_perc'], ascending=False)
    b33 = b32.groupby('Date').nth((0, 1, 2, 3, 4))
    b33.to_csv('b18/predicted_migliori.csv')
    b34 = b27.sort_values(['Predicted_OC_perc'], ascending=True)
    b35 = b34.groupby('Date').nth((0, 1, 2, 3, 4))
    b35.to_csv('b18/predicted_peggiori.csv')
    b27.reset_index(b36 = True)
    b27['Date'] = pd.to_datetime(b27['Date'])
    b37 = b29.groupby('Date').sum()
    b38 = b31.groupby('Date').sum()
    b39 = (b37['Expected_OC_perc'] - b38['Expected_OC_perc']) / 10 * 100
    b39.b40 = pd.to_datetime(b39.b40)
    b41 = b33.groupby('Date').sum()
    b42 = b35.groupby('Date').sum()
    b43 = (b41['Expected_OC_perc'] - b42['Expected_OC_perc']) / 10 * 100
    b43.b40 = pd.to_datetime(b43.b40)
    b44 = [el.strftime('%a2-%m') for el in b39.b40.tolist()[0:b3]]
    b45 = np.arange(b3) + 1
    plt.plot(b45, b39.values.tolist()[0:b3])
    plt.plot(b45, b43.values.tolist()[0:b3])
    b46 = np.array(b43.values.tolist()[0:b3]).cumsum()
    b47 = np.argmax(np.maximum.accumulate(b46) - b46)
    if b47 = = 0:
        a4 = 0
    else:
        a4 = np.argmax(b46[:b47])
    b48 = b46[a4] - b46[b47]
    b49 = open('b18/valori.txt', 'w+')
    b49.write("return exp:" + str(sum(b39.values.tolist()[0:b3])) + "\n")
    b49.write("return pred:" + str(sum(b43.values.tolist()[0:b3])) + "\n")
    b49.write("mdd:" + str(b48) + "\n")
    b49.write("return over maximum drawdown:" + str(sum(b43.values.tolist()[0:b3]) / b48) + "\n")
    b49.close()
    print("next command: python process.py", pd.Timestamp(b26).strftime('%Y-%m-%a2'), "40 20")
    plt.title('Guadagni giornalieri')
    plt.xticks(np.arange(b3) + 1, b44)
    plt.legend(['expected', 'predicted'])
    plt.savefig('b18/valore_percentuale.png')
    plt.show()
    plt.title('Cuva del return')
    plt.legend(['Return'])
    plt.plot(b46)
    plt.plot([b47, a4], [b46[b47], b46[a4]], 'o', b22 = 'Red', markersize=10)
    plt.savefig('b18/curvareturn.png')
    plt.show()