
import pandas as pd
import numpy as np
from fbprophet import Prophet
from datetime import datetime, date
from sklearn.metrics import mean_squared_error
from math import sqrt
import matplotlib.pyplot as plt
df = pd.read_excel('C:/Users/tusha/Desktop/newtable.xlsx', sheet_name='newtable')
df['start_time'] = pd.to_datetime(df['start_time'], format="%d/%m/%Y %I:%M:%S %p")
df['end_time'] = pd.to_datetime(df['end_time'], format="%d/%m/%Y %I:%M:%S %p")
def calculate_revenue(passtype, duration, start_date):
    per_thirty = 1.75
    if start_date < date(2018, 7, 12):
        per_thirty = 3.5
    qty = int(duration / 30)
    if duration % 30 != 0:
        qty += 1
    if passtype in ['Monthly Pass', 'Annual Pass', 'One Day Pass', 'Flex Pass']:
        qty -= 1
    return max(0, per_thirty * qty)
df['revenue'] = df.apply(lambda row: calculate_revenue(row['passholder_type'], row['trip_duration'], row['start_time'].date()), axis=1)
df_pivot = df.pivot_table(values='revenue', index=df['start_time'].dt.date, aggfunc='sum', fill_value=0)
df_pivot.index = pd.to_datetime(df_pivot.index)
df_forecast = pd.DataFrame()
mse_train = []
mse_test = []
def prepare_prophet_input(df):
    return pd.DataFrame({'ds': df.index, 'y': df.values})
def prepare_data(df, sample='D', train_prop=0.80):
    df_resampled = df.resample(sample).sum()
    dates_to_remove = [
        '2016-08-14', '2018-10-16', '2017-03-26', '2017-05-11', '2017-08-13', '2017-10-08',
        '2017-12-10', '2018-04-22', '2018-06-24', '2018-09-30', '2018-12-02'
    ]
    df_filtered = df_resampled[~df_resampled.index.isin(pd.to_datetime(dates_to_remove))]
    train_size = int(train_prop * len(df_filtered))
    train_data = prepare_prophet_input(df_filtered.iloc[:train_size])
    test_data = prepare_prophet_input(df_filtered.iloc[train_size:])
    return train_data, test_data
for column in df_pivot.columns:
    train_data, test_data = prepare_data(df_pivot[column], sample='D')
    model = Prophet(yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=True)
    model.fit(train_data)
    future = model.make_future_dataframe(periods=len(test_data), freq='D')
    forecast = model.predict(future)
    df_forecast[column] = forecast['yhat']
    y_actual_test = test_data['y']
    y_predicted_test = df_forecast[column].iloc[-len(test_data):]
    mse_test.append(sqrt(mean_squared_error(y_actual_test, y_predicted_test)))
    y_actual_train = train_data['y']
    y_predicted_train = df_forecast[column].iloc[:len(train_data)]
    mse_train.append(sqrt(mean_squared_error(y_actual_train, y_predicted_train)))
df_forecast['ds'] = forecast['ds']
mse_train_df = pd.DataFrame(mse_train, columns=['MSE_Train'])
mse_test_df = pd.DataFrame(mse_test, columns=['MSE_Test'])
with pd.ExcelWriter('outputY_Passholder.xlsx') as writer:
    df_pivot.to_excel(writer, sheet_name='actual(YWD)')
    df_forecast.to_excel(writer, sheet_name='predicted(YWD)')
    mse_train_df.to_excel(writer, sheet_name='mse_train(YWD)')
    mse_test_df.to_excel(writer, sheet_name='mse_test(YWD)')
df_forecast.plot(x='ds', y=df_forecast.columns[:-1], title='Forecasted Revenue')
plt.show()