import pandas as pd
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def load_coin_data(filepath):
    return pd.read_csv(filepath)
def convert_to_datetime(df, column):
    df[column] = pd.to_datetime(df[column], infer_datetime_format=True)
    return df
def filter_coins_by_date_and_market_cap(df, date, min_market_cap):
    return df[(df['Date'] == date) & (df['Marketcap'] >= min_market_cap)]['Coin'].tolist()
def filter_coins_by_exchanges(coins, exchanges_data, min_exchanges):
    return [coin for coin in coins if len(exchanges_data[coin]) >= min_exchanges]
def filter_coins_by_listing_period(coins, df, date, min_listing_period):
    filtered_coins = []
    for coin in coins:
        coin_data = df[df['Coin'] == coin].dropna().copy()
        start_date = coin_data['Date'].min()
        if (date - start_date).days >= min_listing_period:
            filtered_coins.append(coin)
    return filtered_coins
def filter_coins_by_volume(coins, df, circulating_pct):
    filtered_coins = []
    http = urllib3.PoolManager()
    for coin in coins:
        url = f'https:
        response = http.request('GET', url)
        clean_data = json.loads(response.data)
        circulating_supply = float(clean_data[0]['available_supply'])
        coin_data = df[df['Coin'] == coin].copy()
        coin_data['TokenVolume'] = coin_data['Volume'] / coin_data['Close']
        coin_data = coin_data.groupby(pd.Grouper(key='Date', freq='M')).sum()
        coin_data.drop(coin_data.tail(1).index, inplace=True)
        vol_list = coin_data.tail(3)['TokenVolume'].tolist()
        if all(volume >= circulating_supply * circulating_pct for volume in vol_list):
            filtered_coins.append(coin)
    return filtered_coins
def screenUniverse(universe_selection_date, min_market_cap, min_listing_period, circulating_pct, min_exchanges):
    coindata = load_coin_data('input/clean_coindata.csv')
    coindata = convert_to_datetime(coindata, 'Date')
    filtered_coins = filter_coins_by_date_and_market_cap(coindata, universe_selection_date, min_market_cap)
    exchanges_data = json.load(open('input/exchangesdata.json'))
    filtered_coins = filter_coins_by_exchanges(filtered_coins, exchanges_data, min_exchanges)
    filtered_coins = filter_coins_by_listing_period(filtered_coins, coindata, universe_selection_date, min_listing_period)
    filtered_coins = filter_coins_by_volume(filtered_coins, coindata, circulating_pct)
    return filtered_coins