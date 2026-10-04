import pandas as pd
import numpy as np
from fbprophet import Prophet
from sklearn.metrics import mean_squared_error
from math import sqrt
df = pd.read_excel('newtable.xlsx', sheet_name='newtable')
df['start_time'] = pd.to_datetime(df['start_time'], format="%d/%m/%Y %I:%M:%S %p")
df['end_time'] = pd.to_datetime(df['end_time'], format="%d/%m/%Y %I:%M:%S %p")
df_d = pd.pivot_table(df[['start_station', 'start_time']], aggfunc='count', index=df['start_time'].dt.date, columns=['start_station'], fill_value=0)
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
df_d.drop(labels=columns_to_remove, axis=1, inplace=True)
df_d.index = pd.to_datetime(df_d.index)
df_o = pd.DataFrame()
mse_trn = []
mse_tst = []
def prophet_inputize(df, column_num=0):
    df_1 = pd.DataFrame()
    df_1['ds'] = df.index
    df_1['y'] = df.iloc[:, column_num].values
    return df_1
def prepare_data(df_d, test_period=-184):
    dates_to_remove = [
        '2016-08-14', '2018-10-16', '2017-03-26', '2017-05-11', '2017-08-13', '2017-10-08',
        '2017-12-10', '2018-04-22', '2018-06-24', '2018-09-30', '2018-12-02'
    ]
    df_d = df_d[~df_d.index.isin(dates_to_remove)]
    df_trn = df_d.iloc[:test_period]
    df_tst = df_d.iloc[test_period:]
    return prophet_inputize(df_trn, i), prophet_inputize(df_tst, i)
for i, v in enumerate(df_d.columns):
    trn, tst = prepare_data(df_d, test_period=-184)
    model = Prophet(yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False)
    model.fit(trn)
    future = model.make_future_dataframe(periods=len(tst) + 90 + 3, freq='D')
    forecast = model.predict(future)
    df_o[v] = forecast['yhat']
    y_actual_tst = tst['y']
    y_predicted_tst = df_o[v].iloc[-184:]
    mse_tst.append(sqrt(mean_squared_error(y_actual_tst, y_predicted_tst)))
    y_actual_trn = trn['y']
    y_predicted_trn = df_o[v].iloc[:-184-93]
    mse_trn.append(sqrt(mean_squared_error(y_actual_trn, y_predicted_trn)))
df_o['ds'] = forecast['ds']
df_d['ds'] = df_d.index
df_d = df_d[~df_d['ds'].isin(dates_to_remove)]
df_d.reset_index(drop=True, inplace=True)
mse_trn_df = pd.DataFrame(mse_trn, columns=['MSE_Train'])
mse_tst_df = pd.DataFrame(mse_tst, columns=['MSE_Test'])
with pd.ExcelWriter('outputY.xlsx') as writer:
    df_d.to_excel(writer, sheet_name='actual(Y)')
    df_o.to_excel(writer, sheet_name='predicted(Y)')
    mse_trn_df.to_excel(writer, sheet_name='mse_trn(Y)')
    mse_tst_df.to_excel(writer, sheet_name='mse_tst(Y)')