import pandas as pd
def coin_lookup(coin):
    btc_url = 'https:
    cc = 'BTC_' + coin
    url = f'https:
    ico = pd.read_json(url)
    return ico
cryptos = ['ETH', 'VTC', 'STR', 'XRP','DASH','LTC','ETC','XMR','ZEC',
           'STRAT','XEM','VIA','SYS','LSK','FCT','CVC','BTS','DOGE',
           'DGB','DCR','SC','EXP','GNO','XCP','MAID',
           'NXC','GNT','STEEM','ZRX','GAME','FLO','NAV','CLAM',
           'LBC','HUC','OMNI','POT','BURST','BCY','NXT','FLDC',
           'ARDR','BLK','EMC2','NEOS','AMP','BCN','RADS','VRC', 'XVC',
           'REP','BTCD','XBC','RIC','PASC','NMC','PPC','PINK',
           'XPM','SBD','GRC','BELA','BTM']
for crypto in cryptos:
    data = coin_lookup(crypto)
