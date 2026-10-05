import os
import jsonlines
from random import shuffle
def load_jsonl(file_path):
    with jsonlines.open(file_path) as file:
        return [line for line in file]
def write_jsonl(data, file_path):
    with jsonlines.open(file_path, mode='w') as writer:
        for item in data:
            writer.write(item)
def subsample_data(data, num_samples):
    shuffle(data)
    return data[:num_samples]
def categorize_data(data):
    support = []
    refute = []
    not_enough_info = []
    for line in data:
        label = line['label']
        if label == "SUPPORTS":
            support.append(line)
        elif label == "REFUTES":
            refute.append(line)
        elif label == "NOT ENOUGH INFO":
            not_enough_info.append(line)
    return support, refute, not_enough_info
train_file_path = "data/train.jsonl"
subsampled_file_path = "data/subsample_train.jsonl"
train_set = load_jsonl(train_file_path)
num_required_support = 3000
num_required_refute = 3000
num_required_not_enough_info = 4000
support, refute, not_enough_info = categorize_data(train_set)
subsampled_support = subsample_data(support, num_required_support)
subsampled_refute = subsample_data(refute, num_required_refute)
subsampled_not_enough_info = subsample_data(not_enough_info, num_required_not_enough_info)
subsampled = subsampled_support + subsampled_refute + subsampled_not_enough_info
shuffle(subsampled)
print("Original dataset length:", len(train_set))
print("Subsampled dataset length:", len(subsampled))
write_jsonl(subsampled, subsampled_file_path)