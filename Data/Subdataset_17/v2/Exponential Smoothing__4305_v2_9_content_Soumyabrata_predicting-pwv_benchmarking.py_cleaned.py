import numpy as np
import pandas as pd
import random
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing
from read_matfile import read_matfile
def main():
    matlab_file = './data/PWV_2010from_WS_2_withGradient.mat'
    timestamp, pwv = read_matfile(matlab_file)
    print('Imported the MATLAB file')
    data = np.column_stack((timestamp, pwv))
    df = pd.DataFrame(data=data, columns=['timestamps', 'pwv']).set_index('timestamps')
    end_index_of_df = len(df)
    lead_time_array = np.arange(5, 20, 5)
    no_of_experiments = 10
    previous_time = 10000
    previous_observations = int(previous_time / 5)
    with open("./results/comparison.txt", "w") as text_file:
        text_file.write("time, our, naive, average\n")
        for lead_time in lead_time_array:
            lead_observations = int(lead_time / 5)
            rmse_array = []
            persist_array = []
            average_array = []
            for _ in range(no_of_experiments):
                last_possible_index = end_index_of_df - (previous_observations + lead_observations)
                start_index = random.randint(0, last_possible_index)
                print(f'From start index of {start_index}')
                print(f'Computing for lead time = {lead_time} mins with history of {previous_time} mins')
                train = df[start_index:start_index + previous_observations]
                test = df[start_index + previous_observations:start_index + previous_observations + lead_observations]
                y_hat_avg = test.copy()
                print('Computation started')
                fit = ExponentialSmoothing(
                    np.asarray(train['pwv']),
                    seasonal_periods=288,
                    trend='add',
                    seasonal='add'
                ).fit()
                y_hat_avg['Holt_Winter'] = fit.forecast(len(test))
                last_value = train['pwv'].iloc[-1]
                y_hat_avg['naive'] = last_value * np.ones(len(test))
                mean_training_value = np.mean(train['pwv'])
                y_hat_avg['aver'] = mean_training_value * np.ones(len(test))
                print('Computation completed')
                rmse_value = np.sqrt(np.mean((y_hat_avg['Holt_Winter'] - y_hat_avg['pwv']) ** 2))
                rmse_array.append(rmse_value)
                rmse_value = np.sqrt(np.mean((y_hat_avg['naive'] - y_hat_avg['pwv']) ** 2))
                persist_array.append(rmse_value)
                rmse_value = np.sqrt(np.mean((y_hat_avg['aver'] - y_hat_avg['pwv']) ** 2))
                average_array.append(rmse_value)
            text_file.write(f"{lead_time}, {np.mean(rmse_array)}, {np.mean(persist_array)}, {np.mean(average_array)}\n")
if __name__ == '__main__':
    main()