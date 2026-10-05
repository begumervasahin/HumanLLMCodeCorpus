import pandas as pd
from fbprophet import Prophet
from sklearn.metrics import mean_squared_error
from math import sqrt
b1 = pd.read_excel('newtable.xlsx', b25='newtable')
b1['start_time'] = pd.to_datetime(b1['start_time'], b2 = "%d/%m/%Y %I:%M:%S %p")
b1['end_time'] = pd.to_datetime(b1['end_time'], b2 = "%d/%m/%Y %I:%M:%S %p")
b3 = pd.pivot_table(b1[['start_station', 'start_time']], aggfunc='count', b6=b1['start_time'].dt.date, b5=['start_station'], fill_value=0)
b4 = [
    3021, 3053, 3055, 3059, 3060, 3061, 3079, 3080,
    4108, 4138, 4142, 4143, 4144, 4146, 4147, 4148,
    4149, 4150, 4151, 4152, 4153, 4154, 4155, 4156,
    4157, 4158, 4159, 4160, 4162, 4163, 4165, 4166,
    4167, 4169, 4170, 4174, 4176, 4177, 4180, 4181,
    4183, 4194, 4244, 4276
]
b3.drop(b5 = b4, inplace=True)
b3.b6 = pd.to_datetime(b3.b6)
def fonk1(b1):
    return pd.DataFrame({'ds': b1.b6, 'y': b1.values})
def fonk2(b3, b7 = -184):
    b8 = ['2016-08-14', '2018-10-16', '2017-03-26', '2017-05-11', '2017-08-13', '2017-10-08',
                     '2017-12-10', '2018-04-22', '2018-06-24', '2018-09-30', '2018-12-02']
    b9 = b3.loc[~b3.b6.isin(b8)].iloc[:b7]
    b10 = b3.iloc[b7:]
    return fonk1(b9), fonk1(b10)
b11 = pd.DataFrame()
b12 = []
b13 = []
for station in b3.b5:
    train_data, b14 = fonk2(b3)
    b15 = Prophet(yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False)
    b15.fit(train_data)
    b16 = b15.make_future_dataframe(periods=len(b14) + 90 + 3, freq='D')
    b17 = b15.predict(b16)
    b11[station] = b17['yhat']
    b18 = b14['y']
    b19 = b11[station].tail(184)
    b13.append(sqrt(mean_squared_error(b18, b19)))
    b20 = train_data['y']
    b21 = b11[station].iloc[:-277]
    b12.append(sqrt(mean_squared_error(b20, b21)))
b22 = b3.reset_index(drop=True)
b23 = pd.DataFrame(b12)
b24 = pd.DataFrame(b13)
with pd.ExcelWriter('outputY.xlsx') as writer:
    b22.to_excel(writer, b25 = 'actual(Y)')
    b11.to_excel(writer, b25 = 'predicted(Y)')
    b23.to_excel(writer, b25 = 'mse_trn(Y)')
    b24.to_excel(writer, b25 = 'mse_tst(Y)')