from heapq import heappush, heappop, heapify
from collections import defaultdict
import string
import random
import time
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
    return sorted(heappop(b1)[1:], b4 = lambda b17: (len(b17[-1]), b17)), a1
def fonk2(string_length):
    b5 = string.ascii_lowercase
    return ''.join(random.choice(b5) for _ in range(string_length))
def fonk3(a4):
    b6 = defaultdict(list)
    b7 = defaultdict(list)
    for i in range(1, a4 + 1):
        for j in range(1, a4 + 1):
            b8 = 10 ** j
            b9 = fonk2(b8)
            b10 = defaultdict(int)
            a2 = 0
            for ch in b9:
                a2 += 1
                b10[ch] += 1
            b11 = time.time()
            b12 = fonk1(b10)
            b13 = time.time()
            b14 = (b13 - b11) * 1000000000
            b15 = b12[1] + a2
            b6[f'Iteration{i}'].append(b15)
            b7[f'Iteration{i}'].append(b14)
    fonk4(b6, 'Average')
    fonk4(b7, 'Average')
    return b6, b7
def fonk4(matrix, average_key):
    b16 = {}
    for i in range(0, len(matrix['Iteration1'])):
        b16[i] = 0
    for b4 in matrix:
        a3 = 0
        for i in matrix[b4]:
            b16[a3] += i
            a3 += 1
    for b4 in b16:
        b17 = b16[b4]
        b16[b4] = b17 / 10
    matrix[average_key] = []
    for b4 in b16:
        matrix[average_key].append(b16[b4])
def fonk5(matrix, message):
    print(f'\b8\b8------------{message}------------\b8\b8')
    for b4 in matrix:
        print(b4 + ' ' + str(matrix[b4]))
if b18 = = '__main__':
    a4 = 10
    b6, b7 = fonk3(a4)
    fonk5(b6, 'This is for the operation measurement')
    fonk5(b7, 'This is for the time measurement')