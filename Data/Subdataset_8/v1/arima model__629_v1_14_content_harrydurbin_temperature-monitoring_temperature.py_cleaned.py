import os
import glob
import time
import subprocess
import datetime
import urllib.request
import json
import sqlite3
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import plotly.graph_objs as go
import plotly.io as pio
this_dir = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(this_dir, "data", "temperature.db")
conn = sqlite3.connect(DATA_PATH)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS temperature
             (date text, inside real, outside real)''')
def read_temp_raw():
    catdata = subprocess.Popen(['cat', device_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, _ = catdata.communicate()
    out_decode = out.decode('utf-8')
    lines = out_decode.split('\n')
    return lines
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        print('Time is: ', datetime.datetime.now())
        print("%s temperature is: %s" % ('Indoor', temp_f))
        return temp_c, temp_f
def get_outside_temp():
    url = 'http:
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
        ps_temp_f = data['current_observation']['temp_f']
        print("%s temperature is: %s" % ('Outside', ps_temp_f))
        return ps_temp_f
while True:
    sensor_data = round(read_temp()[1], 2)
    outside_temp = round(get_outside_temp(), 1)
    cur_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    new_row = [(cur_time, sensor_data, outside_temp)]
    c.executemany("INSERT INTO temperature ('date', 'inside', 'outside') VALUES (?,?,?)", new_row)
    conn.commit()
    df = pd.read_sql_query("SELECT * FROM temperature ORDER BY date DESC LIMIT 24*7", con=conn)
    model = ARIMA(df['outside'], order=(5, 1, 0))
    model_fit = model.fit(disp=0)
    forecast = model_fit.forecast(5)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['date'], y=df['inside'], mode='lines', name='Indoor Temperature'))
    fig.add_trace(go.Scatter(x=df['date'], y=df['outside'], mode='lines', name='Outdoor Temperature'))
    new_dates = [df['date'].iloc[-1] + datetime.timedelta(minutes=60*i) for i in range(1, 6)]
    forecast_dates = [date.strftime('%Y-%m-%d %H:%M') for date in new_dates]
    fig.add_trace(go.Scatter(x=forecast_dates, y=forecast[0], mode='lines', name='ARIMA Forecast'))
    fig.update_layout(title='Temperature', yaxis=dict(title='Temp [deg F]'))
    pio.write_html(fig, 'temperature_plot.html', auto_open=False)
    time.sleep(60*60)