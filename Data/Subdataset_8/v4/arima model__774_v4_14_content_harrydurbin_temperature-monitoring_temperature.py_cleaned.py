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
this_dir, this_filename = os.path.split(__file__)
DATA_PATH = os.path.join(this_dir, "data", "temperature.db")
conn = sqlite3.connect(DATA_PATH)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS temperature
                 (date text, inside real, outside real)''')
prediction = 0
username = config.USERNAME
api_key = config.API_KEY
py.sign_in(username, api_key)
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
def read_temp_raw():
    catdata = subprocess.Popen(['cat', device_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = catdata.communicate()
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
        print('Time is:', datetime.datetime.now())
        print("%s temperature is: %s" % ('Indoor', temp_f))
        return temp_c, temp_f
def getOutsideTemp():
    f1 = urllib2.urlopen('http:
    json_string = f1.read()
    parsed_json = json.loads(json_string)
    ps_temp_f = parsed_json['current_observation']['temp_f']
    print("%s temperature is: %s" % ('Outside', ps_temp_f))
    f1.close()
    return ps_temp_f
while True:
    sensor_data = round(read_temp()[1], 2)
    outside_temp = round(getOutsideTemp(), 1)
    cur_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    conn = sqlite3.connect(DATA_PATH)
    c = conn.cursor()
    new_row = [(cur_time, sensor_data, outside_temp,)]
    c.executemany("INSERT INTO temperature ('date', 'inside', 'outside') VALUES (?,?,?)", new_row)
    conn.commit()
    if prediction > 0:
        print(prediction)
        new_row = [(prediction,)]
        c.executemany("INSERT INTO temperature ('forecast') VALUES (?)", new_row)
        conn.commit()
    df = pd.read_sql_query(
        , con=conn)
    df['date1'] = pd.to_datetime(df['date']).values
    df.index = df.date1
    df.index = pd.DatetimeIndex(df.index)
    df = df.drop('forecast', 1)
    df['upper'] = df['outside']
    df['lower'] = df['outside']
    model = ARIMA(df['outside'], order=(5, 1, 0))
    model_fit = model.fit(disp=0)
    forecast = model_fit.forecast(5)
    prediction = round(forecast[0][0], 2)
    t0 = df['date1'][-1]
    new_dates = [t0 + datetime.timedelta(minutes=60 * i) for i in range(1, 6)]
    new_dates1 = map(lambda x: x.strftime('%Y-%m-%d %H:%M'), new_dates)
    df2 = pd.DataFrame(columns=['date', 'inside', 'outside', 'forecast'])
    df2.date = new_dates1
    df2.forecast = forecast[0]
    df2['upper'] = forecast[0] + forecast[1]
    df2['lower'] = forecast[0] - forecast[1]
    df = df.append(df2)
    df = df.reset_index()
    recentreadings = df
    recentreadings['forecast'][-6:-5] = recentreadings['outside'][-6:-5]
    X = [str(i) for i in recentreadings['date'].values]
    X_rev = X[::-1]
    y_upper = [j for j in recentreadings['upper']]
    y_lower = [j for j in recentreadings['lower']]
    y_lower = y_lower[::-1]
    trace1 = go.Scatter(
        x=X,
        y=[j for j in recentreadings['inside'].values],
        name='Indoor Temperature',
        line=dict(
            color=('rgb(22, 96, 167)'),
            width=4)
    )
    trace2 = go.Scatter(
        x=X,
        y=[j for j in recentreadings['outside'].values],
        name='Outdoor Temperature',
        line=dict(
            color=('rgb(205, 12, 24)'),
            width=4)
    )
    trace3 = go.Scatter(
        x=X,
        y=[j for j in recentreadings['forecast'].values],
        name='ARIMA Forecasted Temperature',
        line=dict(
            color=('rgb(205, 12, 24)'),
            width=4,
            dash='dot')
    )
    trace4 = go.Scatter(
        x=X+X_rev,
        y=y_upper+y_lower,
        fill='tozerox',
        fillcolor='rgba(231,107,243,0.2)',
        line=go.Line(color='transparent'),
        showlegend=True,
        name='Std Error'
    )
    data = [trace1, trace2, trace3, trace4]
    layout = go.Layout(
        title='Temperature',
        yaxis=dict(title='Temp [deg F]')
    )
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='home_temperature', auto_open=False)
    time.sleep(60 * 60)