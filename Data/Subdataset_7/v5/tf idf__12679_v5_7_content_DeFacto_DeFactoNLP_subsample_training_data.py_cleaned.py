import os
import jsonlines
from random import shuffle
def fonk1(file_path):
    with jsonlines.open(file_path) as file:
        return [line for line in file]
def fonk2(data, file_path):
    with jsonlines.open(file_path, b1 = 'w') as writer:
        for item in data:
            writer.write(item)
def fonk3(data, num_samples):
    shuffle(data)
    return data[:num_samples]
def fonk4(data):
    b2 = []
    b3 = []
    b4 = []
    for line in data:
        b5 = line['b5']
        if b5 = = "SUPPORTS":
            b2.append(line)
        elif b5 = = "REFUTES":
            b3.append(line)
        elif b5 = = "NOT ENOUGH INFO":
            b4.append(line)
    return b2, b3, b4
b6 = "data/train.jsonl"
b7 = "data/subsample_train.jsonl"
b8 = fonk1(b6)
a1 = 3000
a2 = 3000
a3 = 4000
b2, b3, b4 = fonk4(b8)
b9 = fonk3(b2, a1)
b10 = fonk3(b3, a2)
b11 = fonk3(b4, a3)
b12 = b9 + b10 + b11
shuffle(b12)
print("Original dataset length:", len(b8))
print("Subsampled dataset length:", len(b12))
fonk2(b12, b7)