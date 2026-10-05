import pandas as pd
from fbprophet import Prophet
from sklearn.metrics import mean_squared_error
from math import sqrt
from datetime import datetime, date
b1 = pd.read_excel('C:/Users/tusha/Desktop/newtable.xlsx', b29='newtable')
b1['start_time'] = pd.to_datetime(b1['start_time'], b2 = "%d/%m/%Y %I:%M:%S %p")
b1['end_time'] = pd.to_datetime(b1['end_time'], b2 = "%d/%m/%Y %I:%M:%S %p")
def fonk1(passtype, duration, time):
    a1 = 1.75
    if time < date(b3 = 2018, month=7, day=12):
        a1 = 3.5
    b4 = int(duration / 30)
    if duration % 30 != 0:
        b4 += 1
    if passtype in ['Monthly Pass', 'Annual Pass', 'One Day Pass', 'Flex Pass']:
        b4 -= 1
        if b4 < 0:
            b4 = 0
    return a1 * b4
b1['revenue'] = b1.apply(lambda row: fonk1(row['passholder_type'], row['trip_duration'], row['start_time'].date()), b5 = 1)
b6 = pd.pivot_table(b1[['revenue', 'start_time']], aggfunc='sum', b7=b1['start_time'].dt.date, fill_value=0)
b6.b7 = pd.to_datetime(b6.b7)
b8 = pd.DataFrame()
b9 = []
b10 = []
def fonk2(b1, b11 = 0):
    b12 = pd.DataFrame()
    b12['ds'] = b1.b7
    b12['y'] = list(b1.iloc[:, b11])
    return b12
def fonk3(b1, b13 = 'D', test_size=-184):
    b14 = ['2016-08-14', '2018-10-16', '2017-03-26', '2017-05-11', '2017-08-13', '2017-10-08',
                     '2017-12-10', '2018-04-22', '2018-06-24', '2018-09-30', '2018-12-02']
    b1['temp'] = b1.b7
    b1 = b1[~b1['temp'].isin(b14)]
    b1.drop('temp', b5 = 1, inplace=True)
    b15 = b1.iloc[:test_size]
    b16 = b1.iloc[test_size:]
    b17 = fonk2(b15)
    b18 = fonk2(b16)
    return b17, b18
for i, column in enumerate(b6.columns):
    train_data, b19 = fonk3(b6)
    b20 = Prophet(yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False)
    b20.fit(train_data)
    b21 = b20.make_future_dataframe(periods=len(b19)+90+3, freq='D')
    b22 = b20.predict(b21)
    b8[column] = b22['yhat']
    b23 = b19['y']
    b24 = b8[column].tail(len(b19))
    b10.append(sqrt(mean_squared_error(b23, b24)))
    b25 = train_data['y']
    b26 = b8[column].iloc[:-184-93]
    b9.append(sqrt(mean_squared_error(b25, b26)))
b8['ds'] = b22['ds']
b14 = ['2016-08-14', '2018-10-16', '2017-03-26', '2017-05-11', '2017-08-13', '2017-10-08',
                 '2017-12-10', '2018-04-22', '2018-06-24', '2018-09-30', '2018-12-02']
b6['ds'] = b6.b7
b6 = b6[~b6['ds'].isin(b14)]
b6 = b6.reset_index(drop=True)
b27 = pd.DataFrame(b9)
b28 = pd.DataFrame(b10)
with pd.ExcelWriter('outputY_Revenue.xlsx') as writer:
    b6.to_excel(writer, b29 = 'actual(Y)')
    b8.to_excel(writer, b29 = 'predicted(Y)')
    b27.to_excel(writer, b29 = 'mse_trn(Y)')
    b28.to_excel(writer, b29 = 'mse_tst(Y)')