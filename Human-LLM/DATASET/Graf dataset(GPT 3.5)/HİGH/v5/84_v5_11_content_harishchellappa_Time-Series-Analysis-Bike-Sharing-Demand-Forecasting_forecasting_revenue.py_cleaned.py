import pandas as pd
from fbprophet import Prophet
from sklearn.metrics import mean_squared_error
from math import sqrt
from datetime import datetime, date
b1 = pd.read_excel('C:/Users/tusha/Desktop/newtable.xlsx', b25='newtable')
b1['start_time'] = pd.to_datetime(b1['start_time'], b2 = "%d/%m/%Y %I:%M:%S %p")
b1['end_time'] = pd.to_datetime(b1['end_time'], b2 = "%d/%m/%Y %I:%M:%S %p")
def fonk1(pass_type, duration, time):
    a1 = 1.75
    if time < date(b3 = 2018, month=7, day=12):
        a1 = 3.5
    b4 = duration
    if duration % 30 != 0:
        b4 += 1
    if pass_type in ['Monthly Pass', 'Annual Pass', 'One Day Pass', 'Flex Pass']:
        b4 -= 1
        if b4 < 0:
            b4 = 0
    return a1 * b4
b1['revenue'] = b1.apply(lambda row: fonk1(row['passholder_type'], row['trip_duration'], row['start_time'].date()), b5 = 1)
b6 = b1.groupby(b1['start_time'].dt.date)['revenue'].sum().reset_index()
b6['start_time'] = pd.to_datetime(b6['start_time'])
b7 = pd.DataFrame()
b8 = []
b9 = []
def fonk2(b1):
    b10 = b1.rename(columns={'start_time': 'ds', 'revenue': 'y'})
    return b10
def fonk3(b1, b11 = -184):
    b12 = ['2016-08-14', '2018-10-16', '2017-03-26', '2017-05-11', '2017-08-13', '2017-10-08',
                     '2017-12-10', '2018-04-22', '2018-06-24', '2018-09-30', '2018-12-02']
    b1 = b1[~b1['start_time'].isin(b12)]
    b13 = b1.iloc[:b11]
    b14 = b1.iloc[b11:]
    return b13, b14
for column in b6.columns:
    train_data, b15 = fonk3(b6)
    b16 = Prophet(yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False)
    b16.fit(fonk2(train_data))
    b17 = b16.make_future_dataframe(periods=len(b15) + 90 + 3, freq='D')
    b18 = b16.predict(b17)
    b7[column] = b18['yhat']
    b19 = b15['y']
    b20 = b7[column].tail(len(b15))
    b9.append(sqrt(mean_squared_error(b19, b20)))
    b21 = train_data['y']
    b22 = b7[column].iloc[:-184 - 93]
    b8.append(sqrt(mean_squared_error(b21, b22)))
b7['ds'] = b18['ds']
b12 = ['2016-08-14', '2018-10-16', '2017-03-26', '2017-05-11', '2017-08-13', '2017-10-08',
                 '2017-12-10', '2018-04-22', '2018-06-24', '2018-09-30', '2018-12-02']
b6 = b6[~b6['start_time'].isin(b12)]
b23 = pd.DataFrame(b8)
b24 = pd.DataFrame(b9)
with pd.ExcelWriter('outputY_Revenue.xlsx') as writer:
    b6.to_excel(writer, b25 = 'actual(Y)', index=False)
    b7.to_excel(writer, b25 = 'predicted(Y)', index=False)
    b23.to_excel(writer, b25 = 'mse_trn(Y)', index=False)
    b24.to_excel(writer, b25 = 'mse_tst(Y)', index=False)