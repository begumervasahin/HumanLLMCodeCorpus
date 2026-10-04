import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis
from scipy.special import cbrt
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy.stats import chisquare
from matplotlib import pyplot as plt
import os
import pickle
from sklearn.linear_model import LinearRegression
def exponential_smoothing(data, column, alpha=0.5, high=True, low=True):
    if not 0 < alpha < 1:
        raise ValueError('alpha should be between 0 and 1')
    p1, p5, p95, p99 = data[column].quantile([0.01, 0.05, 0.95, 0.99])
    data.sort_values(column, ascending=True, inplace=True)
    if high:
        s0 = get_st_increasing(data.loc[(data[column] >= p95) & (data[column] <= p99) & (data[column].notnull()), column], alpha)
        for i in data[(data[column] > p99) & (data[column].notnull())].index:
            data.at[i, column] = alpha * data.at[i, column] + (1 - alpha) * s0
            s0 = data.at[i, column]
    if low:
        s0 = get_st_decreasing(data.loc[(data[column] >= p1) & (data[column] <= p5) & (data[column].notnull()), column], alpha)
        for i in data[(data[column] < p1) & (data[column].notnull())].index[::-1]:
            data.at[i, column] = alpha * data.at[i, column] + (1 - alpha) * s0
            s0 = data.at[i, column]
def get_st_increasing(array, alpha):
    st = array[0]
    for value in array[1:]:
        st = alpha * value + (1 - alpha) * st
    return st
def get_st_decreasing(array, alpha):
    st = array[-1]
    for value in array[-2::-1]:
        st = alpha * value + (1 - alpha) * st
    return st
def capping_and_flooring(data, column, upper, lower, high=True, low=True):
    if high:
        data.loc[(data[column] > upper) & (data[column].notnull()), column] = upper
    if low:
        data.loc[(data[column] < lower) & (data[column].notnull()), column] = lower
def make_dummies(data, column):
    df_value = data[column].value_counts(dropna=False).to_frame(name='counts').sort_values(by='counts', ascending=False)
    conversion_list = df_value.index[:-1].tolist()
    for category in conversion_list:
        dummy_column = f"{column}_dum_{category}"
        data[dummy_column] = (data[column] == category).astype(int)
    return conversion_list
def make_dummies_binary(data, column):
    df_value = data[column].value_counts(dropna=False).to_frame(name='counts')
    categories = df_value.index.tolist()
    total_categories = len(categories)
    dummies_count = len(bin(total_categories)[2:])
    binary_conversions = [int(bin(i)[2:]) for i in range(total_categories)]
    conv_list = list(zip(categories, binary_conversions))
    for j in range(dummies_count):
        dummy_column = f"{column}_dum_{j}"
        data[dummy_column] = 0
        for i, category in enumerate(categories):
            data.loc[data[column] == category, dummy_column] = binary_conversions[i] % 10
            binary_conversions[i]
    return conv_list