import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis, chisquare
from scipy.special import cbrt
import statsmodels.api as sm
from statsmodels.formula.api import ols
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
def exponential_smoothing(data, column, alpha=0.5, high=True, low=True):
    p1, p5, p95, p99 = data[column].quantile([0.01, 0.05, 0.95, 0.99])
    if not (0 < alpha < 1):
        raise ValueError('Alpha should be between 0 and 1')
    data.sort_values(column, ascending=True, inplace=True)
    if high:
        def smooth_high_values(array, alpha):
            smoothed_value = array[0]
            for value in array[1:]:
                smoothed_value = alpha * value + (1 - alpha) * smoothed_value
            return smoothed_value
        high_values = data.loc[(data[column] >= p95) & (data[column] <= p99) & data[column].notnull(), column]
        initial_smooth = smooth_high_values(high_values, alpha)
        for idx in data[(data[column] > p99) & data[column].notnull()].index:
            data.at[idx, column] = alpha * data.at[idx, column] + (1 - alpha) * initial_smooth
            initial_smooth = data.at[idx, column]
    if low:
        def smooth_low_values(array, alpha):
            smoothed_value = array[-1]
            for value in array[-2::-1]:
                smoothed_value = alpha * value + (1 - alpha) * smoothed_value
            return smoothed_value
        low_values = data.loc[(data[column] >= p1) & (data[column] <= p5) & data[column].notnull(), column]
        initial_smooth = smooth_low_values(low_values, alpha)
        for idx in reversed(data[(data[column] < p1) & data[column].notnull()].index):
            data.at[idx, column] = alpha * data.at[idx, column] + (1 - alpha) * initial_smooth
            initial_smooth = data.at[idx, column]
def cap_and_floor(data, column, upper_bound, lower_bound, high=True, low=True):
    if high:
        data.loc[(data[column] > upper_bound) & data[column].notnull(), column] = upper_bound
    if low:
        data.loc[(data[column] < lower_bound) & data[column].notnull(), column] = lower_bound
def create_dummies(data, column):
    conversion_list = []
    value_counts = data[column].value_counts(dropna=False).sort_values(ascending=False)
    for category in value_counts.index[:-1]:
        conversion_list.append(category)
        dummy_column = f"{column}_dum_{category}"
        data[dummy_column] = (data[column] == category).astype(int)
    return conversion_list
def create_binary_dummies(data, column):
    value_counts = data[column].value_counts(dropna=False)
    categories = value_counts.index.tolist()
    num_categories = len(categories)
    num_dummies = len(bin(num_categories - 1)) - 2
    binary_repr = [bin(i)[2:].zfill(num_dummies) for i in range(num_categories)]
    conversion_list = list(zip(categories, binary_repr))
    for i in range(num_dummies):
        dummy_column = f"{column}_dum_{i}"
        data[dummy_column] = data[column].apply(lambda x: int(binary_repr[categories.index(x)][i]))
    return conversion_list