import pandas as pd
from fbprophet import Prophet
from sklearn.metrics import mean_squared_error
from math import sqrt
from datetime import datetime, date
df = pd.read_excel('C:/Users/tusha/Desktop/newtable.xlsx', sheet_name='newtable')
df['start_time'] = pd.to_datetime(df['start_time'], format="%d/%m/%Y %I:%M:%S %p")
df['end_time'] = pd.to_datetime(df['end_time'], format="%d/%m/%Y %I:%M:%S %p")
def calculate_revenue(passtype, duration, time):
    per_thirty = 1.75
    if time < date(year=2018, month=7, day=12):
        per_thirty = 3.5
    qty = int(duration / 30)
    if duration % 30 != 0:
        qty += 1
    if passtype in ['Monthly Pass', 'Annual Pass', 'One Day Pass', 'Flex Pass']:
        qty -= 1
        if qty < 0:
            qty = 0
    return per_thirty * qty
df['revenue'] = df.apply(lambda row: calculate_revenue(row['passholder_type'], row['trip_duration'], row['start_time'].date()), axis=1)
df_daily_revenue = pd.pivot_table(df[['revenue', 'start_time']], aggfunc='sum', index=df['start_time'].dt.date, fill_value=0)
df_daily_revenue.index = pd.to_datetime(df_daily_revenue.index)
df_predicted_revenue = pd.DataFrame()
mse_train = []
mse_test = []
def prepare_prophet_data(df, column_num=0):
    df_prophet = pd.DataFrame()
    df_prophet['ds'] = df.index
    df_prophet['y'] = list(df.iloc[:, column_num])
    return df_prophet
def perform_prophet_forecasting(df, sample='D', test_size=-184):
    removal_dates = ['2016-08-14', '2018-10-16', '2017-03-26', '2017-05-11', '2017-08-13', '2017-10-08',
                     '2017-12-10', '2018-04-22', '2018-06-24', '2018-09-30', '2018-12-02']
    df['temp'] = df.index
    df = df[~df['temp'].isin(removal_dates)]
    df.drop('temp', axis=1, inplace=True)
    df_train = df.iloc[:test_size]
    df_test = df.iloc[test_size:]
    df_train_prophet = prepare_prophet_data(df_train)
    df_test_prophet = prepare_prophet_data(df_test)
    return df_train_prophet, df_test_prophet
for i, column in enumerate(df_daily_revenue.columns):
    train_data, test_data = perform_prophet_forecasting(df_daily_revenue)
    model = Prophet(yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False)
    model.fit(train_data)
    future_dataframe = model.make_future_dataframe(periods=len(test_data)+90+3, freq='D')
    forecast = model.predict(future_dataframe)
    df_predicted_revenue[column] = forecast['yhat']
    y_actual_test = test_data['y']
    y_predicted_test = df_predicted_revenue[column].tail(len(test_data))
    mse_test.append(sqrt(mean_squared_error(y_actual_test, y_predicted_test)))
    y_actual_train = train_data['y']
    y_predicted_train = df_predicted_revenue[column].iloc[:-184-93]
    mse_train.append(sqrt(mean_squared_error(y_actual_train, y_predicted_train)))
df_predicted_revenue['ds'] = forecast['ds']
removal_dates = ['2016-08-14', '2018-10-16', '2017-03-26', '2017-05-11', '2017-08-13', '2017-10-08',
                 '2017-12-10', '2018-04-22', '2018-06-24', '2018-09-30', '2018-12-02']
df_daily_revenue['ds'] = df_daily_revenue.index
df_daily_revenue = df_daily_revenue[~df_daily_revenue['ds'].isin(removal_dates)]
df_daily_revenue = df_daily_revenue.reset_index(drop=True)
mse_train_df = pd.DataFrame(mse_train)
mse_test_df = pd.DataFrame(mse_test)
with pd.ExcelWriter('outputY_Revenue.xlsx') as writer:
    df_daily_revenue.to_excel(writer, sheet_name='actual(Y)')
    df_predicted_revenue.to_excel(writer, sheet_name='predicted(Y)')
    mse_train_df.to_excel(writer, sheet_name='mse_trn(Y)')
    mse_test_df.to_excel(writer, sheet_name='mse_tst(Y)')