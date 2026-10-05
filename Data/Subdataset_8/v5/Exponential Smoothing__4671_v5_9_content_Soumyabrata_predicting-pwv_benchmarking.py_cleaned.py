import numpy as np
import pandas as pd
import random
from read_matfile import read_matfile
from statsmodels.tsa.api import ExponentialSmoothing
import matplotlib.pyplot as plt
def calculate_rmse(actual, predicted):
    return np.sqrt(np.mean((predicted - actual) ** 2))
matlab_file_path = './data/PWV_2010from_WS_2_withGradient.mat'
timestamps, pwv = read_matfile(matlab_file_path)
print('Imported the MATLAB file')
data_df = pd.DataFrame({'timestamps': timestamps, 'pwv': pwv})
lead_times = np.arange(5, 20, 5)
num_experiments = 10
previous_time = 10000
previous_observations = int(previous_time / 5)
with open("./results/comparison.txt", "w") as result_file:
    result_file.write("time, our, naive, average \n")
    for lead_time in lead_times:
        lead_observations = int(lead_time / 5)
        rmse_values = []
        persist_values = []
        average_values = []
        for _ in range(num_experiments):
            start_index = random.randint(0, len(data_df) - (previous_observations + lead_observations))
            train_data = data_df.iloc[start_index:start_index + previous_observations]
            test_data = data_df.iloc[start_index + previous_observations:start_index + previous_observations + lead_observations]
            predictions = test_data.copy()
            model = ExponentialSmoothing(np.asarray(train_data['pwv']), seasonal_periods=288, trend='add', seasonal='add').fit()
            predictions['Holt_Winter'] = model.forecast(len(test_data))
            last_value = train_data['pwv'].iloc[-1]
            predictions['naive'] = last_value * np.ones(len(test_data))
            mean_training_value = np.mean(train_data['pwv'])
            predictions['average'] = mean_training_value * np.ones(len(test_data))
            actual_values = predictions['pwv']
            holt_winter_values = predictions['Holt_Winter']
            naive_values = predictions['naive']
            average_values = predictions['average']
            rmse_values.append(calculate_rmse(actual_values, holt_winter_values))
            persist_values.append(calculate_rmse(actual_values, naive_values))
            average_values.append(calculate_rmse(actual_values, average_values))
        result_file.write(f"{lead_time}, {np.mean(rmse_values)}, {np.mean(persist_values)}, {np.mean(average_values)} \n")