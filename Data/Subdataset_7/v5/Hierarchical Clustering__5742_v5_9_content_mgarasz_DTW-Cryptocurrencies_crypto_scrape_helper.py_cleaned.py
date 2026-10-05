import pandas as pd
def fonk1(coin):
    b1 = f'BTC_{coin}'
    b2 = 'https:
    b3 = b2.replace('XXX', b1)
    b4 = pd.read_json(b3)
    return b4
b5 = [
    'ETH', 'VTC', 'STR', 'XRP', 'DASH', 'LTC', 'ETC', 'XMR', 'ZEC',
    'STRAT', 'XEM', 'VIA', 'SYS', 'LSK', 'FCT', 'CVC', 'BTS', 'DOGE',
    'DGB', 'DCR', 'SC', 'EXP', 'GNO', 'XCP', 'MAID',
    'NXC', 'GNT', 'STEEM', 'ZRX', 'GAME', 'FLO', 'NAV', 'CLAM',
    'LBC', 'HUC', 'OMNI', 'POT', 'BURST', 'BCY', 'NXT', 'FLDC',
    'ARDR', 'BLK', 'EMC2', 'NEOS', 'AMP', 'BCN', 'RADS', 'VRC', 'XVC',
    'REP', 'BTCD', 'XBC', 'RIC', 'PASC', 'NMC', 'PPC', 'PINK',
    'XPM', 'SBD', 'GRC', 'BELA', 'BTM'
]
for crypto in b5:
    b4 = fonk1(crypto)
