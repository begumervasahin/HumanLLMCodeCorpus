import pandas as pd
from fbprophet import Prophet
from sklearn.metrics import mean_squared_error
from math import sqrt
from datetime import datetime, date
b1 = pd.read_excel('C:/Users/tusha/Desktop/newtable.xlsx', b31='newtable')
b1['start_time'] = pd.to_datetime(b1['start_time'], b2 = "%d/%m/%Y %I:%M:%S %p")
b1['end_time'] = pd.to_datetime(b1['end_time'], b2 = "%d/%m/%Y %I:%M:%S %p")
def fonk1(pass_type, duration, time):
    a1 = 1.75
    if time < date(b3 = 2018, month=7, day=12):
        a1 = 3.5
    b4 = int(duration / 30)
    if duration % 30 != 0:
        b4 += 1
    if pass_type in ['Monthly Pass', 'Annual Pass', 'One Day Pass', 'Flex Pass']:
        b4 -= 1
        if b4 < 0:
            b4 = 0
    return a1 * b4
b1['revenue'] = b1.apply(lambda row: fonk1(row['passholder_type'], row['trip_duration'], row['start_time'].date()), b5 = 1)
b6 = pd.pivot_table(b1[['revenue', 'start_time']], aggfunc='sum', b7=b1['start_time'].dt.date, columns=['revenue'], fill_value=0)
b6.b7 = pd.to_datetime(b6.b7)
b8 = pd.DataFrame()
b9 = []
b10 = []
def fonk2(b1, b11 = 0):
    b12 = pd.DataFrame()
    b12['ds'] = b1.b7
    b12['y'] = list(b1.iloc[:, b11])
    return b12
def fonk3(b1, b13 = 'D', train_prop=0.80):
    b14 = b1.resample(b13).sum()
    b15 = ['2016-08-14', '2018-10-16', '2017-03-26', '2017-05-11', '2017-08-13', '2017-10-08',
                     '2017-12-10', '2018-04-22', '2018-06-24', '2018-09-30', '2018-12-02']
    b14 = b14[~b14.b7.isin(b15)]
    b16 = int(train_prop * len(b14))
    b17 = b14.iloc[:b16]
    b18 = b14.iloc[b16:]
    b19 = fonk2(b17)
    b20 = fonk2(b18)
    return b19, b20
for i, column in enumerate(b6.columns):
    train_data, b21 = fonk3(b6)
    b22 = Prophet(yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=True)
    b22.fit(train_data)
    b23 = b22.make_future_dataframe(periods=len(b21), freq='D')
    b24 = b22.predict(b23)
    b8[column] = b24['yhat']
    b25 = b21['y']
    b26 = b8[column].tail(len(b21))
    b10.append(sqrt(mean_squared_error(b25, b26)))
    b27 = train_data['y']
    b28 = b8[column].iloc[:len(train_data)]
    b9.append(sqrt(mean_squared_error(b27, b28)))
b8['ds'] = b24['ds']
b15 = ['2016-08-14', '2018-10-16', '2017-03-26', '2017-05-11', '2017-08-13', '2017-10-08',
                 '2017-12-10', '2018-04-22', '2018-06-24', '2018-09-30', '2018-12-02']
b6['ds'] = b6.b7
b6 = b6[~b6['ds'].isin(b15)]
b6 = b6.reset_index(drop=True)
b29 = pd.DataFrame(b9)
b30 = pd.DataFrame(b10)
with pd.ExcelWriter('outputY_Passholder.xlsx') as writer:
    b6.to_excel(writer, b31 = 'actual(YWD)')
    b8.to_excel(writer, b31 = 'predicted(YWD)')
    b29.to_excel(writer, b31 = 'b9(YWD)')
    b30.to_excel(writer, b31 = 'b10(YWD)')