import random
import string
import time
from heapq import heappush, heappop, heapify
from collections import defaultdict
def fonk1(symbol_weights):
    a1 = 0
    b1 = []
    for symbol, weight in symbol_weights.items():
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
    b4 = sorted(heappop(b1)[1:], key=lambda item: (len(item[1]), item[0]))
    return b4, a1
def fonk2(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
def fonk3():
    a2 = 10
    b5 = {f'Iteration {i + 1}': [] for i in range(a2)}
    b6 = {f'Iteration {i + 1}': [] for i in range(a2)}
    for itr in range(a2):
        b7 = f'Iteration {itr + 1}'
        a3 = 10
        while a3 <= 100000:
            b8 = fonk2(a3)
            b9 = defaultdict(int)
            a4 = 0
            for char in b8:
                a4 += 1
                b9[char] += 1
            b10 = time.time()
            encoded_values, b11 = fonk1(b9)
            b12 = time.time()
            b13 = (b12 - b10) * 1e9
            b14 = a4 + b11
            b5[b7].append(b14)
            b6[b7].append(b13)
            a3 *= 10
    fonk4(b5)
    fonk4(b6)
    fonk5(b5, 'Operation Count')
    fonk5(b6, 'Time (ns)')
def fonk4(matrix):
    b15 = len(matrix)
    b16 = [
        sum(matrix[key][i] for key in matrix) / b15
        for i in range(len(next(iter(matrix.values()))))
    ]
    matrix['Average'] = b16
def fonk5(matrix, label):
    print(f'\a3------------ {label} Measurements ------------\a3')
    for key, values in matrix.items():
        print(f'{key}: {values}')
if b17 = = "__main__":
    fonk3()