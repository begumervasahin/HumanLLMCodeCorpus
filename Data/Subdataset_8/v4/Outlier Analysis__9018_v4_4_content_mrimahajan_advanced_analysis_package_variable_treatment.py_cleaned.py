import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis
from scipy.special import cbrt
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy.stats import chisquare
import matplotlib.pyplot as plt
from pandas.plotting import table
import os
import pickle
from sklearn.linear_model import LinearRegression
def exponential_smoothing(data, column, alpha=0.5, high=True, low=True):
    p1, p5, p95, p99 = data[column].quantile([0.01, 0.05, 0.95, 0.99])
    if not 0 < alpha < 1:
        raise ValueError('Alpha should be between 0 and 1')
    data.sort_values(column, ascending=True, inplace=True)
    if high:
        st = data.loc[(data[column] >= p95) & (data[column] <= p99) & (data[column].notnull()), column].mean()
        for i in data[(data[column] > p99) & (data[column].notnull())].index:
            data.loc[i, column] = alpha * data.loc[i, column] + (1 - alpha) * st
            st = data.loc[i, column]
    if low:
        st = data.loc[(data[column] >= p1) & (data[column] <= p5) & (data[column].notnull()), column].mean()
        for i in data[(data[column] < p1) & (data[column].notnull())].index[::-1]:
            data.loc[i, column] = alpha * data.loc[i, column] + (1 - alpha) * st
            st = data.loc[i, column]
def capping_and_flooring(data, column, a, b, high=True, low=True):
    if high:
        data.loc[(data[column] > a) & (data[column].notnull()), column] = a
    if low:
        data.loc[(data[column] < b) & (data[column].notnull()), column] = b
def make_dummies(data, column):
    conversion_list = []
    value_counts = data[column].value_counts(dropna=False).sort_values(ascending=False)
    for category in value_counts.index[:-1]:
        conversion_list.append(category)
        data[column + '_dum_' + str(category)] = (data[column] == category).astype(int)
    return conversion_list
def make_binary_dummies(data, column):
    value_counts = data[column].value_counts(dropna=False).sort_index()
    categories = value_counts.index.tolist()
    total_categories = len(categories)
    num_digits = len(str(total_categories))
    bin_conversion = [int(bin(i)[2:]) for i in range(total_categories)]
    conv_list = [(cat, bin_val) for cat, bin_val in zip(categories, bin_conversion)]
    for j in range(num_digits):
        data[column + '_dum_' + str(j)] = 0
        for i, (_, bin_val) in enumerate(conv_list):
            data.loc[data[column] == categories[i], column + '_dum_' + str(j)] = bin_val % 10
            bin_conversion[i] = bin_val
    return conv_list