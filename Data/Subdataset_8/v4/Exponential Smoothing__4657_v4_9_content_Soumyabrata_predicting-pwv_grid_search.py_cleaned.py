import numpy as np
import pandas as pd
import random
from read_matfile import read_matfile
from statsmodels.tsa.api import ExponentialSmoothing
import matplotlib.pyplot as plt
matlab_file_path = './data/PWV_2010from_WS_2_withGradient.mat'
(timestamp, pwv) = read_matfile(matlab_file_path)
print('Imported the MATLAB file')
df = pd.DataFrame(data=np.column_stack((timestamp, pwv)), columns=['timestamps', 'pwv']).set_index(['timestamps'])
total_data_points = len(df)
lead_time_array = np.arange(5, 30, 5)
previous_time_array = np.arange(12000, 2000, -2000)
num_experiments = 10
rmse_matrix = np.zeros([len(previous_time_array), len(lead_time_array)])
print(rmse_matrix)
for i, lead_time in enumerate(lead_time_array):
    for j, previous_time in enumerate(previous_time_array):
        lead_obs_minutes = int(lead_time / 5)
        prev_obs_minutes = int(previous_time / 5)
        rmse_values = []
        for _ in range(num_experiments):
            last_possible_index = total_data_points - (prev_obs_minutes + lead_obs_minutes)
            start_index = random.randint(0, last_possible_index)
            print('Start index:', start_index)
            print(f'Computing for lead time = {lead_time} mins with history of {previous_time} mins')
            train_data = df[start_index:start_index + prev_obs_minutes]
            test_data = df[start_index + prev_obs_minutes:start_index + prev_obs_minutes + lead_obs_minutes]
            y_hat_avg = test_data.copy()
            print('Computation started')
            fit1 = ExponentialSmoothing(np.asarray(train_data['pwv']), seasonal_periods=288, trend='add', seasonal='add').fit()
            y_hat_avg['Holt_Winter'] = fit1.forecast(len(test_data))
            print('Computation completed')
            actual_values = y_hat_avg['pwv']
            predicted_values = y_hat_avg['Holt_Winter']
            rmse_value = np.sqrt(np.mean((predicted_values - actual_values) ** 2))
            rmse_values.append(rmse_value)
        rmse_values = np.array(rmse_values)
        rmse_matrix[j, i] = np.mean(rmse_values)
        print(rmse_matrix)
np.save('./results/rmse_matrix_for_grid.npy', rmse_matrix)
num_y_components, num_x_components = rmse_matrix.shape
x_labels = [5 * (i + 1) for i in range(num_x_components)]
y_labels = list(previous_time_array)
y_labels.reverse()
fig, ax = plt.subplots()
cax = ax.imshow(rmse_matrix, cmap=plt.cm.coolwarm)
plt.xticks([]), plt.yticks([])
plt.xticks(np.arange(0, num_x_components, 1), x_labels)
plt.yticks(np.arange(0, num_y_components, 1), y_labels)
plt.xlabel('Lead Times (in mins)', fontsize=12)
plt.ylabel('Historical Data (in mins)', fontsize=12)
color_bar = fig.colorbar(cax, ticks=[rmse_matrix.min(), rmse_matrix.max()], orientation='vertical')
color_bar.ax.set_yticklabels(['Low', 'High'])
fig.tight_layout()
fig.savefig('./results/rmse.pdf')
plt.show()