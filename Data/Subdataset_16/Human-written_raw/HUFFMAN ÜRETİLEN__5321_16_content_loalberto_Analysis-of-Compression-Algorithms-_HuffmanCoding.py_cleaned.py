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
    return sorted(heappop(b1)[1:], b4 = lambda b18: (len(b18[-1]), b18)), a1
def fonk2(string_length):
    b5 = string.ascii_lowercase
    return ''.join(random.choice(b5) for i in range(string_length))
a2 = 10
b6 = {'Iteration1': [],
             'Iteration2': [],
             'Iteration3': [],
             'Iteration4': [],
             'Iteration5': [],
             'Iteration6': [],
             'Iteration7': [],
             'Iteration8': [],
             'Iteration9': [],
             'Iteration10': []}
b7 = {'Iteration1': [],
               'Iteration2': [],
               'Iteration3': [],
               'Iteration4': [],
               'Iteration5': [],
               'Iteration6': [],
               'Iteration7': [],
               'Iteration8': [],
               'Iteration9': [],
               'Iteration10': []}
a3 = 1
b8 = 'Iteration{}'.format(a3)
a4 = 1
b9 = 'Iteration{}'.format(a4)
while a2 != 0:
    a2 -= 1
    a5 = 10
    while a5 <= 100000:
        b10 = fonk2(a5)
        b11 = defaultdict(int)
        a6 = 0
        for ch in b10:
            a6 += 1
            b11[ch] += 1
        b12 = time.time()
        b13 = fonk1(b11)
        b14 = time.time()
        b15 = (b14 - b12) * 1000000000
        b16 = b13[1] + a6
        b6[b8].append(b16)
        b7[b9].append(b15)
        a5 *= 10
    a3 += 1
    b8 = 'Iteration{}'.format(a3)
    a4 += 1
    b9 = 'Iteration{}'.format(a4)
b17 = {}
for i in range(0, len(b6['Iteration1'])):
    b17[i] = 0
for b4 in b6:
    a3 = 0
    for i in b6[b4]:
        b17[a3] += i
        a3 += 1
for b4 in b17:
    b18 = b17[b4]
    b17[b4] = b18 / 10
b6['Average'] = []
for b4 in b17:
    b6['Average'].append(b17[b4])
b17 = {}
for i in range(0, len(b7['Iteration1'])):
    b17[i] = 0
for b4 in b7:
    a3 = 0
    for i in b7[b4]:
        b17[a3] += i
        a3 += 1
for b4 in b17:
    b18 = b17[b4]
    b17[b4] = b18 / 10
b7['Average'] = []
for b4 in b17:
    b7['Average'].append(b17[b4])
print('\a5\a5------------This is for the operation measurement------------\a5\a5')
for b4 in b6:
    print(b4 + ' ' + str(b6[b4]))
print('\a5\a5------------This is for the time measurement------------\a5\a5')
for b4 in b7:
    print(b4 + ' ' + str(b7[b4]))