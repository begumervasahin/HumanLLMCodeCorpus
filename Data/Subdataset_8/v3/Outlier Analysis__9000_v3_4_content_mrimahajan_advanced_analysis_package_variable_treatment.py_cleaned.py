import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
def apply_exponential_smoothing(data, column, alpha=0.5, smooth_high=True, smooth_low=True):
    percentiles = data[column].quantile([0.01, 0.05, 0.95, 0.99])
    if not 0 < alpha < 1:
        raise ValueError('Alpha should be between 0 and 1')
    data.sort_values(column, ascending=True, inplace=True)
    if smooth_high:
        smoothed_high = data.loc[(data[column] >= percentiles[0.95]) & (data[column] <= percentiles[0.99]) & (data[column].notnull()), column].mean()
        for index in data[(data[column] > percentiles[0.99]) & (data[column].notnull())].index:
            data.loc[index, column] = alpha * data.loc[index, column] + (1 - alpha) * smoothed_high
            smoothed_high = data.loc[index, column]
    if smooth_low:
        smoothed_low = data.loc[(data[column] >= percentiles[0.01]) & (data[column] <= percentiles[0.05]) & (data[column].notnull()), column].mean()
        for index in data[(data[column] < percentiles[0.01]) & (data[column].notnull())].index[::-1]:
            data.loc[index, column] = alpha * data.loc[index, column] + (1 - alpha) * smoothed_low
            smoothed_low = data.loc[index, column]
def apply_capping_and_flooring(data, column, upper_bound, lower_bound, cap_high=True, floor_low=True):
    if cap_high:
        data.loc[(data[column] > upper_bound) & (data[column].notnull()), column] = upper_bound
    if floor_low:
        data.loc[(data[column] < lower_bound) & (data[column].notnull()), column] = lower_bound
def create_dummy_variables(data, column):
    conversion_list = []
    value_counts = data[column].value_counts(dropna=False).sort_values(ascending=False)
    for category in value_counts.index[:-1]:
        conversion_list.append(category)
        data[column + '_dum_' + str(category)] = (data[column] == category).astype(int)
    return conversion_list
def create_binary_dummy_variables(data, column):
    value_counts = data[column].value_counts(dropna=False).sort_index()
    categories = value_counts.index.tolist()
    total_categories = len(categories)
    num_digits = int(np.ceil(np.log2(total_categories)))
    bin_conversion = [int(bin(i)[2:]) for i in range(total_categories)]
    conversion_list = [(cat, bin_val) for cat, bin_val in zip(categories, bin_conversion)]
    for j in range(num_digits):
        data[column + '_dum_' + str(j)] = 0
        for i, (_, bin_val) in enumerate(conversion_list):
            data.loc[data[column] == categories[i], column + '_dum_' + str(j)] = bin_val % 10
            bin_conversion[i] = bin_val
    return conversion_list