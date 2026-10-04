
import pandas as pd
import numpy as np
from fbprophet import Prophet
from datetime import datetime, date
from sklearn.metrics import mean_squared_error
from math import sqrt
import matplotlib.pyplot as plt
b1 = pd.read_excel('C:/Users/tusha/Desktop/newtable.xlsx', b31='newtable')
b1['start_time'] = pd.to_datetime(b1['start_time'], b2 = "%d/%m/%Y %I:%M:%S %p")
b1['end_time'] = pd.to_datetime(b1['end_time'], b2 = "%d/%m/%Y %I:%M:%S %p")
def fonk1(passtype, duration, time):
    a1 = 1.75
    if time < date(b3 = 2018, month=7, day=12):
        a1 = 3.5
    b4 = int(duration / 30)
    b5 = duration % 30
    if b5 != 0:
        b4 += 1
    if passtype in ['Monthly Pass', 'Annual Pass', 'One Day Pass', 'Flex Pass']:
        b4 -= 1
    return max(0, a1 * b4)
b1['revenue'] = b1.apply(lambda row: fonk1(row['passholder_type'], row['trip_duration'], row['start_time'].date()), b6 = 1)
b7 = pd.pivot_table(b1[['revenue', 'start_time']],
                          b8 = b1['start_time'].dt.date,
                          b9 = ['revenue'],
                          b10 = 'sum',
                          b11 = 0)
b7.b8 = pd.to_datetime(b7.b8)
b12 = pd.DataFrame()
b13 = []
b14 = []
def fonk2(b1, b15 = 0):
    return pd.DataFrame({'ds': b1.b8, 'y': b1.iloc[:, b15].values})
def fonk3(b1, b16 = 'D', train_prop=0.80):
    b1 = b1.resample(b16).sum()
    b17 = [
        '2016-08-14', '2018-10-16', '2017-03-26', '2017-05-11', '2017-08-13', '2017-10-08',
        '2017-12-10', '2018-04-22', '2018-06-24', '2018-09-30', '2018-12-02'
    ]
    b1 = b1[~b1.b8.isin(pd.to_datetime(b17))]
    b18 = int(train_prop * len(b1))
    b19 = fonk2(b1.iloc[:b18], b15)
    b20 = fonk2(b1.iloc[b18:], b15)
    return b19, b20
for b15, revenue in enumerate(b7.b9):
    train_data, b21 = fonk3(b7, b16='D')
    b22 = Prophet(yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=True)
    b22.fit(train_data)
    b23 = b22.make_future_dataframe(periods=len(b21), freq='D')
    b24 = b22.predict(b23)
    b12[revenue] = b24['yhat']
    b25 = b21['y']
    b26 = b12[revenue].iloc[-len(b21):]
    b14.append(sqrt(mean_squared_error(b25, b26)))
    b27 = train_data['y']
    b28 = b12[revenue].iloc[:len(train_data)]
    b13.append(sqrt(mean_squared_error(b27, b28)))
b12['ds'] = b24['ds']
b29 = pd.DataFrame(b13, b9=['MSE_Train'])
b30 = pd.DataFrame(b14, b9=['MSE_Test'])
with pd.ExcelWriter('outputY_Passholder.xlsx') as writer:
    b7.to_excel(writer, b31 = 'actual(YWD)')
    b12.to_excel(writer, b31 = 'predicted(YWD)')
    b29.to_excel(writer, b31 = 'b13(YWD)')
    b30.to_excel(writer, b31 = 'b14(YWD)')