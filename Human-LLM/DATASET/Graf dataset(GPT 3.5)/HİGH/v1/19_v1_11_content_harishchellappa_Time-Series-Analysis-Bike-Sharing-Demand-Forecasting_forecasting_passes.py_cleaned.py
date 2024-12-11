import pandas as pd
import numpy as np
from fbprophet import Prophet
from sklearn.metrics import mean_squared_error
from math import sqrt
from datetime import datetime, date
def fonk1(passtype, duration, time):
    a1 = 1.75
    if time < date(b1 = 2018, month=7, day=12):
        a1 = 3.5
    a2 = 0
    b2 = int(duration / 30)
    b3 = duration % 30
    if b3 != 0:
        b2 = b2 + 1
    if passtype in ['Monthly Pass', 'Annual Pass', 'One Day Pass', 'Flex Pass']:
        b2 = b2 - 1
    if b2 < 0:
        b2 = 0
    a2 = a1 * b2
    return a2
b4 = pd.read_excel('C:/Users/tusha/Desktop/newtable.xlsx', b27='newtable')
b4['start_time'] = pd.to_datetime(b4['start_time'], b5 = "%d/%b20/%Y %I:%M:%S %p")
b4['end_time'] = pd.to_datetime(b4['end_time'], b5 = "%d/%b20/%Y %I:%M:%S %p")
b6 = []
for passtype, duration, time in zip(b4['passholder_type'], b4['trip_duration'], b4['start_time']):
    b6.append(fonk1(passtype, duration, time.date()))
b4['revenue'] = b6
b7 = pd.pivot_table(b4[['revenue', 'start_time']], aggfunc='sum', b8=b4['start_time'].dt.date, columns=['revenue'], fill_value=0)
b7.b8 = pd.to_datetime(b7.b8)
b9 = pd.DataFrame()
b10 = []
b11 = []
def fonk2(b4, b12 = 0):
    b13 = pd.DataFrame()
    b13['ds'] = b4.b8
    b13['y'] = list(b4.iloc[:, b12])
    return b13
def fonk3(b7, b14 = 'D', train_prop=0.80):
    b7 = b7.resample(b14).sum()
    b15 = ['2016-08-14', '2018-10-16', '2017-03-26', '2017-05-11', '2017-08-13', '2017-10-08',
           '2017-12-10', '2018-04-22', '2018-06-24', '2018-09-30', '2018-12-02']
    b7['temp'] = b7.b8
    for l in b15:
        b7 = b7[b7.temp != l]
    b7.drop('temp', b16 = 1, inplace=True)
    b17 = pd.DataFrame()
    b18 = pd.DataFrame()
    b17 = b7.loc[b7.b8[:int(train_prop * len(b7.b8))]]
    b18 = b7.loc[b7.b8[int(train_prop * len(b7.b8)):]]
    b17 = fonk2(b17)
    b18 = fonk2(b18)
    return b17, b18
for i, v in enumerate(b7.columns):
    trn, b19 = fonk3(b7)
    b20 = Prophet(yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=True)
    b20.fit(trn)
    b21 = b20.make_future_dataframe(periods=len(b19), freq='D')
    b22 = b20.predict(b21)
    b9[v] = b22['yhat']
    b23 = b19['y']
    b24 = b9[v][b9.b8[int(0.8 * len(b9.b8)):]]
    b11.append(sqrt(mean_squared_error(b23, b24)))
    b25 = trn['y']
    b26 = b9[v].iloc[:int(0.8 * len(b9.b8))]
    b10.append(sqrt(mean_squared_error(b25, b26)))
b9['ds'] = b22['ds']
b15 = ['2016-08-14', '2018-10-16', '2017-03-26', '2017-05-11', '2017-08-13', '2017-10-08',
       '2017-12-10', '2018-04-22', '2018-06-24', '2018-09-30', '2018-12-02']
b7['ds'] = b7.b8
for l in b15:
    b7 = b7[b7.ds != l]
b7 = b7.reset_index(drop=True)
b10 = pd.DataFrame(b10)
b11 = pd.DataFrame(b11)
with pd.ExcelWriter('outputY_Passholder.xlsx') as writer:
    b7.to_excel(writer, b27 = 'actual(YWD)')
    b9.to_excel(writer, b27 = 'predicted(YWD)')
    b10.to_excel(writer, b27 = 'b10(YWD)')
    b11.to_excel(writer, b27 = 'b11(YWD)')