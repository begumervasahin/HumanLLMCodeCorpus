import random
import string
import time
from collections import defaultdict
from heapq import heappush, heappop, heapify
def fonk1(symbols_weights):
    b1 = []
    a1 = 0
    for symbol, weight in symbols_weights.items():
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
    b4 = sorted(heappop(b1)[1:], key=lambda pair: (len(pair[1]), pair[0]))
    return b4, a1
def fonk2(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
def fonk3(b5 = 10):
    b6 = {f'Iteration {i + 1}': [] for i in range(b5)}
    b7 = {f'Iteration {i + 1}': [] for i in range(b5)}
    for iteration in range(1, b5 + 1):
        a2 = 10
        while a2 <= 100000:
            b8 = fonk2(a2)
            b9 = defaultdict(int)
            for ch in b8:
                b9[ch] += 1
            b10 = time.time()
            _, b11 = fonk1(b9)
            b12 = time.time()
            b13 = (b12 - b10) * 1e9
            b14 = b11 + len(b8)
            b6[f'Iteration {iteration}'].append(b14)
            b7[f'Iteration {iteration}'].append(b13)
            a2 *= 10
    b6['Average'] = fonk4(b6)
    b7['Average'] = fonk4(b7)
    return b6, b7
def fonk4(matrix):
    b15 = []
    b16 = len(matrix) - 1
    for i in range(len(matrix['Iteration 1'])):
        b17 = sum(matrix[f'Iteration {j + 1}'][i] for j in range(b16)) / b16
        b15.append(b17)
    return b15
def fonk5():
    b6, b7 = fonk3()
    print('\n\n------------ Operation Measurement ------------\n\n')
    for key, values in b6.items():
        print(f'{key}: {values}')
    print('\n\n------------ Time Measurement (ns) ------------\n\n')
    for key, values in b7.items():
        print(f'{key}: {values}')
if b18 = = "__main__":
    fonk5()