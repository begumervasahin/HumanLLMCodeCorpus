
import pandas as pd
import numpy as np
from fbprophet import Prophet
from datetime import datetime
from sklearn.metrics import mean_squared_error
from math import sqrt
import matplotlib.pyplot as plt
b1 = pd.read_excel('newtable.xlsx', b30='newtable')
b1['start_time'] = pd.to_datetime(b1['start_time'], b2 = "%d/%m/%Y %I:%M:%S %p")
b1['end_time'] = pd.to_datetime(b1['end_time'], b2 = "%d/%m/%Y %I:%M:%S %p")
b3 = pd.pivot_table(b1[['start_station', 'start_time']],
                          b4 = b1['start_time'].dt.date,
                          b5 = ['start_station'],
                          b6 = 'count',
                          b7 = 0)
b8 = [
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
b3.b27(b9 = b8, axis=1, inplace=True)
b3.b4 = pd.to_datetime(b3.b4)
b10 = pd.DataFrame()
b11 = []
b12 = []
def fonk1(b1, b13 = 0):
    return pd.DataFrame({'ds': b1.b4, 'y': b1.iloc[:, b13].values})
def fonk2(b1, b14 = -184):
    b15 = [
        '2016-08-14', '2018-10-16', '2017-03-26', '2017-05-11', '2017-08-13', '2017-10-08',
        '2017-12-10', '2018-04-22', '2018-06-24', '2018-09-30', '2018-12-02'
    ]
    b16 = b1[~b1.b4.isin(pd.to_datetime(b15))]
    b17 = b16.iloc[:b14]
    b18 = b16.iloc[b14:]
    return fonk1(b17, b13), fonk1(b18, b13)
for b13, station in enumerate(b3.b5):
    train_data, b19 = fonk2(b3, b14=-184)
    b20 = Prophet(yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False)
    b20.fit(train_data)
    b21 = b20.make_future_dataframe(periods=len(b19) + 90 + 3, freq='D')
    b22 = b20.predict(b21)
    b10[station] = b22['yhat']
    b23 = b19['y']
    b24 = b10[station].iloc[-184:]
    b12.append(sqrt(mean_squared_error(b23, b24)))
    b25 = train_data['y']
    b26 = b10[station].iloc[:-184-93]
    b11.append(sqrt(mean_squared_error(b25, b26)))
b10['ds'] = b22['ds']
b15 = [
    '2016-08-14', '2018-10-16', '2017-03-26', '2017-05-11', '2017-08-13', '2017-10-08',
    '2017-12-10', '2018-04-22', '2018-06-24', '2018-09-30', '2018-12-02'
]
b3['ds'] = b3.b4
b3 = b3[~b3['ds'].isin(pd.to_datetime(b15))]
b3.reset_index(b27 = True, inplace=True)
b28 = pd.DataFrame(b11, b5=['MSE_Train'])
b29 = pd.DataFrame(b12, b5=['MSE_Test'])
with pd.ExcelWriter('outputY.xlsx') as writer:
    b3.to_excel(writer, b30 = 'actual(Y)')
    b10.to_excel(writer, b30 = 'predicted(Y)')
    b28.to_excel(writer, b30 = 'b11(Y)')
    b29.to_excel(writer, b30 = 'b12(Y)')
b10.tail()
b19.tail()
b10.loc[b10.b4[int(0.8 * len(b10.b4)):]].plot(b31 = 'ds', y=station)
b19.plot(b31 = 'ds', y='y')
b32 = b19['y']
b33 = b10[station][b10.b4[int(0.8 * len(b10.b4)):]]
b34 = sqrt(mean_squared_error(b32, b33))
print(f'Mean Squared Error: {b34}')
b35 = pd.DataFrame(list(b3['b4']), b5=['ds'])
b35.rename(b5 = {'0': 'ds'}, inplace=True)
b35['y'] = list(b3.iloc[:, 0])
b35.head()
b36 = b35.iloc[0:-25, :]
b36.tail()
b37 = b35.iloc[-25:, :]
b37.head()
b36.plot(b31 = 'ds', y='y')
b37.plot(b31 = 'ds', y='y')
b20 = Prophet()
b20.fit(b36)
b21 = b20.make_future_dataframe(periods=25)
b22 = b20.predict(b21)
b22[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
b38 = b20.plot(b22)
plt.show()