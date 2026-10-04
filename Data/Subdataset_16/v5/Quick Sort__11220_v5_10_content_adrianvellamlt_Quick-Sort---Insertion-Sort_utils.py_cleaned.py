import time
import numpy as np
import hashlib
import quicksort as qsort
import sys
import os
from random import randint
b1 = qsort.QuickSort()
b2 = []
b3 = []
b4 = ''
a1 = 0
a2 = 1
a3 = 0
a4 = 0
b5 = {
    'CSVFileName': 'randomNumDump.csv',
    'Output': 'output.csv',
    'TimeLog': 'timelog.csv'
}
def fonk1(function):
    global b2
    global b3
    global a4
    for i in range(int(a4)):
        b3 = fonk6()
        b6 = time.time()
        b7 = fonk4(function)
        b3 = b7(b3)
        b8 = (time.time() - b6) * 1000
        print(hashlib.sha512(', '.join(map(str, b3)).encode('utf-8')).hexdigest())
        print(f'{i}. function [{b7.b15}] finished in {b8:.2f} ms')
        b2.append(b8)
    b9 = sum(b2) / len(b2)
    b2.append(f'Mean :: {b9:.2f}')
    np.savetxt(b5['TimeLog'], b2, b10 = '%s', b11=',')
    np.savetxt(b5['Output'], b3, b10 = '%d', b11=',')
def fonk2(size, a2, a3):
    b3 = list(np.random.choice(size, size, replace=not a2))
    print('Array Size ::', len(b3))
    if a3 = = '0':
        b3.sort()
    elif a3 = = '1':
        b3.sort()
        b3 = fonk7(b3)
    np.savetxt(b5['CSVFileName'], b3, b10 = '%d', b11=',')
def fonk3(path):
    return list(np.genfromtxt(path, b11 = ',', dtype=int))
def fonk4(func):
    return {
        'QuickSort': b1.QuickSort,
        'SortMedianOfThree': b1.SortMedianOfThree,
        'OptimisedSort': b1.OptimisedSort
    }.get(func, b1.QuickSort)
def fonk5():
    global b4
    global a1
    global a2
    global a3
    global a4
    if len(sys.argv) > 1:
        b4 = sys.argv[1]
        a1 = sys.argv[2]
        a2 = sys.argv[3]
        a3 = sys.argv[4]
        a4 = sys.argv[5]
        b5['CSVFileName'] = sys.argv[6]
        b5['Output'] = sys.argv[7]
    else:
        b4 = input('Choose the algorithm to be used: (QuickSort, SortMedianOfThree, OptimisedSort):\n')
        a1 = input('Enter the size of the array:\n')
        a2 = input('All unique elements? (0/1)\n')
        a3 = input('How shuffled should the list be? (0/1/2)\n')
        a4 = input('Repeat sort how many times?\n')
        b5['CSVFileName'] = input('Enter input file name:\n')
        b5['Output'] = input('Enter output file name:\n')
    if not b5['CSVFileName'].endswith('.csv'):
        b5['CSVFileName'] += '.csv'
    if not b5['Output'].endswith('.csv'):
        b5['Output'] += '.csv'
    b12 = os.path.abspath(os.path.dirname(sys.argv[0]))
    b5['Output'] = os.path.join(b12, b5['Output'])
    if a1 != '0':
        b5['CSVFileName'] = os.path.join(b12, b5['CSVFileName'])
    return b4
def fonk6():
    global a1
    global a2
    global a3
    if a1 != '0':
        fonk2(int(a1), a2 = = '1', a3)
    return fonk3(b5['CSVFileName'])
def fonk7(b3):
    for _ in range(len(b3)
        b13 = randint(0, len(b3) - 1)
        b14 = randint(0, len(b3) - 1)
        b3[b13], b3[b14] = b3[b14], b3[b13]
    return b3
if b15 = = "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "runtests":
        print('Running tests')
    else:
        fonk5()
        fonk1(b4)