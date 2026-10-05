import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller as ADF
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.stats.diagnostic import acorr_ljungbox
input_file = 'data/sales_by_item.xlsx'
output_path = 'result/'
forecast_output_file = os.path.join(output_path, 'forecast.xlsx')
model_output_file = os.path.join(output_path, 'model.xlsx')
sales_data = pd.read_excel(input_file).T
sales_data.index = pd.to_datetime(sales_data.index)
data_for_analysis = sales_data.iloc[:-12, :]
data_for_testing = sales_data.iloc[-12:-7, :]
data_for_prediction = sales_data.iloc[-7: -1, :]
eda_output_folder = 'eda_fig/'
os.makedirs(eda_output_folder, exist_ok=True)
plt.style.use('ggplot')
for column in data_for_analysis.columns:
    output_path = os.path.join(eda_output_folder, column + '.png')
    data_for_analysis[column].plot(figsize=(10, 8))
    plt.title(column)
    plt.xlabel('Date')
    plt.ylabel('Sales Quantity')
    plt.savefig(output_path, dpi=200)
    plt.close()
differences = {}
p_values_adf = {}
for column in data_for_analysis.columns:
    adf_result = ADF(data_for_analysis[column])
    differences[column] = 0
    p_values_adf[column] = adf_result[1]
    while adf_result[1] >= .05:
        try:
            differences[column] += 1
            adf_result = ADF(data_for_analysis[column].diff(differences[column]).dropna())
            p_values_adf[column] = adf_result[1]
        except:
            differences[column] = -1
new_products = [k for (k, v) in p_values_adf.items() if np.isnan(v) or v == 0.0]
current_products = [x for x in sales_data.columns if x not in new_products]
acf_pacf_output_folder = 'acf_pacf_fig/'
os.makedirs(acf_pacf_output_folder, exist_ok=True)
def plot_acf_pacf(data, savefig=False, savename=''):
    lag = len(data) - 1
    fig = plt.figure(figsize=(10, 8))
    ax1 = fig.add_subplot(211)
    fig = sm.graphics.tsa.plot_acf(data, lags=lag, ax=ax1)
    ax2 = fig.add_subplot(212)
    fig = sm.graphics.tsa.plot_pacf(data, lags=lag, ax=ax2)
    if not savefig:
        plt.show()
    else:
        plt.savefig(savename, dpi=200)
for column in current_products:
    diff_value = differences[column]
    if diff_value == 0:
        data = data_for_analysis[column]
    else:
        data = data_for_analysis[column].diff(diff_value).dropna()
    save_path = os.path.join(acf_pacf_output_folder, column + ' (diff ' + str(diff_value) + ').png')
    plot_acf_pacf(data, True, save_path)
    plt.close()
num_products = len(current_products)
num_models_to_check = int(num_products / 10)
p_max = q_max = num_models_to_check
bic_values = {}
for column in current_products:
    print('Working on %s' % column)
    diff_value = differences[column]
    data = data_for_analysis[column].astype(float)
    bic_matrix = []
    for p in range(p_max + 1):
        tmp = []
        for q in range(q_max + 1):
            try:
                tmp.append(ARIMA(data, (p, diff_value, q)).fit().bic)
            except:
                tmp.append(np.nan)
        bic_matrix.append(tmp)
    bic_values[column] = bic_matrix
    print('-' * 80)
models_to_manually_check = []
for column in current_products:
    data = pd.DataFrame(bic_values[column])
    if int(data.isnull().sum().sum()) == (num_models_to_check + 1) ** 2:
        print('%s is empty and should be manually checked. ' % column)
        models_to_manually_check.append(column)
models_to_run = [x for x in current_products if x not in models_to_manually_check]
p_q_values = {}
for column in models_to_run:
    data = pd.DataFrame(bic_values[column])
    p, q = data.stack().idxmin()
    p_q_values[column] = [p, q]
parameters_df = pd.DataFrame()
for column in models_to_run:
    p_val = p_q_values[column][0]
    q_val = p_q_values[column][1]
    d_val = differences[column]
    parameters_df[column] = pd.Series([p_val, d_val, q_val])
parameters_df.to_excel(model_output_file)
model_validity = {}
fitted_models = {}
for column in models_to_run:
    try:
        arima_model = ARIMA(data_for_analysis[column].astype(float), tuple(parameters_df[column])).fit()
        predicted_values = arima_model.predict()
        residuals = pd.Series(predicted_values) - data_for_analysis[column]
        lb_test_statistic, p_value = acorr_ljungbox(residuals, lags=1)
        num_lags_rejected = (p_value < 0.05).sum()
        if num_lags_rejected > 0:
            model_validity[column] = False
            models_to_manually_check.append(column)
        else:
            model_validity[column] = True
            fitted_models[column] = arima_model
    except:
        model_validity[column] = False
        models_to_manually_check.append(column)
models_to_run = [x for x in current_products if x not in models_to_manually_check]
forecast_results = {}
forecast_start_date = pd.Timestamp(np.datetime64('2017-01'))
forecast_end_date = pd.Timestamp(np.datetime64('2017-12'))
for column in models_to_run:
    arima_model = fitted_models[column]
    forecast_values = arima_model.predict(start=forecast_start_date, end=forecast_end_date)
    forecast_results[column] = forecast_values
writer = pd.ExcelWriter(forecast_output_file)
for column, forecast_data in forecast_results.items():
    forecast_data.to_excel(writer, sheet_name=column)
writer.save()