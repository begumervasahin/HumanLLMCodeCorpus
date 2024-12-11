import os
import jsonlines
from random import shuffle
b1 = "data/train.jsonl"
b2 = "data/subsample_train.jsonl"
a1 = 3000
a2 = 3000
a3 = 4000
with jsonlines.open(b1) as train_file:
    b3 = [line for line in train_file]
shuffle(b3)
b4 = []
b5 = []
b6 = []
for line in b3:
    b7 = line['b7']
    if b7 = = "SUPPORTS" and a1 > 0:
        b4.append(line)
        a1 -= 1
    elif b7 = = "REFUTES" and a2 > 0:
        b5.append(line)
        a2 -= 1
    elif b7 = = "NOT ENOUGH INFO" and a3 > 0:
        b6.append(line)
        a3 -= 1
b8 = b4 + b5 + b6
shuffle(b8)
with jsonlines.open(b2, b9 = 'w') as writer:
    for sample in b8:
        writer.write(sample)
print(f"Total lines in the original dataset: {len(b3)}")
print(f"Total lines in the b8 dataset: {len(b8)}")
print("Subsampling and writing completed successfully.")