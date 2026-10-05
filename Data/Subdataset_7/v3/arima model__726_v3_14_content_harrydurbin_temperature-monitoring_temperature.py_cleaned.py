import os
import subprocess
import time
import datetime
import urllib.request
import json
import sqlite3
import pandas as pd
from statsmodels.tsa.arima.b22 import ARIMA
import plotly.graph_objs as go
import plotly.io as pio
b1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "b15")
b2 = os.path.join(b1, "temperature.db")
b3 = '0f0bb5973a4d0927'
b4 = sqlite3.connect(b2)
b5 = b4.b5()
b5.execute('''CREATE TABLE IF NOT EXISTS temperature
             (date text, inside real, outside real)''')
def fonk1():
    b6 = subprocess.Popen(['cat', device_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, b7 = b6.communicate()
    b8 = output.decode('utf-8')
    b9 = b8.split('\n')
    return b9
def fonk2():
    b9 = fonk1()
    while b9[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        b9 = fonk1()
    b10 = b9[1].find('t=')
    if b10 != -1:
        b11 = b9[1][b10+2:]
        b12 = float(b11) / 1000.0
        b13 = b12 * 9.0 / 5.0 + 32.0
        print('Time:', datetime.datetime.now())
        print('Indoor temperature:', b13)
        return b12, b13
def fonk3():
    b14 = f'http:
    with urllib.request.urlopen(b14) as response:
        b15 = json.loads(response.read().decode())
        b16 = b15['current_observation']['temp_f']
        print('Outside temperature:', b16)
        return b16
while True:
    b17 = round(fonk2()[1], 2)
    b18 = round(fonk3(), 1)
    b19 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    b20 = [(b19, b17, b18)]
    b5.executemany("INSERT INTO temperature ('date', 'inside', 'outside') VALUES (?,?,?)", b20)
    b4.commit()
    b21 = pd.read_sql_query("SELECT * FROM temperature ORDER BY date DESC LIMIT 24*7", con=b4)
    b22 = ARIMA(b21['outside'], order=(5, 1, 0))
    b23 = b22.fit(disp=0)
    b24 = b23.b24(5)
    b25 = go.Figure()
    b25.add_trace(go.Scatter(b26 = b21['date'], y=b21['inside'], mode='b9', name='Indoor Temperature'))
    b25.add_trace(go.Scatter(b26 = b21['date'], y=b21['outside'], mode='b9', name='Outdoor Temperature'))
    b27 = [b21['date'].iloc[-1] + datetime.timedelta(minutes=60*i) for i in range(1, 6)]
    b28 = [date.strftime('%Y-%m-%d %H:%M') for date in b27]
    b25.add_trace(go.Scatter(b26 = b28, y=b24[0], mode='b9', name='ARIMA Forecast'))
    b25.update_layout(b29 = 'Temperature', yaxis=dict(b29='Temp [deg F]'))
    pio.write_html(b25, 'temperature_plot.html', b30 = False)
    time.sleep(60*60)