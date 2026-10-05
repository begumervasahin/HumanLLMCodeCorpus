import os
import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller as ADF
from statsmodels.tsa.arima_model import ARIMA
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot
from statsmodels.stats.diagnostic import acorr_ljungbox
input_file = 'data/sales_by_item.xlsx'
output_path = 'result/'
if not os.path.exists(output_path):
    os.makedirs(output_path)
forecast_output_file = 'result/forecast.xlsx'
model_output_file = 'result/model.xlsx'
data = pd.read_excel(input_file).T
data.index = pd.to_datetime(data.index)
data_analysis = data.iloc[:-12, :]
data_test = data.iloc[-12:-7, :]
data_prediction = data.iloc[-7: -1, :]
eda_figure_output = 'eda_fig/'
if not os.path.exists(eda_figure_output):
    os.makedirs(eda_figure_output)
plt.style.use('ggplot')
for column in data_analysis.columns:
    figure_output = os.path.join(eda_figure_output, column + '.png')
    data_analysis[column].plot(figsize=(10, 8))
    plt.title(column)
    plt.xlabel('Date')
    plt.ylabel('Sales Quantity')
    plt.savefig(figure_output, dpi=200)
    plt.close()
differences = {}
p_values_adf = {}
for column in data_analysis.columns:
    adf_result = ADF(data_analysis[column])
    differences[column] = 0
    p_values_adf[column] = adf_result[1]
    while adf_result[1] >= .05:
        try:
            differences[column] += 1
            adf_result = ADF(data_analysis[column].diff(differences[column]).dropna())
            p_values_adf[column] = adf_result[1]
        except:
            differences[column] = -1
new_products = [key for key, value in p_values_adf.items() if np.isnan(value) or value == 0.0]
current_products = [column for column in data.columns if column not in new_products]
acf_pacf_figure_output = 'acf_pacf_fig/'
if not os.path.exists(acf_pacf_figure_output):
    os.makedirs(acf_pacf_figure_output)
def plot_acf_pacf(data, save_fig=False, save_name=''):
    lag = len(data) - 1
    fig = plt.figure(figsize=(10, 8))
    ax1 = fig.add_subplot(211)
    fig = sm.graphics.tsa.plot_acf(data, lags=lag, ax=ax1)
    ax2 = fig.add_subplot(212)
    fig = sm.graphics.tsa.plot_pacf(data, lags=lag, ax=ax2)
    if not save_fig:
        plt.show()
    else:
        plt.savefig(save_name, dpi=200)
for column in current_products:
    d = differences[column]
    if d == 0:
        data_to_plot = data_analysis[column]
    else:
        data_to_plot = data_analysis[column].diff(d).dropna()
    save_directory = os.path.join(acf_pacf_figure_output, column + ' (diff ' + str(d) + ').png')
    plot_acf_pacf(data_to_plot, save_fig=True, save_name=save_directory)
    plt.close()
limit = int(len(current_products) / 10)
p_max = limit
q_max = limit
bic_values = {}
for column in current_products:
    print('Working on %s' % column)
    d = differences[column]
    data_to_fit = data_analysis[column].astype(float)
    bic_matrix = []
    for p in range(p_max + 1):
        tmp = []
        for q in range(q_max + 1):
            try:
                tmp.append(ARIMA(data_to_fit, (p, d, q)).fit().bic)
            except:
                tmp.append(np.nan)
        bic_matrix.append(tmp)
    bic_values[column] = bic_matrix
    print('-' * 80)
manual_check_columns = []
for column in current_products:
    data = pd.DataFrame(bic_values[column])
    if int(data.isnull().sum().sum()) == (limit + 1) ** 2:
        print('%s is empty and should be manually checked. ' % column)
        manual_check_columns.append(column)
machine_run_columns = [column for column in current_products if column not in manual_check_columns]
p_q_values = {}
for column in machine_run_columns:
    data = pd.DataFrame(bic_values[column])
    p, q = data.stack().idxmin()
    p_q_values[column] = [p, q]
parameters_df = pd.DataFrame()
for column in machine_run_columns:
    p = p_q_values[column][0]
    q = p_q_values[column][1]
    d = differences[column]
    parameters_df[column] = pd.Series([p, d, q])
lag_value = 6
validity_dict = {}
arima_models = {}
for column in machine_run_columns:
    try:
        arima_model = ARIMA(data_analysis[column].astype(float), tuple(parameters_df[column])).fit()
        predicted_values = arima_model.predict()
        error_series = pd.Series(predicted_values) - data_analysis[column]
        lb_test_results, p_value = acorr_ljungbox(error_series, lags=1)
        significant_lags_count = (p_value < 0.05).sum()
        if significant_lags_count > 0:
            validity_dict[column] = False
            manual_check_columns.append(column)
        else:
            validity_dict[column] = True
            arima_models[column] = arima_model
    except:
        validity_dict[column] = False
        manual_check_columns.append(column)
machine_run_columns = [column for column in current_products if column not in manual_check_columns]
parameters_df[machine_run_columns].to_excel(model_output_file)
forecasted_values = {}
start_timestamp = pd.Timestamp(np.datetime64('2017-01'))
end_timestamp = pd.Timestamp(np.datetime64('2017-12'))
for column in machine_run_columns:
    original_data = data_analysis[column]
    test_data = data_test[column]
    arima_model = arima_models[column]
    predicted_values = arima_model.predict(start_timestamp, end_timestamp)
    forecasted_values[column] = predicted_values
    plt.figure(figsize=(10, 5))
    plt.title('Sales Projection of %s for %s - %s' % (column, str(start_timestamp)[:7], str(end_timestamp)[:7]))
    plt.plot(original_data, color='r', label='History', linestyle='-')
    plt.plot(test_data, color='c', label='YTD', linestyle='-')
    plt.plot(predicted_values, color='g', label='Projection', linestyle='--')
    plt.xlabel('Date')
    plt.ylabel('Sales Quantity')
    plt.legend(loc=0)
    figure_name = column + ' for ' + str(start_timestamp)[:7] + ' - ' + str(end_timestamp)[:7] + '.png'
    figure_path = os.path.join(output_path, figure_name)
    plt.savefig(figure_path, dpi=200)
    plt.close()