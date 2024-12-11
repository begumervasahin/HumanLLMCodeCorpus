import os
import glob
import time
import subprocess
import datetime
import plotly.plotly as py
import plotly.graph_objs as go
from plotly import tools
import urllib2
import json
import sqlite3
import pandas as pd
from statsmodels.tsa.arima_model import ARIMA
import config
this_dir, b1 = os.path.split(__file__)
b2 = os.path.join(this_dir, "b58", "temperature.db")
b3 = sqlite3.connect(b2)
b4 = b3.cursor()
b4.execute('''CREATE TABLE IF NOT EXISTS temperature
                 (b38 text, inside real, outside real)''')
a1 = 0
b5 = config.USERNAME
b6 = config.API_KEY
b7 = config.b7
b8 = config.b8
py.sign_in(b5, b6)
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
b9 = '/sys/bus/w1/devices/'
b10 = glob.glob(b9 + '28*')[0]
b11 = b10 + '/w1_slave'
def fonk1():
    b12 = subprocess.Popen(['cat',b11], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out,b13 = b12.communicate()
    b14 = out.decode('utf-8')
    b15 = b14.split('\n')
    return b15
def fonk2():
    b15 = fonk1()
    while b15[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        b15 = fonk1()
    b16 = b15[1].find('t=')
    if b16 != -1:
        b17 = b15[1][b16+2:]
        b18 = float(b17) / 1000.0
        b19 = b18 * 9.0 / 5.0 + 32.0
	print '
  	print 'Time is: ', datetime.datetime.now()
	print "%s temperature is: %s" % ('Indoor', b19)
        return b18, b19
def fonk3():
  b20 = urllib2.urlopen('http:
  b21 = b20.read()
  b22 = json.loads(b21)
  b22.keys()
  b23 = b22['current_observation']['b19']
  print "%s temperature is: %s" % ('Outside', b23)
  b20.close()
  return b23
while True:
  	b24 = round(fonk2()[1],2)
	b25 = round(fonk3(),1)
	b26 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
	b3 = sqlite3.connect(b2)
	b4 = b3.cursor()
	b27 = [(b26, b24, b25,)]
	b4.executemany("INSERT INTO temperature ('b38', 'inside', 'outside') VALUES (?,?,?)", b27)
	b3.commit()
	if a1 > 0:
		print a1
		b27 = [(a1,)]
		b4.executemany("INSERT INTO temperature ('b33') VALUES (?)", b27)
		b3.commit()
	b28 = pd.read_sql_query(
	, b29 = b3)
	b28['date1'] = pd.to_datetime(b28['b38']).values
	b28.b30 = b28.date1
	b28.b30 = pd.DatetimeIndex(b28.b30)
    	b28 = b28.drop('b33',1)
	b28['upper'] = b28['outside']
	b28['lower'] = b28['outside']
	b31 = ARIMA(b28['outside'], order=(5,1,0))
	b32 = b31.fit(disp=0)
	b33 = b32.b33(5)
	a1 = round(b33[0][0],2)
	b34 = b28['date1'][-1]
	b35 = [b34+datetime.timedelta(minutes = 60*i) for i in range(1,6)]
	b36 = map(lambda b45: b45.strftime('%Y-%m-%d %H:%M'), b35)
	b37 = pd.DataFrame(columns=['b38','inside','outside','b33'])
	b37.b38 = b36
	b37.b33 = b33[0]
	b37['upper'] = b33[0]+b33[1]
	b37['lower'] = b33[0]-b33[1]
	b28 = b28.append(b37)
	b28 = b28.reset_index()
	b39 = b28
	b39['b33'][-6:-5] = b39['outside'][-6:-5]
	b40 = [str(i) for i in b39['b38'].values]
	b41 = b40[::-1]
	b42 = [j for j in b39['upper']]
	b43 = [j for j in b39['lower']]
	b43 = b43[::-1]
	b44 = go.Scatter(
	b45 = b40,
	b46 = [j for j in b39['inside'].values],
	    b47 = 'Indoor Temperature',
	    b48 = dict(
	    b49 = ('rgb(22, 96, 167)'),
	    b50 = 4)
	)
	b51 = go.Scatter(
	b45 = b40,
	b46 = [j for j in b39['outside'].values],
	    b47 = 'Outdoor Temperature',
	    b48 = dict(
	    b49 = ('rgb(205, 12, 24)'),
	    b50 = 4)
	)
	b52 = go.Scatter(
	b45 = b40,
	b46 = [j for j in b39['b33'].values],
	    b47 = 'ARIMA Forecasted Temperature',
	    b48 = dict(
	    b49 = ('rgb(205, 12, 24)'),
	    b50 = 4,
	    b53 = 'dot')
	)
	b54 = go.Scatter(
	b45 = b40+b41,
	b46 = b42+b43,
	    b55 = 'tozerox',
	    b56 = 'rgba(231,107,243,0.2)',
	    b48 = go.Line(b49='transparent'),
	    b57 = True,
	    b47 = 'Std Error'
	)
	b58 = [b44, b51, b52, b54]
	b59 = go.Layout(
	b60 = 'Temperature',
	b61 = dict(b60 = 'Temp [deg F]')
	)
	b62 = go.Figure(b58=b58, b59=b59)
	b63 = py.plot(b62, filename='home_temperature', auto_open = False)
	time.sleep(60*60)