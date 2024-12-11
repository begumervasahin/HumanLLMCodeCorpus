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
b1 = os.path.join(os.path.split(__file__)[0], "b53", "temperature.db")
b2 = sqlite3.connect(b1)
b3 = b2.cursor()
b3.execute('''CREATE TABLE IF NOT EXISTS temperature
                 (b33 text, inside real, outside real)''')
a1 = 0
b4 = config.USERNAME
b5 = config.API_KEY
py.sign_in(b4, b5)
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
b6 = '/sys/bus/w1/devices/'
b7 = glob.glob(b6 + '28*')[0]
b8 = b7 + '/w1_slave'
def fonk1():
    b9 = subprocess.Popen(['cat', b8], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, b10 = b9.communicate()
    b11 = out.decode('utf-8')
    return b11.split('\n')
def fonk2():
    b12 = fonk1()
    while b12[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        b12 = fonk1()
    b13 = b12[1].find('t=')
    if b13 != -1:
        b14 = b12[1][b13+2:]
        b15 = float(b14) / 1000.0
        b16 = b15 * 9.0 / 5.0 + 32.0
        print('Time is:', datetime.datetime.now())
        print("%s temperature is: %s" % ('Indoor', b16))
        return b15, b16
def fonk3():
    with urllib2.urlopen('http:
        b17 = json.load(f)
        b18 = b17['current_observation']['b16']
        print("%s temperature is: %s" % ('Outside', b18))
        return b18
while True:
    b19 = round(fonk2()[1], 2)
    b20 = round(fonk3(), 1)
    b21 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    b22 = [(b21, b19, b20)]
    b3.executemany("INSERT INTO temperature ('b33', 'inside', 'outside') VALUES (?,?,?)", b22)
    b2.commit()
    if a1 > 0:
        print(a1)
        b22 = [(a1,)]
        b3.executemany("INSERT INTO temperature ('b28') VALUES (?)", b22)
        b2.commit()
    b23 = pd.read_sql_query(
        , b24 = b2)
    b23['date1'] = pd.to_datetime(b23['b33']).values
    b23.b25 = b23.date1
    b23.b25 = pd.DatetimeIndex(b23.b25)
    b23 = b23.drop('b28', 1)
    b23['upper'] = b23['outside']
    b23['lower'] = b23['outside']
    b26 = ARIMA(b23['outside'], order=(5, 1, 0))
    b27 = b26.fit(disp=0)
    b28 = b27.b28(5)
    a1 = round(b28[0][0], 2)
    b29 = b23['date1'][-1]
    b30 = [b29 + datetime.timedelta(minutes=60 * i) for i in range(1, 6)]
    b31 = map(lambda b40: b40.strftime('%Y-%m-%d %H:%M'), b30)
    b32 = pd.DataFrame(columns=['b33', 'inside', 'outside', 'b28'])
    b32.b33 = b31
    b32.b28 = b28[0]
    b32['upper'] = b28[0] + b28[1]
    b32['lower'] = b28[0] - b28[1]
    b23 = b23.append(b32)
    b23 = b23.reset_index()
    b34 = b23
    b34['b28'][-6:-5] = b34['outside'][-6:-5]
    b35 = [str(i) for i in b34['b33'].values]
    b36 = b35[::-1]
    b37 = [j for j in b34['upper']]
    b38 = [j for j in b34['lower']]
    b38 = b38[::-1]
    b39 = go.Scatter(
        b40 = b35,
        b41 = [j for j in b34['inside'].values],
        b42 = 'Indoor Temperature',
        b43 = dict(
            b44 = ('rgb(22, 96, 167)'),
            b45 = 4)
    )
    b46 = go.Scatter(
        b40 = b35,
        b41 = [j for j in b34['outside'].values],
        b42 = 'Outdoor Temperature',
        b43 = dict(
            b44 = ('rgb(205, 12, 24)'),
            b45 = 4)
    )
    b47 = go.Scatter(
        b40 = b35,
        b41 = [j for j in b34['b28'].values],
        b42 = 'ARIMA Forecasted Temperature',
        b43 = dict(
            b44 = ('rgb(205, 12, 24)'),
            b45 = 4,
            b48 = 'dot')
    )
    b49 = go.Scatter(
        b40 = b35+b36,
        b41 = b37+b38,
        b50 = 'tozerox',
        b51 = 'rgba(231,107,243,0.2)',
        b43 = go.Line(b44='transparent'),
        b52 = True,
        b42 = 'Std Error'
    )
    b53 = [b39, b46, b47, b49]
    b54 = go.Layout(
        b55 = 'Temperature',
        b56 = dict(b55='Temp [deg F]')
    )
    b57 = go.Figure(b53=b53, b54=b54)
    b58 = py.plot(b57, filename='home_temperature', auto_open=False)
    time.sleep(60 * 60)