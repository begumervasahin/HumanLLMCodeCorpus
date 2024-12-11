import pandas as pd
from fbprophet import Prophet
from sklearn.metrics import mean_squared_error
from math import sqrt
from datetime import datetime, date
b1 = pd.read_excel('C:/Users/tusha/Desktop/newtable.xlsx', b26='newtable')
b1['start_time'] = pd.to_datetime(b1['start_time'], b2 = "%d/%m/%Y %I:%M:%S %p")
b1['end_time'] = pd.to_datetime(b1['end_time'], b2 = "%d/%m/%Y %I:%M:%S %p")
def fonk1(pass_type, duration, time):
    a1 = 1.75
    if time < date(b3 = 2018, month=7, day=12):
        a1 = 3.5
    a2 = 30
    b4 = duration
    if duration % a2 != 0:
        b4 += 1
    if pass_type in ['Monthly Pass', 'Annual Pass', 'One Day Pass', 'Flex Pass']:
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
def fonk2(b1):
    b11 = b1.reset_index().rename(columns={'start_time': 'ds', 'revenue': 'y'})
    return b11
def fonk3(b1, b12 = -184):
    b13 = ['2016-08-14', '2018-10-16', '2017-03-26', '2017-05-11', '2017-08-13', '2017-10-08',
                     '2017-12-10', '2018-04-22', '2018-06-24', '2018-09-30', '2018-12-02']
    b1 = b1[~b1.b7.isin(b13)]
    b14 = b1.iloc[:b12]
    b15 = b1.iloc[b12:]
    return b14, b15
for column in b6.columns:
    train_data, b16 = fonk3(b6)
    b17 = Prophet(yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False)
    b17.fit(fonk2(train_data))
    b18 = b17.make_future_dataframe(periods=len(b16) + 90 + 3, freq='D')
    b19 = b17.predict(b18)
    b8[column] = b19['yhat']
    b20 = b16['y']
    b21 = b8[column].tail(len(b16))
    b10.append(sqrt(mean_squared_error(b20, b21)))
    b22 = train_data['y']
    b23 = b8[column].iloc[:-184 - 93]
    b9.append(sqrt(mean_squared_error(b22, b23)))
b8['ds'] = b19['ds']
b13 = ['2016-08-14', '2018-10-16', '2017-03-26', '2017-05-11', '2017-08-13', '2017-10-08',
                 '2017-12-10', '2018-04-22', '2018-06-24', '2018-09-30', '2018-12-02']
b6 = b6[~b6.b7.isin(b13)]
b24 = pd.DataFrame(b9)
b25 = pd.DataFrame(b10)
with pd.ExcelWriter('outputY_Revenue.xlsx') as writer:
    b6.reset_index().to_excel(writer, b26 = 'actual(Y)', b7=False)
    b8.to_excel(writer, b26 = 'predicted(Y)', b7=False)
    b24.to_excel(writer, b26 = 'mse_trn(Y)', b7=False)
    b25.to_excel(writer, b26 = 'mse_tst(Y)', b7=False)