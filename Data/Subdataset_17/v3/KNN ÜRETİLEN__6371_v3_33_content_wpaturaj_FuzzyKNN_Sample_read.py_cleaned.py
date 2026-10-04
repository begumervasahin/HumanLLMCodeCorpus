import math
import random
import pandas as pd
def get_stratified_sample(filepath, error_rate=0.01, confidence_level=0.99):
    target_data = pd.read_csv(filepath, usecols=[0])
    percent_default = target_data.iloc[:, 0].mean()
    sample_size = calculate_sample_size(percent_default, len(target_data), error_rate, confidence_level)
    samples_from_default = int(math.ceil(percent_default * sample_size))
    samples_from_non_default = sample_size - samples_from_default
    indices_non_default = target_data[target_data.iloc[:, 0] == 0].index.tolist()
    indices_default = target_data[target_data.iloc[:, 0] == 1].index.tolist()
    sampled_indices_non_default = random.sample(indices_non_default, samples_from_non_default)
    sampled_indices_default = random.sample(indices_default, samples_from_default)
    stratified_sample = pd.concat([
        filter_sampled_indices(filepath, sampled_indices_non_default),
        filter_sampled_indices(filepath, sampled_indices_default)
    ])
    return stratified_sample
def calculate_sample_size(percent, total_elements, error_rate, confidence_level):
    Z = {
        0.99: 2.576,
        0.95: 1.96,
        0.90: 1.645
    }.get(confidence_level, 1.96)
    n = (percent * (1 - percent)) / (((error_rate / Z) ** 2) + ((percent * (1 - percent)) / total_elements))
    return int(n)
def filter_sampled_indices(filepath, sampled_indices):
    iter_csv = pd.read_csv(filepath, iterator=True, chunksize=10000)
    return pd.concat([chunk.loc[sampled_indices] for chunk in iter_csv if not chunk.loc[sampled_indices].empty])
if __name__ == "__main__":
    filepath = "your_dataset.csv"
    sample = get_stratified_sample(filepath)
    sample.to_csv("stratified_sample.csv", index=False)
    print("Stratified sample saved to stratified_sample.csv")