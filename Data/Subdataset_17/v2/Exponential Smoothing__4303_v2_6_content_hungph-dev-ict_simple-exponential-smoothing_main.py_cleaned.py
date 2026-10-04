import pandas as pd
import numpy as np
import datetime
from datetime import timedelta
import time
import json
def prepare_data(file_path, output_file='processed_data.csv'):
    price_df = pd.read_csv(file_path)
    most_recorded_id = price_df['id'].value_counts().idxmax()
    filtered_data = price_df[price_df['id'] == most_recorded_id][['id', 'dateUpdated', 'prices.amountMax']].copy()
    current_time = datetime.datetime.now()
    for i in range(len(filtered_data)):
        filtered_data.iat[i, 1] = (current_time + timedelta(days=i)).strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    filtered_data.columns = ['id', 'timestamp', 'demand']
    filtered_data.to_csv(output_file, index=False)
def est_algorithm(file_path, alpha=0.2, log_cli=True):
    start_time = time.time()
    df = pd.read_csv(file_path)
    records = df.values.tolist()
    absolute_deviation = 0
    for index, item in enumerate(records):
        if index == 0:
            item.append(item[2])
        else:
            previous_predict_value = records[index - 1][3]
            previous_actual_value = records[index - 1][2]
            predicted_value = previous_predict_value + alpha * (previous_actual_value - previous_predict_value)
            item.append(predicted_value)
            absolute_deviation += abs(item[2] - item[3])
    mean_absolute_deviation = absolute_deviation / len(records)
    end_time = time.time()
    if log_cli:
        print('-------------------------')
        print(f'MAD: {mean_absolute_deviation:.4f}')
        print(f'Calculation time: {end_time - start_time:.4f} seconds')
        print('-------------------------')
    result = {
        'mse_value': mean_absolute_deviation,
        'calculate_time': round(end_time - start_time, 4)
    }
    return json.dumps(result)
def choose_best_alpha(file_path, frequency=0.2, criterion='mse_value'):
    alpha_values = np.arange(0.01, 1, frequency)
    best_alpha = 0.2
    min_mse_value = float('inf')
    min_calculate_time = float('inf')
    print('*********************')
    for alpha in alpha_values:
        print(f'Processing with alpha = {alpha}')
        result = json.loads(est_algorithm(file_path=file_path, alpha=alpha, log_cli=False))
        mse_value = result['mse_value']
        calculate_time = result['calculate_time']
        if criterion == 'mse_value' and mse_value < min_mse_value:
            min_mse_value = mse_value
            min_calculate_time = calculate_time
            best_alpha = alpha
        if criterion == 'calculate_time' and calculate_time < min_calculate_time:
            min_mse_value = mse_value
            min_calculate_time = calculate_time
            best_alpha = alpha
    print(f'Best alpha: {best_alpha} with MSE value: {min_mse_value:.4f} and calculate time: {min_calculate_time:.4f} seconds')
    print('*********************')
    return best_alpha
if __name__ == '__main__':
    prepare_data('data/DatafinitiElectronicsProductsPricingData.csv')
    choose_best_alpha('processed_data.csv', frequency=0.05, criterion='mse_value')