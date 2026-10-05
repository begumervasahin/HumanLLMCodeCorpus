import pandas as pd
from fbprophet import Prophet
from sklearn.metrics import mean_squared_error
from math import sqrt
from datetime import datetime, date
def fonk1(passtype, duration, time):
    a1 = 1.75
    if time < date(b1 = 2018, month=7, day=12):
        a1 = 3.5
    b2 = int(duration / 30)
    b3 = duration % 30
    if b3 != 0:
        b2 += 1
    if passtype in ['Monthly Pass', 'Annual Pass', 'One Day Pass', 'Flex Pass']:
        b2 -= 1
    if b2 < 0:
        b2 = 0
    return a1 * b2
b4 = pd.read_excel('C:/Users/tusha/Desktop/newtable.xlsx', b32='newtable')
b4['start_time'] = pd.to_datetime(b4['start_time'], b5 = "%d/%m/%Y %I:%M:%S %p")
b4['end_time'] = pd.to_datetime(b4['end_time'], b5 = "%d/%m/%Y %I:%M:%S %p")
b4['revenue'] = b4.apply(lambda row: fonk1(row['passholder_type'], row['trip_duration'], row['start_time'].date()), b6 = 1)
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
def fonk3(b4, b14 = 'D', train_proportion=0.80):
    b15 = b4.resample(b14).sum()
    b16 = ['2016-08-14', '2018-10-16', '2017-03-26', '2017-05-11', '2017-08-13', '2017-10-08',
                 '2017-12-10', '2018-04-22', '2018-06-24', '2018-09-30', '2018-12-02']
    b15['temp'] = b15.b8
    b15 = b15[~b15['temp'].isin(b16)]
    b15.drop('temp', b6 = 1, inplace=True)
    b17 = int(train_proportion * len(b15))
    b18 = b15.iloc[:b17]
    b19 = b15.iloc[b17:]
    b20 = fonk2(b18)
    b21 = fonk2(b19)
    return b20, b21
for i, column in enumerate(b7.columns):
    train_data, b22 = fonk3(b7)
    b23 = Prophet(yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=True)
    b23.fit(train_data)
    b24 = b23.make_future_dataframe(periods=len(b22), freq='D')
    b25 = b23.predict(b24)
    b9[column] = b25['yhat']
    b26 = b22['y']
    b27 = b9[column].tail(len(b22))
    b11.append(sqrt(mean_squared_error(b26, b27)))
    b28 = train_data['y']
    b29 = b9[column].iloc[:len(train_data)]
    b10.append(sqrt(mean_squared_error(b28, b29)))
b9['ds'] = b25['ds']
b16 = ['2016-08-14', '2018-10-16', '2017-03-26', '2017-05-11', '2017-08-13', '2017-10-08',
             '2017-12-10', '2018-04-22', '2018-06-24', '2018-09-30', '2018-12-02']
b7['ds'] = b7.b8
b7 = b7[~b7['ds'].isin(b16)]
b7 = b7.reset_index(drop=True)
b30 = pd.DataFrame(b10)
b31 = pd.DataFrame(b11)
with pd.ExcelWriter('outputY_Passholder.xlsx') as writer:
    b7.to_excel(writer, b32 = 'actual(YWD)')
    b9.to_excel(writer, b32 = 'predicted(YWD)')
    b30.to_excel(writer, b32 = 'b10(YWD)')
    b31.to_excel(writer, b32 = 'b11(YWD)')