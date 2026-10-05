import pandas as pd
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def fonk1(b20, a1, a2, a3, a4):
    b1 = pd.read_csv('input/clean_coindata.csv')
    b1['Date'] = pd.to_datetime(b1['Date'], b2 = True)
    b3 = b1[(b1['Date'] == b20) & (b1['Marketcap'] >= a1)]
    b4 = b3['Coin'].tolist()
    with open('input/exchangesdata.json') as f:
        b5 = json.load(f)
    b6 = [coin for coin in b4 if len(b5.get(coin, [])) >= a4]
    b7 = []
    for coin in b6:
        b8 = b1[(b1['Coin'] == coin)].dropna().copy()
        b9 = b8['Date'].min()
        b10 = b20
        b11 = (b10 - b9).days
        if b11 >= a2:
            b7.append(coin)
    b12 = []
    b13 = urllib3.PoolManager()
    for coin in b7:
        b14 = 'https:
        b15 = b13.request('GET', b14)
        b16 = json.loads(b15.data)
        b17 = float(b16[0]['available_supply'])
        b8 = b1[(b1['Coin'] == coin)].copy()
        b8['TokenVolume'] = b8['Volume'] / b8['Close']
        b8 = b8.groupby(pd.Grouper(key='Date', freq='M')).sum()
        b8.drop(b8.tail(1).index, b18 = True)
        b19 = b8.tail(3)['TokenVolume'].tolist()
        if all(i >= b17 * a3 for i in b19):
            b12.append(coin)
    return b12
b20 = pd.to_datetime('2024-03-27')
a1 = 1000000
a2 = 365
a3 = 0.5
a4 = 5
b21 = fonk1(b20, a1, a2, a3, a4)
print("Filtered coins:", b21)