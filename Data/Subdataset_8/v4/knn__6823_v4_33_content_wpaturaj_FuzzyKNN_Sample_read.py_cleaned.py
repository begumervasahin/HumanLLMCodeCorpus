import math
import random
import pandas as pd
def get_stratified_sample(filepath):
    target_data = pd.read_csv(filepath, usecols=[0])
    percent_default = sum(target_data.iloc[:, 0]) / float(len(target_data))
    number_of_sample = get_sample_size(percent_default, len(target_data), 0.01)
    number_from_default = int(math.ceil(percent_default * number_of_sample))
    number_from_non_default = number_of_sample - number_from_default
    range_of_non_default = target_data[target_data.iloc[:, 0] == 0].index.tolist()
    range_of_default = target_data[target_data.iloc[:, 0] == 1].index.tolist()
    indx_rows_non_default = random.sample(range_of_non_default, number_from_non_default)
    indx_rows_default = random.sample(range_of_default, number_from_default)
    iter_csv = pd.read_csv(filepath, iterator=True, chunksize=10000)
    df_default = pd.concat([chunk[chunk.index.isin(chunk.index & indx_rows_default)] for chunk in iter_csv])
    iter_csv = pd.read_csv(filepath, iterator=True, chunksize=10000)
    df_non_default = pd.concat([chunk[chunk.index.isin(chunk.index & indx_rows_non_default)] for chunk in iter_csv])
    sample = pd.concat([df_non_default, df_default])
    return sample
def get_sample_size(percent, number_of_elements, error_rate):
    Z = 2.59
    n = percent * (1 - percent) / ((error_rate / Z) ** 2 + percent * (1 - percent) / number_of_elements)
    return n