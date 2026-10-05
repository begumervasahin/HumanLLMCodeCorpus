import pandas as pd
import json
import urllib3
import csv
import sys
import urllib3
import cryptofolio
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def fonk1(universeSelectionDate,minMarketCap,minimumListingPeriod,circulatingPct,minExchanges):
	b1 = pd.read_csv('input/clean_coindata.csv')
	b2 = pd.to_datetime(b1['Date'].copy().unique(),b3=True).sort_values(ascending=True).tolist()
	b1['Date'] = pd.to_datetime(b1['Date'],b3 = True)
	b4 = b1.ix[(b1['Date'] == universeSelectionDate) & (b1['Marketcap'] >= minMarketCap)]
	b5 = b4['Coin'].tolist()
	b6 = []
	b7 = json.load(open('input/exchangesdata.json'))
	for coin in b5:
		b8 = len(b7[coin])
		if b8 >= minExchanges:
			b6.append(coin)
	b9 = []
	for coin in b6:
		b10 = b1.ix[(b1['Coin'] == coin)].dropna().copy()
		b11 = b10['Date'].min()
		b12 = universeSelectionDate
		b13 = (b12 - b11).days
		if b13 >= minimumListingPeriod:
			b9.append(coin)
	b14 = []
	b15 = urllib3.PoolManager()
	for coin in b9:
		b16 = 'https:
		b17 = b15.request('GET',b16)
		b18 = json.loads(b17.data)
		b19 = float(b18[0]['available_supply'])
		b10 = b1.ix[(b1['Coin'] == coin)].copy()
		b10['TokenVolume'] = b10['Volume'] / b10['Close']
		b10 = b10.groupby(pd.Grouper(key='Date', freq='M')).sum()
		b10.drop(b10.tail(1).index,b20 = True)
		b21 = b10.tail(3)['TokenVolume'].tolist()
		if all(i >= b19 * circulatingPct for i in b21) == True:
			b14.append(coin)
	return b14