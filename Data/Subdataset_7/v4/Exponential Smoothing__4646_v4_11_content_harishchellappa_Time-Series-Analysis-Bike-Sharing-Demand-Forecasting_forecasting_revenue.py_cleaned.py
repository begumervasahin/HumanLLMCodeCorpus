import pandas as pd
from fbprophet import Prophet
from sklearn.metrics import mean_squared_error
from math import sqrt
from datetime import datetime, date
b1 = pd.read_excel('C:/Users/tusha/Desktop/newtable.xlsx', sheet_name='newtable')
b1['start_time'] = pd.to_datetime(b1['start_time'], b2 = "%d/%m/%Y %I:%M:%S %p")
b1['end_time'] = pd.to_datetime(b1['end_time'], b2 = "%d/%m/%Y %I:%M:%S %p")
def fonk1(pass_type, duration, time):
    a1 = 1.75
    if time < date(b3 = 2018, month=7, day=12):
        a1 = 3.5
    a2 = 0
    b4 = int(duration / 30)
    b5 = duration % 30
    if b5 != 0:
        b4 += 1
    if pass_type in ['Monthly Pass', 'Annual Pass', 'One Day Pass', 'Flex Pass']:
        b4 -= 1
        if b4 < 0:
            b4 = 0
    a2 = a1 * b4
    return a2
b6 = []
for pass_type, duration, time in zip(b1['passholder_type'], b1['trip_duration'], b1['start_time']):
    b6.append(fonk1(pass_type, duration, time.date()))
b1['revenue'] = b6
b7 = pd.pivot_table(b1[['revenue', 'start_time']], aggfunc='sum', b8=b1['start_time'].dt.date, fill_value=0)
b7.b8 = pd.to_datetime(b7.b8)
b9 = pd.DataFrame()
b10 = []
b11 = []
def fonk2(b1):
    b12 = pd.DataFrame()
    b12['ds'] = b1.b8
    b12['y'] = b1.values.flatten()
    return b12
def fonk3(b1, b13 = -184):
    b14 = ['2016-08-14', '2018-10-16', '2017-03-26', '2017-05-11', '2017-08-13', '2017-10-08',
                     '2017-12-10', '2018-04-22', '2018-06-24', '2018-09-30', '2018-12-02']
    b1 = b1[~b1.b8.isin(b14)]
    b15 = b1.iloc[:b13]
    b16 = b1.iloc[b13:]
    return b15, b16
for column in b7.columns:
    train_data, b17 = fonk3(b7)
    b18 = Prophet(yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False)
    b18.fit(fonk2(train_data))
    b19 = b18.make_future_dataframe(periods=len(b17) + 90 + 3, freq='D')
    b20 = b18.predict(b19)
    b9[column] = b20['yhat']
    b21 = b17['y']
    b22 = b9[column].tail(len(b17))
    b11.append(sqrt(mean_squared_error(b21, b22)))
    b23 = train_data['y']
    b24 = b9[column].iloc[:-184 - 93]
    b10.append(sqrt(mean_squared_error(b23, b24)))
b9['ds'] = b20['ds']
b14 = ['2016-08-14', '2018-10-16', '2017-03-26', '2017-05-11', '2017-08-13', '2017-10-08',
                 '2017-12-10', '2018-04-22', '2018-06-24', '2018-09-30', '2018-12-02']
b7['ds'] = b7.b8
b7 = b7[~b7['ds'].isin(b14)]
b7 = df_daily_re