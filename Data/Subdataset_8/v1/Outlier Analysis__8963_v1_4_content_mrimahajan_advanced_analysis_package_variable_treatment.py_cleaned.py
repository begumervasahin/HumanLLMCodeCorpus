import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
def exponential_smoothing(data, s, alpha=0.5, high=True, low=True):
    p1, p5, p95, p99 = data[s].quantile([0.01, 0.05, 0.95, 0.99])
    if not 0 < alpha < 1:
        raise ValueError('alpha should be between 0 and 1')
    data.sort_values(s, ascending=True, inplace=True)
    if high:
        st_high = data.loc[(data[s] >= p95) & (data[s] <= p99) & (data[s].notnull()), s].mean()
        for i in data[(data[s] > p99) & (data[s].notnull())].index:
            data.loc[i, s] = alpha * data.loc[i, s] + (1 - alpha) * st_high
            st_high = data.loc[i, s]
    if low:
        st_low = data.loc[(data[s] >= p1) & (data[s] <= p5) & (data[s].notnull()), s].mean()
        for i in data[(data[s] < p1) & (data[s].notnull())].index[::-1]:
            data.loc[i, s] = alpha * data.loc[i, s] + (1 - alpha) * st_low
            st_low = data.loc[i, s]
def capping_and_flooring(data, s, a, b, high=True, low=True):
    if high:
        data.loc[(data[s] > a) & (data[s].notnull()), s] = a
    if low:
        data.loc[(data[s] < b) & (data[s].notnull()), s] = b
def make_dummies(data, s):
    conversion_list = []
    df_value = data[s].value_counts(dropna=False).sort_values(ascending=False)
    for category in df_value.index[:-1]:
        conversion_list.append(category)
        data[s + '_dum_' + str(category)] = (data[s] == category).astype(int)
    return conversion_list
def make_dummies_binary(data, s):
    df_value = data[s].value_counts(dropna=False).sort_index()
    categories = df_value.index.tolist()
    total_categories = len(categories)
    dummies = int(np.ceil(np.log2(total_categories)))
    bin_conv = [int(bin(i)[2:]) for i in range(total_categories)]
    conv_list = [(cat, bin_val) for cat, bin_val in zip(categories, bin_conv)]
    for j in range(dummies):
        data[s + '_dum_' + str(j)] = 0
        for i, (_, bin_val) in enumerate(conv_list):
            data.loc[data[s] == categories[i], s + '_dum_' + str(j)] = bin_val % 10
            bin_conv[i] = bin_val
    return conv_list
