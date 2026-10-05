import os
import jsonlines
from random import shuffle
b1 = "data/train.jsonl"
b1 = jsonlines.open(b1)
b2 = []
b3 = []
b4 = []
b5 = []
a1 = 3000
a2 = 3000
a3 = 4000
for lines in b1:
	b2.append(lines)
shuffle(b2)
for lines in b2:
	if lines['label'] == "SUPPORTS" and a1>0:
		b3.append(lines)
		a1 = a1 - 1
	elif lines['label'] == "REFUTES" and a2>0:
		b4.append(lines)
		a2 = a2 - 1
	elif lines['label'] == "NOT ENOUGH INFO" and a3>0:
		b5.append(lines)
		a3 = a3 - 1
b6 = b3 + b4 + b5
shuffle(b6)
print(len(b2))
print(len(b6))
b7 = "data/subsample_train.jsonl"
with jsonlines.open(b7, b8 = 'w') as writer:
	for s in b6:
		writer.write(s)