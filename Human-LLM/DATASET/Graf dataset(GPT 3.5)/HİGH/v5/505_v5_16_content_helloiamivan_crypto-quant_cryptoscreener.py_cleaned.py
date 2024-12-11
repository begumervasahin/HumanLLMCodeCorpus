import pandas as pd
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def fonk1(filepath):
    return pd.read_csv(filepath)
def fonk2(df, column):
    df[column] = pd.to_datetime(df[column], b1 = True)
    return df
def fonk3(df, date, min_market_cap):
    return df[(df['Date'] == date) & (df['Marketcap'] >= min_market_cap)]['Coin'].tolist()
def fonk4(coins, b13, min_exchanges):
    return [coin for coin in coins if len(b13[coin]) >= min_exchanges]
def fonk5(coins, df, date, min_listing_period):
    b2 = []
    for coin in coins:
        b3 = df[df['Coin'] == coin].dropna().copy()
        b4 = b3['Date'].min()
        if (date - b4).days >= min_listing_period:
            b2.append(coin)
    return b2
def fonk6(coins, df, circulating_pct):
    b2 = []
    b5 = urllib3.PoolManager()
    for coin in coins:
        b6 = f'https:
        b7 = b5.request('GET', b6)
        b8 = json.loads(b7.data)
        b9 = float(b8[0]['available_supply'])
        b3 = df[df['Coin'] == coin].copy()
        b3['TokenVolume'] = b3['Volume'] / b3['Close']
        b3 = b3.groupby(pd.Grouper(key='Date', freq='M')).sum()
        b3.drop(b3.tail(1).index, b10 = True)
        b11 = b3.tail(3)['TokenVolume'].tolist()
        if all(volume >= b9 * circulating_pct for volume in b11):
            b2.append(coin)
    return b2
def fonk7(universe_selection_date, min_market_cap, min_listing_period, circulating_pct, min_exchanges):
    b12 = fonk1('input/clean_coindata.csv')
    b12 = fonk2(b12, 'Date')
    b2 = fonk3(b12, universe_selection_date, min_market_cap)
    b13 = json.load(open('input/exchangesdata.json'))
    b2 = fonk4(b2, b13, min_exchanges)
    b2 = fonk5(b2, b12, universe_selection_date, min_listing_period)
    b2 = fonk6(b2, b12, circulating_pct)
    return b2