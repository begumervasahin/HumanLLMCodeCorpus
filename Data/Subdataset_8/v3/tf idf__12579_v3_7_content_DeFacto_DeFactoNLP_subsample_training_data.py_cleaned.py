import os
import jsonlines
from random import shuffle
TRAIN_FILE_PATH = "data/train.jsonl"
SUBSAMPLED_FILE_PATH = "data/subsample_train.jsonl"
NUM_REQUIRED_SUPPORT = 3000
NUM_REQUIRED_REFUTE = 3000
NUM_REQUIRED_NOTENOUGHINFO = 4000
def load_data(file_path):
    with jsonlines.open(file_path) as file:
        return [line for line in file]
def write_to_jsonl(file_path, data):
    with jsonlines.open(file_path, mode='w') as writer:
        for sample in data:
            writer.write(sample)
train_set = load_data(TRAIN_FILE_PATH)
shuffle(train_set)
support = []
refute = []
not_enough_info = []
for line in train_set:
    label = line['label']
    if label == "SUPPORTS" and NUM_REQUIRED_SUPPORT > 0:
        support.append(line)
        NUM_REQUIRED_SUPPORT -= 1
    elif label == "REFUTES" and NUM_REQUIRED_REFUTE > 0:
        refute.append(line)
        NUM_REQUIRED_REFUTE -= 1
    elif label == "NOT ENOUGH INFO" and NUM_REQUIRED_NOTENOUGHINFO > 0:
        not_enough_info.append(line)
        NUM_REQUIRED_NOTENOUGHINFO -= 1
subsampled = support + refute + not_enough_info
shuffle(subsampled)
write_to_jsonl(SUBSAMPLED_FILE_PATH, subsampled)
print(f"Total lines in the original dataset: {len(train_set)}")
print(f"Total lines in the subsampled dataset: {len(subsampled)}")
print("Subsampling and writing completed successfully.")