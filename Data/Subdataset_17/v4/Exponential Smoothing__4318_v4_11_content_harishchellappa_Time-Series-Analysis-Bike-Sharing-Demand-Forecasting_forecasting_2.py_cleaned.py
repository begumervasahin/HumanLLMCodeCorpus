
import pandas as pd
import numpy as np
from fbprophet import Prophet
from datetime import datetime
from sklearn.metrics import mean_squared_error
from math import sqrt
import matplotlib.pyplot as plt
df = pd.read_excel('newtable.xlsx', sheet_name='newtable')
df['start_time'] = pd.to_datetime(df['start_time'], format="%d/%m/%Y %I:%M:%S %p")
df['end_time'] = pd.to_datetime(df['end_time'], format="%d/%m/%Y %I:%M:%S %p")
df_pivot = pd.pivot_table(df[['start_station', 'start_time']],
                          index=df['start_time'].dt.date,
                          columns=['start_station'],
                          aggfunc='count',
                          fill_value=0)
columns_to_remove = [
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
df_pivot.drop(labels=columns_to_remove, axis=1, inplace=True)
df_pivot.index = pd.to_datetime(df_pivot.index)
df_forecast = pd.DataFrame()
mse_train = []
mse_test = []
def prepare_prophet_input(df, column_num=0):
    return pd.DataFrame({'ds': df.index, 'y': df.iloc[:, column_num].values})
def prepare_data(df, test_period=-184):
    dates_to_remove = [
        '2016-08-14', '2018-10-16', '2017-03-26', '2017-05-11', '2017-08-13', '2017-10-08',
        '2017-12-10', '2018-04-22', '2018-06-24', '2018-09-30', '2018-12-02'
    ]
    df_cleaned = df[~df.index.isin(pd.to_datetime(dates_to_remove))]
    df_train = df_cleaned.iloc[:test_period]
    df_test = df_cleaned.iloc[test_period:]
    return prepare_prophet_input(df_train, column_num), prepare_prophet_input(df_test, column_num)
for column_num, station in enumerate(df_pivot.columns):
    train_data, test_data = prepare_data(df_pivot, test_period=-184)
    model = Prophet(yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False)
    model.fit(train_data)
    future = model.make_future_dataframe(periods=len(test_data) + 90 + 3, freq='D')
    forecast = model.predict(future)
    df_forecast[station] = forecast['yhat']
    y_actual_test = test_data['y']
    y_predicted_test = df_forecast[station].iloc[-184:]
    mse_test.append(sqrt(mean_squared_error(y_actual_test, y_predicted_test)))
    y_actual_train = train_data['y']
    y_predicted_train = df_forecast[station].iloc[:-184-93]
    mse_train.append(sqrt(mean_squared_error(y_actual_train, y_predicted_train)))
df_forecast['ds'] = forecast['ds']
dates_to_remove = [
    '2016-08-14', '2018-10-16', '2017-03-26', '2017-05-11', '2017-08-13', '2017-10-08',
    '2017-12-10', '2018-04-22', '2018-06-24', '2018-09-30', '2018-12-02'
]
df_pivot['ds'] = df_pivot.index
df_pivot = df_pivot[~df_pivot['ds'].isin(pd.to_datetime(dates_to_remove))]
df_pivot.reset_index(drop=True, inplace=True)
mse_train_df = pd.DataFrame(mse_train, columns=['MSE_Train'])
mse_test_df = pd.DataFrame(mse_test, columns=['MSE_Test'])
with pd.ExcelWriter('outputY.xlsx') as writer:
    df_pivot.to_excel(writer, sheet_name='actual(Y)')
    df_forecast.to_excel(writer, sheet_name='predicted(Y)')
    mse_train_df.to_excel(writer, sheet_name='mse_train(Y)')
    mse_test_df.to_excel(writer, sheet_name='mse_test(Y)')
df_forecast.tail()
test_data.tail()
df_forecast.loc[df_forecast.index[int(0.8 * len(df_forecast.index)):]].plot(x='ds', y=station)
test_data.plot(x='ds', y='y')
y_actual = test_data['y']
y_predicted = df_forecast[station][df_forecast.index[int(0.8 * len(df_forecast.index)):]]
mse = sqrt(mean_squared_error(y_actual, y_predicted))
print(f'Mean Squared Error: {mse}')
dft1 = pd.DataFrame(list(df_pivot['index']), columns=['ds'])
dft1.rename(columns={'0': 'ds'}, inplace=True)
dft1['y'] = list(df_pivot.iloc[:, 0])
dft1.head()
dft2 = dft1.iloc[0:-25, :]
dft2.tail()
dftv = dft1.iloc[-25:, :]
dftv.head()
dft2.plot(x='ds', y='y')
dftv.plot(x='ds', y='y')
model = Prophet()
model.fit(dft2)
future = model.make_future_dataframe(periods=25)
forecast = model.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
fig1 = model.plot(forecast)
plt.show()