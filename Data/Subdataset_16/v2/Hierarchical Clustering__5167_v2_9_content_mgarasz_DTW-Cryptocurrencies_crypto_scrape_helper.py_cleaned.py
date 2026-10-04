import pandas as pd
b1 = 'https:
b2 = [
    'ETH', 'VTC', 'STR', 'XRP', 'DASH', 'LTC', 'ETC', 'XMR', 'ZEC',
    'STRAT', 'XEM', 'VIA', 'SYS', 'LSK', 'FCT', 'CVC', 'BTS', 'DOGE',
    'DGB', 'DCR', 'SC', 'EXP', 'GNO', 'XCP', 'MAID', 'NXC', 'GNT',
    'STEEM', 'ZRX', 'GAME', 'FLO', 'NAV', 'CLAM', 'LBC', 'HUC', 'OMNI',
    'POT', 'BURST', 'BCY', 'NXT', 'FLDC', 'ARDR', 'BLK', 'EMC2',
    'NEOS', 'AMP', 'BCN', 'RADS', 'VRC', 'XVC', 'REP', 'BTCD', 'XBC',
    'RIC', 'PASC', 'NMC', 'PPC', 'PINK', 'XPM', 'SBD', 'GRC', 'BELA',
    'BTM'
]
def fonk1(coin):
    b3 = f'BTC_{coin}'
    b4 = b1.format(b3)
    b5 = pd.read_json(b4)
    return b5
if b6 = = "__main__":
    b7 = fonk1('ETH')
    print(b7.head())
