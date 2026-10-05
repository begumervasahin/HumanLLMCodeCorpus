
import pandas as pd
from fbprophet import Prophet
from sklearn.metrics import mean_squared_error
from math import sqrt
df = pd.read_excel('newtable.xlsx', sheet_name='newtable')
df['start_time'] = pd.to_datetime(df['start_time'], format="%d/%m/%Y %I:%M:%S %p")
df['end_time'] = pd.to_datetime(df['end_time'], format="%d/%m/%Y %I:%M:%S %p")
df_pivot = pd.pivot_table(df[['start_station', 'start_time']], aggfunc='count', index=df['start_time'].dt.date, columns=['start_station'], fill_value=0)
stations_to_remove = [
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
df_pivot.drop(labels=stations_to_remove, axis=1, inplace=True)
df_pivot.index = pd.to_datetime(df_pivot.index)
df_predicted = pd.DataFrame()
mse_train = []
mse_test = []
def prepare_prophet_input(df, column_num=0):
    df_input = pd.DataFrame()
    df_input['ds'] = df.index
    df_input['y'] = list(df.iloc[:, column_num])
    return df_input
def train_test_prophet(df_pivot, sample='D', test_samples=-184):
    removal_dates = ['2016-08-14', '2018-10-16', '2017-03-26', '2017-05-11', '2017-08-13', '2017-10-08',
                     '2017-12-10', '2018-04-22', '2018-06-24', '2018-09-30', '2018-12-02']
    df_pivot['temp'] = df_pivot.index
    for date in removal_dates:
        df_pivot = df_pivot[df_pivot.temp != date]
    df_pivot.drop('temp', axis=1, inplace=True)
    df_train = df_pivot.loc[df_pivot.index[:test_samples]]
    df_test = df_pivot.loc[df_pivot.index[test_samples:]]
    df_train_input = prepare_prophet_input(df_train)
    df_test_input = prepare_prophet_input(df_test)
    return df_train_input, df_test_input
for i, station in enumerate(df_pivot.columns):
    train_data, test_data = train_test_prophet(df_pivot, sample='D', test_samples=-184)
    model = Prophet(yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False)
    model.fit(train_data)
    future = model.make_future_dataframe(periods=len(test_data) + 90 + 3, freq='D')
    forecast = model.predict(future)
    df_predicted[station] = forecast['yhat']
    y_actual_test = test_data['y']
    y_predicted_test = df_predicted[station][df_predicted.index[-184:]]
    mse_test.append(sqrt(mean_squared_error(y_actual_test, y_predicted_test)))
    y_actual_train = train_data['y']
    y_predicted_train = df_predicted[station][df_predicted.index[:-184-93]]
    mse_train.append(sqrt(mean_squared_error(y_actual_train, y_predicted_train)))
df_actual = df_pivot.reset_index(drop=True)
mse_train_df = pd.DataFrame(mse_train)
mse_test_df = pd.DataFrame(mse_test)
with pd.ExcelWriter('outputY.xlsx') as writer:
    df_actual.to_excel(writer, sheet_name='actual(Y)')
    df_predicted.to_excel(writer, sheet_name='predicted(Y)')
    mse_train_df.to_excel(writer, sheet_name='mse_trn(Y)')
    mse_test_df.to_excel(writer, sheet_name='mse_tst(Y)')