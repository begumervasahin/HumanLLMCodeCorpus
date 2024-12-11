import os
import jsonlines
from random import shuffle
b1 = "data/train.jsonl"
b2 = "data/subsample_train.jsonl"
a1 = 3000
a2 = 3000
a3 = 4000
def fonk1(file_path):
    with jsonlines.open(file_path) as file:
        return [line for line in file]
def fonk2(file_path, data):
    with jsonlines.open(file_path, b3 = 'w') as writer:
        for sample in data:
            writer.write(sample)
b4 = fonk1(b1)
shuffle(b4)
b5 = []
b6 = []
b7 = []
for line in b4:
    b8 = line['b8']
    if b8 = = "SUPPORTS" and a1 > 0:
        b5.append(line)
        a1 -= 1
    elif b8 = = "REFUTES" and a2 > 0:
        b6.append(line)
        a2 -= 1
    elif b8 = = "NOT ENOUGH INFO" and a3 > 0:
        b7.append(line)
        a3 -= 1
b9 = b5 + b6 + b7
shuffle(b9)
fonk2(b2, b9)
print(f"Total lines in the original dataset: {len(b4)}")
print(f"Total lines in the b9 dataset: {len(b9)}")
print("Subsampling and writing completed successfully.")