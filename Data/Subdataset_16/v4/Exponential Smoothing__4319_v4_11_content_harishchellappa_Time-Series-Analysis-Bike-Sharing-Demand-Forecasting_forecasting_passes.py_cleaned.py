
import pandas as pd
import numpy as np
from fbprophet import Prophet
from datetime import datetime, date
from sklearn.metrics import mean_squared_error
from math import sqrt
import matplotlib.pyplot as plt
b1 = pd.read_excel('C:/Users/tusha/Desktop/newtable.xlsx', b26='newtable')
b1['start_time'] = pd.to_datetime(b1['start_time'], b2 = "%d/%m/%Y %I:%M:%S %p")
b1['end_time'] = pd.to_datetime(b1['end_time'], b2 = "%d/%m/%Y %I:%M:%S %p")
def fonk1(passtype, duration, time):
    a1 = 1.75
    if time < date(2018, 7, 12):
        a1 = 3.5
    b3 = int(duration / 30)
    if duration % 30 != 0:
        b3 += 1
    if passtype in ['Monthly Pass', 'Annual Pass', 'One Day Pass', 'Flex Pass']:
        b3 -= 1
    return max(0, a1 * b3)
b1['revenue'] = b1.apply(lambda row: fonk1(row['passholder_type'], row['trip_duration'], row['start_time'].date()), b4 = 1)
b5 = pd.pivot_table(b1, values='revenue', b6=b1['start_time'].dt.date, aggfunc='sum', fill_value=0)
b5.b6 = pd.to_datetime(b5.b6)
b7 = pd.DataFrame()
b8 = []
b9 = []
def fonk2(b1, b10 = 0):
    return pd.DataFrame({'ds': b1.b6, 'y': b1.iloc[:, b10].values})
def fonk3(b1, b11 = 'D', train_prop=0.80):
    b1 = b1.resample(b11).sum()
    b12 = [
        '2016-08-14', '2018-10-16', '2017-03-26', '2017-05-11', '2017-08-13', '2017-10-08',
        '2017-12-10', '2018-04-22', '2018-06-24', '2018-09-30', '2018-12-02'
    ]
    b1 = b1[~b1.b6.isin(pd.to_datetime(b12))]
    b13 = int(train_prop * len(b1))
    b14 = fonk2(b1.iloc[:b13], 0)
    b15 = fonk2(b1.iloc[b13:], 0)
    return b14, b15
for column in b5.columns:
    train_data, b16 = fonk3(b5[column], b11='D')
    b17 = Prophet(yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=True)
    b17.fit(train_data)
    b18 = b17.make_future_dataframe(periods=len(b16), freq='D')
    b19 = b17.predict(b18)
    b7[column] = b19['yhat']
    b20 = b16['y']
    b21 = b7[column].iloc[-len(b16):]
    b9.append(sqrt(mean_squared_error(b20, b21)))
    b22 = train_data['y']
    b23 = b7[column].iloc[:len(train_data)]
    b8.append(sqrt(mean_squared_error(b22, b23)))
b7['ds'] = b19['ds']
b24 = pd.DataFrame(b8, columns=['MSE_Train'])
b25 = pd.DataFrame(b9, columns=['MSE_Test'])
with pd.ExcelWriter('outputY_Passholder.xlsx') as writer:
    b5.to_excel(writer, b26 = 'actual(YWD)')
    b7.to_excel(writer, b26 = 'predicted(YWD)')
    b24.to_excel(writer, b26 = 'b8(YWD)')
    b25.to_excel(writer, b26 = 'b9(YWD)')