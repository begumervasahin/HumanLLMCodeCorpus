import pandas as pd
URL_TEMPLATE = (
    'https:
    '&start=1439020800&end=1511202699&period=14400'
)
CRYPTOS = [
    'ETH', 'VTC', 'STR', 'XRP', 'DASH', 'LTC', 'ETC', 'XMR', 'ZEC',
    'STRAT', 'XEM', 'VIA', 'SYS', 'LSK', 'FCT', 'CVC', 'BTS', 'DOGE',
    'DGB', 'DCR', 'SC', 'EXP', 'GNO', 'XCP', 'MAID', 'NXC', 'GNT',
    'STEEM', 'ZRX', 'GAME', 'FLO', 'NAV', 'CLAM', 'LBC', 'HUC', 'OMNI',
    'POT', 'BURST', 'BCY', 'NXT', 'FLDC', 'ARDR', 'BLK', 'EMC2',
    'NEOS', 'AMP', 'BCN', 'RADS', 'VRC', 'XVC', 'REP', 'BTCD', 'XBC',
    'RIC', 'PASC', 'NMC', 'PPC', 'PINK', 'XPM', 'SBD', 'GRC', 'BELA',
    'BTM'
]
def fetch_coin_data(coin):
    currency_pair = f'BTC_{coin}'
    url = URL_TEMPLATE.format(currency_pair)
    data = pd.read_json(url)
    return data
def main():
    eth_data = fetch_coin_data('ETH')
    print(eth_data.head())
if __name__ == "__main__":
    main()