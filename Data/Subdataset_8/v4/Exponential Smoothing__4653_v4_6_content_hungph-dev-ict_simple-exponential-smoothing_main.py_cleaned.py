import pandas as pd
import numpy as np
import datetime
import time
from datetime import timedelta
import json
price_df = pd.read_csv('data/DatafinitiElectronicsProductsPricingData.csv')
most_common_id = price_df['id'].value_counts().index[0]
most_common_data = price_df[price_df['id'] == most_common_id][['id', 'dateUpdated', 'prices.amountMax']].values
current_time = datetime.datetime.now()
new_time = current_time
for item in most_common_data:
    new_time += timedelta(days=1)
    item[1] = new_time.strftime('%Y-%m-%dT%H:%M:%S:%fZ')
final_df = pd.DataFrame(data=most_common_data, columns=['id', 'timestamp', 'demand'])
final_df.to_csv('foo.csv', index=False)
def est_algorithm(file_path=None, alpha=0.2, log_cli=True):
    start_time = time.time()
    df = pd.read_csv(file_path)
    all_records = df.values.tolist()
    absolute_deviation = 0
    for index, record in enumerate(all_records):
        if index == 0:
            record.append(record[2])
        else:
            previous_prediction = all_records[index - 1][3]
            previous_actual = all_records[index - 1][2]
            smoothed_value = previous_prediction + alpha * (previous_actual - previous_prediction)
            record.append(smoothed_value)
            absolute_deviation += abs(record[2] - record[3])
    mean_absolute_deviation = absolute_deviation / len(all_records)
    end_time = time.time()
    if log_cli:
        print('-------------------------')
        print('MSE:', round(mean_absolute_deviation, 4))
        print('Calculate time:', round((end_time - start_time), 4))
        print('-------------------------')
    result = {'mse_value': mean_absolute_deviation, 'calculate_time': round((end_time - start_time), 4)}
    return json.dumps(result)
def choose_best_alpha(file_path=None, frequency=0.2, criterion='mse_value'):
    alpha_list = np.arange(0.01, 1, frequency).tolist()
    base_result = json.loads(est_algorithm(file_path=file_path, alpha=0.2, log_cli=False))
    min_mse_value = base_result['mse_value']
    min_calculate_time = base_result['calculate_time']
    best_alpha = 0.2
    print('*********************')
    for alpha in alpha_list:
        print('Processing with alpha =', alpha)
        result = json.loads(est_algorithm(file_path=file_path, alpha=alpha))
        mse_value = result['mse_value']
        calculate_time = result['calculate_time']
        if criterion == 'mse_value':
            if mse_value < min_mse_value:
                min_mse_value = mse_value
                min_calculate_time = calculate_time
                best_alpha = alpha
        if criterion == 'calculate_time':
            if calculate_time < min_calculate_time:
                min_mse_value = mse_value
                min_calculate_time = calculate_time
                best_alpha = alpha
    print('Best alpha:', best_alpha, 'with MSE value:', round(min_mse_value, 4), 'and calculate time:', min_calculate_time, 's')
    print('*********************')
    return best_alpha
choose_best_alpha('foo.csv', frequency=0.05, criterion='mse_value')