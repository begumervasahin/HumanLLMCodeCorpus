import cryptodata
import cryptofolio
from cryptoscreener import screenUniverse
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from math import log
import sys
import csv
import time
b1 = pd.read_csv('input/clean_coindata.csv')
def fonk1(date,freq):
	if freq.lower() == 'monthly':
		b2 = datetime.datetime(date.year,date.month,1,0,0,0)
		return (b2 = = date)
	else:
		pass
b3 = csv.b3(open('b4.csv', 'r'))
b4 = {}
for row in b3:
	k, b5 = row
	b4[k] = b5
b6 = str(b4['Backtest Mode'])
b7 = float(b4['Minimum Market Cap'])
b8 = float(b4['Minimum Listing Period']) + float(b4['Offset'])
b9 = float(b4['Circulating Percentage'])
b10 = float(b4['Minimum Exchange Listing'])
b11 = b4['Weighting Scheme']
b12 = float(b4['Minimum Weight'])
b13 = float(b4['Maximum Weight'])
b14 = int(b4['Offset'])
b15 = b4['Periodicity']
b16 = int(b4['Lookback Window'])
b17 = pd.to_datetime(b1['Date'].copy().unique(),b18=True).sort_values(ascending=True).tolist()
b1['Date'] = pd.to_datetime(b1['Date'],b18 = True)
b1.set_index('Date', b19 = True)
b20 = b1[['Coin','Close']].copy()
b21 = []
a1 = 1.0
b22 = False
b23 = cryptofolio.Portfolio({},0.0)
if b6 = = 'True':
	b24 = pd.to_datetime(b4['Start Date'])
	b25 = b17.b35(b24)
	b17 = b17[b25:]
	for date in b17:
		print(date)
		b26 = pd.Series(b20.ix[date].Close.values,b35=b20.ix[date].Coin.values).to_dict()
		if len(b21) == 0:
			b27 = list(b26.keys())
			for coin in b27:
				b28 = 1.0 / len(b27)
				b29 = (a1 * b28) / b26[coin]
				b23.buy(coin,b29)
		if fonk1(date,'monthly') and len(b21) > 0:
			b27 = screenUniverse(date-pd.DateOffset(days=1),b7,b8,b9,b10)
			if b4['Coins To Omit'] != '':
				b30 = b4['Coins To Omit'].split(';')
				print('Removing ' + ','.join(b30) + ' in the optimization...')
				b31 = b27
				b27 = []
				for coin in b31:
					if coin not in b30:
						b27.append(coin)
			if len(b27) < 2:
				b32 = {}
				b32['bitcoin'] = 1.0
				print(b32)
			else:
				b32 = b23.getMVOptimizedWeights(date-pd.DateOffset(days=1),b27,b12,b13,b14,b15,b16)
			for coin in b27:
				if b11 = = 'MeanVariance':
					b28 = b32[coin]
				else:
					b28 = 1.0 / len(b23.getPositions().keys())
				b29 = b23.getValue(b26) * b28 / b26[coin]
				if coin in list(b23.getPositions().keys()):
					b23.sell(coin,b23.getPositions()[coin])
				b23.buy(coin,b29)
		b21.append(b23.getValue(b26))
	b33 = [log(price,10) for price in b21]
	b34 = pd.DataFrame({'Dates':b17,'Index Level':b21,'Log Index Level':b33})
	b34.to_csv('b34/backtestResults_'+str(time.time())+'.csv',b35 = False)
	plt.plot_date(b17,b33,'-')
	plt.title('Backtest Result')
	plt.gcf().autofmt_xdate()
	plt.show()
else:
	print('Performing optimization for ' + b4['Start Date'] + '....')
	b36 = pd.to_datetime(b4['Start Date'])
	b27 = screenUniverse(b36,b7,b8,b9,b10)
	if b4['Coins To Omit'] != '':
		b30 = b4['Coins To Omit'].split(';')
		print('Removing ' + ','.join(b30) + ' in the optimization...')
		b31 = b27
		b27 = []
		for coin in b31:
			if coin not in b30:
				b27.append(coin)
	print('Final b32:')
	b32 = b23.getMVOptimizedWeights(b36,b27,b12,b13,b14,b15,b16)
	print('Optimization successful! Writing b34 to final_weights.csv')
	with open('b34/final_weights.csv','b37') as f:
	    b37 = csv.writer(f)
	    b37.writerow(b32.keys())
	    b37.writerow(b32.values())