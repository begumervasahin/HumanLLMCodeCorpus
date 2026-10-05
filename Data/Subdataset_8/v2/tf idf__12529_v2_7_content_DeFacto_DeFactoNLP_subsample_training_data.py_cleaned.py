import os
import jsonlines
from random import shuffle
train_file_path = "data/train.jsonl"
subsampled_file_path = "data/subsample_train.jsonl"
num_required_support = 3000
num_required_refute = 3000
num_required_notenoughinfo = 4000
with jsonlines.open(train_file_path) as train_file:
    train_set = [line for line in train_file]
shuffle(train_set)
support = []
refute = []
not_enough_info = []
for line in train_set:
    label = line['label']
    if label == "SUPPORTS" and num_required_support > 0:
        support.append(line)
        num_required_support -= 1
    elif label == "REFUTES" and num_required_refute > 0:
        refute.append(line)
        num_required_refute -= 1
    elif label == "NOT ENOUGH INFO" and num_required_notenoughinfo > 0:
        not_enough_info.append(line)
        num_required_notenoughinfo -= 1
subsampled = support + refute + not_enough_info
shuffle(subsampled)
with jsonlines.open(subsampled_file_path, mode='w') as writer:
    for sample in subsampled:
        writer.write(sample)
print(f"Total lines in the original dataset: {len(train_set)}")
print(f"Total lines in the subsampled dataset: {len(subsampled)}")
print("Subsampling and writing completed successfully.")