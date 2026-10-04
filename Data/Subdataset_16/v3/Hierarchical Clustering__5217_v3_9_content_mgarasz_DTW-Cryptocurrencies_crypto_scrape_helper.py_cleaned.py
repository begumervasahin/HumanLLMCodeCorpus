import pandas as pd
b1 = (
    'https:
    '&b2 = 1439020800&end=1511202699&period=14400'
)
b3 = [
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
    b4 = f'BTC_{coin}'
    b5 = b1.format(b4)
    b6 = pd.read_json(b5)
    return b6
def fonk2():
    b7 = fonk1('ETH')
    print(b7.head())
if b8 = = "__main__":
    fonk2()