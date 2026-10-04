import pandas as pd
url_template = 'https:
cryptos = [
    'ETH', 'VTC', 'STR', 'XRP', 'DASH', 'LTC', 'ETC', 'XMR', 'ZEC',
    'STRAT', 'XEM', 'VIA', 'SYS', 'LSK', 'FCT', 'CVC', 'BTS', 'DOGE',
    'DGB', 'DCR', 'SC', 'EXP', 'GNO', 'XCP', 'MAID', 'NXC', 'GNT',
    'STEEM', 'ZRX', 'GAME', 'FLO', 'NAV', 'CLAM', 'LBC', 'HUC', 'OMNI',
    'POT', 'BURST', 'BCY', 'NXT', 'FLDC', 'ARDR', 'BLK', 'EMC2',
    'NEOS', 'AMP', 'BCN', 'RADS', 'VRC', 'XVC', 'REP', 'BTCD', 'XBC',
    'RIC', 'PASC', 'NMC', 'PPC', 'PINK', 'XPM', 'SBD', 'GRC', 'BELA',
    'BTM'
]
def coin_lookup(coin):
    currency_pair = f'BTC_{coin}'
    url = url_template.format(currency_pair)
    data = pd.read_json(url)
    return data
if __name__ == "__main__":
    eth_data = coin_lookup('ETH')
    print(eth_data.head())
