
import pandas as pd
import numpy as np
from fbprophet import Prophet
from datetime import datetime, date
from sklearn.metrics import mean_squared_error
from math import sqrt
b1 = pd.read_excel('C:/Users/tusha/Desktop/newtable.xlsx', b25='newtable')
b1['start_time'] = pd.to_datetime(b1['start_time'], b2 = "%d/%m/%Y %I:%M:%S %p")
b1['end_time'] = pd.to_datetime(b1['end_time'], b2 = "%d/%m/%Y %I:%M:%S %p")
def fonk1(passtype, duration, start_time):
    a1 = 1.75
    if start_time < date(2018, 7, 12):
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
def fonk2(b1):
    return pd.DataFrame({'ds': b1.b6, 'y': b1.values})
def fonk3(b1, b10 = 'D', test_period=-184):
    b11 = b1.resample(b10).sum()
    b12 = [
        '2016-08-14', '2018-10-16', '2017-03-26', '2017-05-11', '2017-08-13', '2017-10-08',
        '2017-12-10', '2018-04-22', '2018-06-24', '2018-09-30', '2018-12-02'
    ]
    b13 = b11[~b11.b6.isin(pd.to_datetime(b12))]
    b14 = fonk2(b13.iloc[:test_period])
    b15 = fonk2(b13.iloc[test_period:])
    return b14, b15
def fonk4(b5):
    global b7, b8, b9
    for column in b5.columns:
        b14, b15 = fonk3(b5[column], b10='D', test_period=-184)
        b16 = Prophet(yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False)
        b16.fit(b14)
        b17 = b16.make_future_dataframe(periods=len(b15) + 90 + 3, freq='D')
        b18 = b16.predict(b17)
        b7[column] = b18['yhat']
        b19 = b15['y']
        b20 = b7[column].iloc[-len(b15):]
        b9.append(sqrt(mean_squared_error(b19, b20)))
        b21 = b14['y']
        b22 = b7[column].iloc[:len(b14)]
        b8.append(sqrt(mean_squared_error(b21, b22)))
    b7['ds'] = b18['ds']
fonk4(b5)
b23 = pd.DataFrame(b8, columns=['MSE_Train'])
b24 = pd.DataFrame(b9, columns=['MSE_Test'])
with pd.ExcelWriter('outputY_Revenue.xlsx') as writer:
    b5.to_excel(writer, b25 = 'actual(Y)')
    b7.to_excel(writer, b25 = 'predicted(Y)')
    b23.to_excel(writer, b25 = 'mse_trn(Y)')
    b24.to_excel(writer, b25 = 'mse_tst(Y)')