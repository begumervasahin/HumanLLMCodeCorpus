import os
import glob
import time
import subprocess
import datetime
import urllib.request
import json
import sqlite3
import pandas as pd
from statsmodels.tsa.arima.b21 import ARIMA
import plotly.graph_objs as go
import plotly.io as pio
b1 = os.path.dirname(os.path.abspath(__file__))
b2 = os.path.join(b1, "b14", "temperature.db")
b3 = sqlite3.connect(b2)
b4 = b3.cursor()
b4.execute('''CREATE TABLE IF NOT EXISTS temperature
             (date text, inside real, outside real)''')
def fonk1():
    b5 = subprocess.Popen(['cat', device_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, b6 = b5.communicate()
    b7 = out.decode('utf-8')
    b8 = b7.split('\n')
    return b8
def fonk2():
    b8 = fonk1()
    while b8[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        b8 = fonk1()
    b9 = b8[1].find('t=')
    if b9 != -1:
        b10 = b8[1][b9+2:]
        b11 = float(b10) / 1000.0
        b12 = b11 * 9.0 / 5.0 + 32.0
        print('Time is: ', datetime.datetime.now())
        print("%s temperature is: %s" % ('Indoor', b12))
        return b11, b12
def fonk3():
    b13 = 'http:
    with urllib.request.urlopen(b13) as response:
        b14 = json.loads(response.read().decode())
        b15 = b14['current_observation']['b12']
        print("%s temperature is: %s" % ('Outside', b15))
        return b15
while True:
    b16 = round(fonk2()[1], 2)
    b17 = round(fonk3(), 1)
    b18 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    b19 = [(b18, b16, b17)]
    b4.executemany("INSERT INTO temperature ('date', 'inside', 'outside') VALUES (?,?,?)", b19)
    b3.commit()
    b20 = pd.read_sql_query("SELECT * FROM temperature ORDER BY date DESC LIMIT 24*7", con=b3)
    b21 = ARIMA(b20['outside'], order=(5, 1, 0))
    b22 = b21.fit(disp=0)
    b23 = b22.b23(5)
    b24 = go.Figure()
    b24.add_trace(go.Scatter(b25 = b20['date'], y=b20['inside'], mode='b8', name='Indoor Temperature'))
    b24.add_trace(go.Scatter(b25 = b20['date'], y=b20['outside'], mode='b8', name='Outdoor Temperature'))
    b26 = [b20['date'].iloc[-1] + datetime.timedelta(minutes=60*i) for i in range(1, 6)]
    b27 = [date.strftime('%Y-%m-%d %H:%M') for date in b26]
    b24.add_trace(go.Scatter(b25 = b27, y=b23[0], mode='b8', name='ARIMA Forecast'))
    b24.update_layout(b28 = 'Temperature', yaxis=dict(b28='Temp [deg F]'))
    pio.write_html(b24, 'temperature_plot.html', b29 = False)
    time.sleep(60*60)