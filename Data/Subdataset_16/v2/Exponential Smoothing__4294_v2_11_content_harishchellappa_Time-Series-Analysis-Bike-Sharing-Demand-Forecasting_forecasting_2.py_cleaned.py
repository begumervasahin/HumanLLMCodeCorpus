import pandas as pd
import numpy as np
from fbprophet import Prophet
from sklearn.metrics import mean_squared_error
from math import sqrt
b1 = pd.read_excel('newtable.xlsx', b27='newtable')
b1['start_time'] = pd.to_datetime(b1['start_time'], b2 = "%d/%m/%Y %I:%M:%S %p")
b1['end_time'] = pd.to_datetime(b1['end_time'], b2 = "%d/%m/%Y %I:%M:%S %p")
b3 = pd.pivot_table(b1[['start_station', 'start_time']], aggfunc='count', b6=b1['start_time'].dt.date, columns=['start_station'], fill_value=0)
b4 = [
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
b3.b24(b5 = b4, axis=1, inplace=True)
b3.b6 = pd.to_datetime(b3.b6)
b7 = pd.DataFrame()
b8 = []
b9 = []
def fonk1(b1, b10 = 0):
    b11 = pd.DataFrame()
    b11['ds'] = b1.b6
    b11['y'] = b1.iloc[:, b10].values
    return b11
def fonk2(b3, b12 = -184):
    b13 = [
        '2016-08-14', '2018-10-16', '2017-03-26', '2017-05-11', '2017-08-13', '2017-10-08',
        '2017-12-10', '2018-04-22', '2018-06-24', '2018-09-30', '2018-12-02'
    ]
    b3 = b3[~b3.b6.isin(b13)]
    b14 = b3.iloc[:b12]
    b15 = b3.iloc[b12:]
    return fonk1(b14, i), fonk1(b15, i)
for i, v in enumerate(b3.columns):
    trn, b16 = fonk2(b3, b12=-184)
    b17 = Prophet(yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False)
    b17.fit(trn)
    b18 = b17.make_future_dataframe(periods=len(b16) + 90 + 3, freq='D')
    b19 = b17.predict(b18)
    b7[v] = b19['yhat']
    b20 = b16['y']
    b21 = b7[v].iloc[-184:]
    b9.append(sqrt(mean_squared_error(b20, b21)))
    b22 = trn['y']
    b23 = b7[v].iloc[:-184-93]
    b8.append(sqrt(mean_squared_error(b22, b23)))
b7['ds'] = b19['ds']
b3['ds'] = b3.b6
b3 = b3[~b3['ds'].isin(b13)]
b3.reset_index(b24 = True, inplace=True)
b25 = pd.DataFrame(b8, columns=['MSE_Train'])
b26 = pd.DataFrame(b9, columns=['MSE_Test'])
with pd.ExcelWriter('outputY.xlsx') as writer:
    b3.to_excel(writer, b27 = 'actual(Y)')
    b7.to_excel(writer, b27 = 'predicted(Y)')
    b25.to_excel(writer, b27 = 'b8(Y)')
    b26.to_excel(writer, b27 = 'b9(Y)')