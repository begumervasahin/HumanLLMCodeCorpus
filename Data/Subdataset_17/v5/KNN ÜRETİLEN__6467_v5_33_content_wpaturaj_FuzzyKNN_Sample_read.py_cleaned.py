import math
import random
import pandas as pd
def get_stratified_sample(filepath, error_rate=0.01):
    target_data = pd.read_csv(filepath, usecols=[0])
    percent_default = target_data.iloc[:, 0].mean()
    num_elements = len(target_data)
    num_sample = calculate_sample_size(percent_default, num_elements, error_rate)
    num_default = int(math.ceil(percent_default * num_sample))
    num_non_default = num_sample - num_default
    default_indices = target_data[target_data.iloc[:, 0] == 1].index.tolist()
    non_default_indices = target_data[target_data.iloc[:, 0] == 0].index.tolist()
    sampled_default_indices = random.sample(default_indices, num_default)
    sampled_non_default_indices = random.sample(non_default_indices, num_non_default)
    df_default = load_filtered_chunks(filepath, sampled_default_indices)
    df_non_default = load_filtered_chunks(filepath, sampled_non_default_indices)
    sample = pd.concat([df_non_default, df_default])
    return sample
def calculate_sample_size(percent, num_elements, error_rate):
    Z = 2.59
    sample_size = percent * (1 - percent) / ((error_rate / Z) ** 2 + (percent * (1 - percent) / num_elements))
    return int(sample_size)
def load_filtered_chunks(filepath, indices):
    iter_csv = pd.read_csv(filepath, iterator=True, chunksize=10000)
    filtered_df = pd.concat([chunk[chunk.index.isin(indices)] for chunk in iter_csv])
    return filtered_df
