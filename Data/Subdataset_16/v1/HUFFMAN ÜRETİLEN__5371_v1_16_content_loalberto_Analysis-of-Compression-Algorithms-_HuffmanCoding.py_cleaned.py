import random
import string
import time
from heapq import heappush, heappop, heapify
from collections import defaultdict
def fonk1(values):
    a1 = 0
    b1 = []
    for sym, wt in values.items():
        a1 += 1
        b1.append([wt, [sym, ""]])
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
def fonk3():
    a2 = 10
    b6 = {f'Iteration{i + 1}': [] for i in range(a2)}
    b7 = {f'Iteration{i + 1}': [] for i in range(a2)}
    for itr in range(a2):
        b8 = f'Iteration{itr + 1}'
        a3 = 10
        while a3 <= 100000:
            b9 = fonk2(a3)
            b10 = defaultdict(int)
            a4 = 0
            for ch in b9:
                a4 += 1
                b10[ch] += 1
            b11 = time.time()
            encoded_values, b12 = fonk1(b10)
            b13 = time.time()
            b14 = (b13 - b11) * 1e9
            b15 = b12 + a4
            b6[b8].append(b15)
            b7[b8].append(b14)
            a3 *= 10
    fonk4(b6)
    fonk4(b7)
    fonk5(b6, 'operation')
    fonk5(b7, 'time')
def fonk4(matrix):
    b16 = []
    b17 = len(matrix)
    for i in range(len(matrix['Iteration1'])):
        b18 = sum(matrix[b4][i] for b4 in matrix) / b17
        b16.append(b18)
    matrix['Average'] = b16
def fonk5(matrix, label):
    print(f'\a3\a3------------This is for the {label} measurement------------\a3\a3')
    for b4 in matrix:
        print(f'{b4}: {matrix[b4]}')
if b19 = = "__main__":
    fonk3()