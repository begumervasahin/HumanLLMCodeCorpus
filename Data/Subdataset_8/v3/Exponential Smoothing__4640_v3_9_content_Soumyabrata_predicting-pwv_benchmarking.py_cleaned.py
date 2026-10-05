import numpy as np
import pandas as pd
import random
from statsmodels.tsa.api import ExponentialSmoothing
def read_matfile(matlab_file):
    pass
matlab_file = './data/PWV_2010from_WS_2_withGradient.mat'
(timestamp, pwv) = read_matfile(matlab_file)
print('MATLAB file imported successfully')
data = np.column_stack((timestamp, pwv))
df = pd.DataFrame(data=data, columns=['timestamps', 'pwv']).set_index(['timestamps'])
end_index = len(df)
lead_times = np.arange(5, 20, 5)
num_experiments = 10
previous_time = 10000
previous_obs = int(previous_time / 5)
output_file = open("./results/comparison.txt", "w")
output_file.write("lead_time, our_model, naive_model, average_model\n")
for lead_time in lead_times:
    lead_obs = int(lead_time / 5)
    rmse_results = []
    persist_results = []
    average_results = []
    for _ in range(num_experiments):
        start_index = random.randint(0, end_index - (previous_obs + lead_obs))
        train_data = df[start_index:start_index + previous_obs]
        test_data = df[start_index + previous_obs:start_index + previous_obs + lead_obs]
        y_hat = test_data.copy()
        model = ExponentialSmoothing(np.asarray(train_data['pwv']), seasonal_periods=288, trend='add', seasonal='add').fit()
        y_hat['Holt_Winter'] = model.forecast(len(test_data))
        last_val = train_data['pwv'].iloc[-1]
        y_hat['naive'] = last_val * np.ones(len(test_data))
        mean_train_val = np.mean(train_data['pwv'])
        y_hat['average'] = mean_train_val * np.ones(len(test_data))
        rmse = np.sqrt(np.mean((y_hat['Holt_Winter'] - y_hat['pwv']) ** 2))
        rmse_results.append(rmse)
        rmse = np.sqrt(np.mean((y_hat['naive'] - y_hat['pwv']) ** 2))
        persist_results.append(rmse)
        rmse = np.sqrt(np.mean((y_hat['average'] - y_hat['pwv']) ** 2))
        average_results.append(rmse)
    output_file.write(f"{lead_time}, {np.mean(rmse_results)}, {np.mean(persist_results)}, {np.mean(average_results)}\n")
output_file.close()