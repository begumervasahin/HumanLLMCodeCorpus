import os
import glob
import time
import subprocess
import datetime
import plotly.plotly as py
import plotly.graph_objs as go
import urllib.request as urllib2
import json
import sqlite3
import pandas as pd
from statsmodels.tsa.arima_model import ARIMA
import config
this_dir, b1 = os.path.split(__file__)
b2 = os.path.join(this_dir, "b56", "temperature.db")
b3 = sqlite3.connect(b2)
b4 = b3.cursor()
b4.execute('''CREATE TABLE IF NOT EXISTS temperature
                 (b36 text, inside real, outside real)''')
a1 = 0
b5 = config.USERNAME
b6 = config.API_KEY
py.sign_in(b5, b6)
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
b7 = '/sys/bus/w1/devices/'
b8 = glob.glob(b7 + '28*')[0]
b9 = b8 + '/w1_slave'
def fonk1():
    b10 = subprocess.Popen(['cat', b9], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, b11 = b10.communicate()
    b12 = out.decode('utf-8')
    b13 = b12.split('\n')
    return b13
def fonk2():
    b13 = fonk1()
    while b13[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        b13 = fonk1()
    b14 = b13[1].find('t=')
    if b14 != -1:
        b15 = b13[1][b14+2:]
        b16 = float(b15) / 1000.0
        b17 = b16 * 9.0 / 5.0 + 32.0
        print('Time is:', datetime.datetime.now())
        print("%s temperature is: %s" % ('Indoor', b17))
        return b16, b17
def fonk3():
    b18 = urllib2.urlopen('http:
    b19 = b18.read()
    b20 = json.loads(b19)
    b21 = b20['current_observation']['b17']
    print("%s temperature is: %s" % ('Outside', b21))
    b18.close()
    return b21
while True:
    b22 = round(fonk2()[1], 2)
    b23 = round(fonk3(), 1)
    b24 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    b3 = sqlite3.connect(b2)
    b4 = b3.cursor()
    b25 = [(b24, b22, b23,)]
    b4.executemany("INSERT INTO temperature ('b36', 'inside', 'outside') VALUES (?,?,?)", b25)
    b3.commit()
    if a1 > 0:
        print(a1)
        b25 = [(a1,)]
        b4.executemany("INSERT INTO temperature ('b31') VALUES (?)", b25)
        b3.commit()
    b26 = pd.read_sql_query(
        , b27 = b3)
    b26['date1'] = pd.to_datetime(b26['b36']).values
    b26.b28 = b26.date1
    b26.b28 = pd.DatetimeIndex(b26.b28)
    b26 = b26.drop('b31', 1)
    b26['upper'] = b26['outside']
    b26['lower'] = b26['outside']
    b29 = ARIMA(b26['outside'], order=(5, 1, 0))
    b30 = b29.fit(disp=0)
    b31 = b30.b31(5)
    a1 = round(b31[0][0], 2)
    b32 = b26['date1'][-1]
    b33 = [b32 + datetime.timedelta(minutes=60 * i) for i in range(1, 6)]
    b34 = map(lambda b43: b43.strftime('%Y-%m-%d %H:%M'), b33)
    b35 = pd.DataFrame(columns=['b36', 'inside', 'outside', 'b31'])
    b35.b36 = b34
    b35.b31 = b31[0]
    b35['upper'] = b31[0] + b31[1]
    b35['lower'] = b31[0] - b31[1]
    b26 = b26.append(b35)
    b26 = b26.reset_index()
    b37 = b26
    b37['b31'][-6:-5] = b37['outside'][-6:-5]
    b38 = [str(i) for i in b37['b36'].values]
    b39 = b38[::-1]
    b40 = [j for j in b37['upper']]
    b41 = [j for j in b37['lower']]
    b41 = b41[::-1]
    b42 = go.Scatter(
        b43 = b38,
        b44 = [j for j in b37['inside'].values],
        b45 = 'Indoor Temperature',
        b46 = dict(
            b47 = ('rgb(22, 96, 167)'),
            b48 = 4)
    )
    b49 = go.Scatter(
        b43 = b38,
        b44 = [j for j in b37['outside'].values],
        b45 = 'Outdoor Temperature',
        b46 = dict(
            b47 = ('rgb(205, 12, 24)'),
            b48 = 4)
    )
    b50 = go.Scatter(
        b43 = b38,
        b44 = [j for j in b37['b31'].values],
        b45 = 'ARIMA Forecasted Temperature',
        b46 = dict(
            b47 = ('rgb(205, 12, 24)'),
            b48 = 4,
            b51 = 'dot')
    )
    b52 = go.Scatter(
        b43 = b38+b39,
        b44 = b40+b41,
        b53 = 'tozerox',
        b54 = 'rgba(231,107,243,0.2)',
        b46 = go.Line(b47='transparent'),
        b55 = True,
        b45 = 'Std Error'
    )
    b56 = [b42, b49, b50, b52]
    b57 = go.Layout(
        b58 = 'Temperature',
        b59 = dict(b58='Temp [deg F]')
    )
    b60 = go.Figure(b56=b56, b57=b57)
    b61 = py.plot(b60, filename='home_temperature', auto_open=False)
    time.sleep(60 * 60)