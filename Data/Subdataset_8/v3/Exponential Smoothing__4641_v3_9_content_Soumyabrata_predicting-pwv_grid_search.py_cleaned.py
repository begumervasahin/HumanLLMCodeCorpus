import numpy as np
import pandas as pd
import random
from read_matfile import read_matfile
from statsmodels.tsa.api import ExponentialSmoothing
import matplotlib.pyplot as plt
matlab_file_path = './data/PWV_2010from_WS_2_withGradient.mat'
timestamps, pwv = read_matfile(matlab_file_path)
print('Imported the MATLAB file')
df = pd.DataFrame(data=np.column_stack((timestamps, pwv)), columns=['timestamps', 'pwv']).set_index(['timestamps'])
total_data_points = len(df)
lead_time_array = np.arange(5, 30, 5)
previous_time_array = np.arange(12000, 2000, -2000)
num_experiments = 10
rmse_matrix = np.zeros([len(previous_time_array), len(lead_time_array)])
for i, lead_time in enumerate(lead_time_array):
    for j, previous_time in enumerate(previous_time_array):
        lead_observation_minutes = int(lead_time / 5)
        previous_observation_minutes = int(previous_time / 5)
        rmse_values = []
        for _ in range(num_experiments):
            last_possible_index = total_data_points - (previous_observation_minutes + lead_observation_minutes)
            start_index = random.randint(0, last_possible_index)
            print('Starting index:', start_index)
            print(f'Computing for lead time = {lead_time} mins with history of {previous_time} mins')
            train_data = df[start_index:start_index + previous_observation_minutes]
            test_data = df[start_index + previous_observation_minutes:start_index + previous_observation_minutes + lead_observation_minutes]
            predictions = test_data.copy()
            model = ExponentialSmoothing(np.asarray(train_data['pwv']), seasonal_periods=288, trend='add', seasonal='add').fit()
            predictions['Holt_Winter'] = model.forecast(len(test_data))
            actual_values = predictions['pwv']
            predicted_values = predictions['Holt_Winter']
            rmse_value = np.sqrt(np.mean((predicted_values - actual_values) ** 2))
            rmse_values.append(rmse_value)
        rmse_matrix[j, i] = np.mean(rmse_values)
        print('RMSE matrix:', rmse_matrix)
np.save('./results/rmse_matrix_for_grid.npy', rmse_matrix)
num_rows, num_columns = rmse_matrix.shape
x_labels = [5 * (i + 1) for i in range(num_columns)]
y_labels = list(previous_time_array)
y_labels.reverse()
fig, ax = plt.subplots()
heatmap = ax.imshow(rmse_matrix, cmap=plt.cm.coolwarm)
plt.xticks([]), plt.yticks([])
plt.xticks(np.arange(0, num_columns, 1), x_labels)
plt.yticks(np.arange(0, num_rows, 1), y_labels)
plt.xlabel('Lead Times (in mins)', fontsize=12)
plt.ylabel('Historical Data (in mins)', fontsize=12)
color_bar = fig.colorbar(heatmap, ticks=[rmse_matrix.min(), rmse_matrix.max()], orientation='vertical')
color_bar.ax.set_yticklabels(['Low', 'High'])
fig.tight_layout()
fig.savefig('./results/rmse.pdf')
plt.show()