import random
import pandas as pd
def get_stratified_sample(filepath):
    target_data = pd.read_csv(filepath, usecols=[0])
    percent_default = target_data.iloc[:, 0].mean()
    number_of_sample = get_sample_size(percent_default, len(target_data), 0.01)
    number_from_default = int(percent_default * number_of_sample)
    number_from_non_default = number_of_sample - number_from_default
    range_of_non_default = target_data[target_data.iloc[:, 0] == 0].index.tolist()
    range_of_default = target_data[target_data.iloc[:, 0] == 1].index.tolist()
    indx_rows_non_default = random.sample(range_of_non_default, number_from_non_default)
    indx_rows_default = random.sample(range_of_default, number_from_default)
    chunksize = 10000
    chunks = pd.read_csv(filepath, chunksize=chunksize)
    df_default = pd.concat([chunk[chunk.index.isin(indx_rows_default)] for chunk in chunks])
    chunks = pd.read_csv(filepath, chunksize=chunksize)
    df_non_default = pd.concat([chunk[chunk.index.isin(indx_rows_non_default)] for chunk in chunks])
    sample = pd.concat([df_non_default, df_default])
    return sample
def get_sample_size(percent, number_of_elements, error_rate):
    Z = 2.59
    n = percent * (1 - percent) / ((error_rate / Z) ** 2 + percent * (1 - percent) / number_of_elements)
    return n
filepath = 'your_csv_file_path.csv'
sample = get_stratified_sample(filepath)
print(sample.head())