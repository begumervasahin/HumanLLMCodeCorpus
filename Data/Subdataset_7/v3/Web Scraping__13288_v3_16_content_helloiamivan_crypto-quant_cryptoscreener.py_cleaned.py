import pandas as pd
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def fonk1(file_path):
    b1 = pd.read_csv(file_path)
    b1['Date'] = pd.to_datetime(b1['Date'], b2 = True)
    return b1
def fonk2(b1, selection_date, a1):
    b3 = b1[(b1['Date'] == selection_date) & (b1['Marketcap'] >= a1)]
    return b3['Coin'].tolist()
def fonk3(file_path):
    with open(file_path) as f:
        b4 = json.load(f)
    return b4
def fonk4(b18, b4, a4):
    return [coin for coin in b18 if len(b4.get(coin, [])) >= a4]
def fonk5(b1, b18, selection_date, a2):
    b5 = []
    for coin in b18:
        b6 = b1[(b1['Coin'] == coin)].dropna().copy()
        b7 = b6['Date'].min()
        b8 = (selection_date - b7).days
        if b8 >= a2:
            b5.append(coin)
    return b5
def fonk6(b1, b18, a3):
    b9 = []
    b10 = urllib3.PoolManager()
    for coin in b18:
        b11 = 'https:
        b12 = b10.request('GET', b11)
        b13 = json.loads(b12.data)
        b14 = float(b13[0]['available_supply'])
        b6 = b1[(b1['Coin'] == coin)].copy()
        b6['TokenVolume'] = b6['Volume'] / b6['Close']
        b6 = b6.groupby(pd.Grouper(key='Date', freq='M')).sum()
        b6.drop(b6.tail(1).index, b15 = True)
        b16 = b6.tail(3)['TokenVolume'].tolist()
        if all(vol >= b14 * a3 for vol in b16):
            b9.append(coin)
    return b9
def fonk7(b19, a1, a2, a3, a4,
                    b17 = 'input/clean_coindata.csv', exchange_data_file='input/exchangesdata.json'):
    b1 = fonk1(b17)
    b18 = fonk2(b1, b19, a1)
    b4 = fonk3(exchange_data_file)
    b18 = fonk4(b18, b4, a4)
    b18 = fonk5(b1, b18, b19, a2)
    b18 = fonk6(b1, b18, a3)
    return b18
b19 = pd.to_datetime('2024-03-27')
a1 = 1000000
a2 = 365
a3 = 0.5
a4 = 5
b20 = fonk7(b19, a1, a2, a3, a4)
print("Filtered coins:", b20)