import pandas as pd
from fbprophet import Prophet
from sklearn.metrics import mean_squared_error
from math import sqrt
def fonk1(file_path, b1):
    return pd.read_excel(file_path, b1 = b1)
def fonk2(b7, b3):
    for col in b3:
        b7[col] = pd.to_datetime(b7[col], b2 = "%d/%b13/%Y %I:%M:%S %p")
    return b7
def fonk3(b7, b3):
    return b7.drop(b3 = b3, b8=1)
def fonk4(b7, column_index):
    b4 = pd.DataFrame()
    b4['ds'] = b7.b22
    b4['y'] = b7.iloc[:, column_index].tolist()
    return b4
def fonk5(b7, b5 = 'D', test_length=-184):
    b6 = [
        '2016-08-14', '2018-10-16', '2017-03-26', '2017-05-11', '2017-08-13', '2017-10-08',
        '2017-12-10', '2018-04-22', '2018-06-24', '2018-09-30', '2018-12-02'
    ]
    b7['temp'] = b7.b22
    for date in b6:
        b7 = b7[b7.temp != date]
    b7.drop('temp', b8 = 1, inplace=True)
    b9 = b7.iloc[:test_length]
    b10 = b7.iloc[test_length:]
    b11 = fonk4(b9, i)
    b12 = fonk4(b10, i)
    b13 = Prophet(yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False)
    b13.fit(b11)
    b14 = b13.make_future_dataframe(periods=len(b10) + 90 + 3, freq=b5)
    b15 = b13.predict(b14)
    b23[v] = b15['yhat']
    b16 = b11['y']
    b17 = b23[v].iloc[:-187]
    b24.append(sqrt(mean_squared_error(b16, b17)))
    b18 = b12['y']
    b19 = b23[v].iloc[-184:]
    b25.append(sqrt(mean_squared_error(b18, b19)))
b7 = fonk1('newtable.xlsx', 'newtable')
b7 = fonk2(b7, ['start_time', 'end_time'])
b20 = pd.pivot_table(b7[['start_station', 'start_time']], aggfunc='count', b22=b7['start_time'].dt.date, b3=['start_station'], fill_value=0)
b21 = [
    ('start_time', 3021), ('start_time', 3053), ('start_time', 3055), ('start_time', 3059),
    ('start_time', 3060), ('start_time', 3061), ('start_time', 3079), ('start_time', 3080),
    ('start_time', 4108), ('start_time', 4138), ('start_time', 4142), ('start_time', 4143),
    ('start_time', 4144), ('start_time', 4146), ('start_time', 4147), ('start_time', 4148),
    ('start_time', 4149), ('start_time', 4150), ('start_time', 4151), ('start_time', 4152),
    ('start_time', 4153), ('start_time', 4154), ('start_time', 4155), ('start_time', 4156),
    ('start_time', 4157), ('start_time', 4158), ('start_time', 4159), ('start_time', 4160),
    ('start_time', 4162), ('start_time', 4163), ('start_time', 4165), ('start_time', 4166),
    ('start_time', 4167), ('start_time', 4169), ('start_time', 4170), ('start_time', 4174),
    ('start_time', 4176), ('start_time', 4177), ('start_time', 4180), ('start_time', 4181),
    ('start_time', 4183), ('start_time', 4194), ('start_time', 4244), ('start_time', 4276)
]
b20 = fonk3(b20, b21)
b20.b22 = pd.to_datetime(b20.b22)
b23 = pd.DataFrame()
b24 = []
b25 = []
for i, v in enumerate(b20.b3):
    fonk5(b20)
b23['ds'] = b15['ds']
b20['ds'] = b20.b22
for date in b6:
    b20 = b20[b20.ds != date]
b20 = b20.reset_index(drop=True)
b26 = pd.DataFrame(b24)
b27 = pd.DataFrame(b25)
with pd.ExcelWriter('outputY.xlsx') as writer:
    b20.to_excel(writer, b1 = 'actual(Y)')
    b23.to_excel(writer, b1 = 'predicted(Y)')
    b26.to_excel(writer, b1 = 'mse_trn(Y)')
    b27.to_excel(writer, b1 = 'mse_tst(Y)')