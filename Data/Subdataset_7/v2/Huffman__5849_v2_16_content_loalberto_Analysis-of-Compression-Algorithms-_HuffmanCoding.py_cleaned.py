from heapq import heappush, heappop, heapify
from collections import defaultdict
import string
import random
import time
def fonk1(values):
    a1 = 0
    b1 = []
    for symbol, weight in values.items():
        a1 += 1
        b1.append([weight, [symbol, ""]])
    heapify(b1)
    while len(b1) > 1:
        a1 += 1
        b2 = heappop(b1)
        b3 = heappop(b1)
        for pair in b2[1:]:
            pair[1] = '0' + pair[1]
        for pair in b3[1:]:
            pair[1] = '1' + pair[1]
        heappush(b1, [b2[0] + b3[0]] + b2[1:] + b3[1:])
    return sorted(heappop(b1)[1:], b4 = lambda val: (len(val[-1]), val)), a1
def fonk2(string_length):
    b5 = string.ascii_lowercase
    return ''.join(random.choice(b5) for _ in range(string_length))
a2 = 10
b6 = {f'Iteration{i}': [] for i in range(1, a2 + 1)}
b7 = {f'Iteration{i}': [] for i in range(1, a2 + 1)}
for i in range(1, a2 + 1):
    for b8 in range(1, 6):
        b8 = 10 ** b8
        b9 = fonk2(b8)
        b10 = defaultdict(int)
        a3 = 0
        for char in b9:
            a3 += 1
            b10[char] += 1
        b11 = time.time()
        vals, b12 = fonk1(b10)
        b13 = time.time()
        b14 = (b13 - b11) * 1000000000
        b15 = b12 + a3
        b6[f'Iteration{i}'].append(b15)
        b7[f'Iteration{i}'].append(b14)
b16 = {i: 0 for i in range(len(b6['Iteration1']))}
for b4 in b6:
    for idx, val in enumerate(b6[b4]):
        b16[idx] += val
b6['Average'] = [val / a2 for val in b16.values()]
b17 = {i: 0 for i in range(len(b7['Iteration1']))}
for b4 in b7:
    for idx, val in enumerate(b7[b4]):
        b17[idx] += val
b7['Average'] = [val / a2 for val in b17.values()]
print('\b8\b8------------Operation Measurement------------\b8\b8')
for b4, value in b6.items():
    print(f"{b4}: {value}")
print('\b8\b8------------Time Measurement------------\b8\b8')
for b4, value in b7.items():
    print(f"{b4}: {value}")