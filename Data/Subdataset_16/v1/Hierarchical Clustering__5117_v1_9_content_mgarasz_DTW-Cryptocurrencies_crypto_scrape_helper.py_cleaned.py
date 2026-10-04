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
    b3 = 'BTC_' + str(coin)
    b4 = 'https:
    b5 = b4.replace('XXX', b3)
    b6 = pd.read_json(b5)
    return b6
b7 = fonk1('ETH')
print(b7.head())
