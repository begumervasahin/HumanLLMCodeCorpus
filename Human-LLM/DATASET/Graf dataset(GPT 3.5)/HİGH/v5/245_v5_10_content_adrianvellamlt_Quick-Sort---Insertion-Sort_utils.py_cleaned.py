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
        b8 = time.time() - b6
        b9 = hashlib.sha512(', '.join([str(x) for x in b3]).encode('utf-8')).hexdigest()
        print(b9)
        print('{}. Function [{}] finished in {} ms'.format(i, b7.__name__, b8 * 1000))
        b2.append(b8 * 1000)
    b2.append('Mean :: {0}'.format(sum(b2) / len(b2)))
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
    return list(np.genfromtxt(path, b11 = ',', dtype=None))
def fonk4(b7):
    return {
        b1.QuickSort.__name__: b1.QuickSort,
        b1.SortMedianOfThree.__name__: b1.SortMedianOfThree,
        b1.OptimisedSort.__name__: b1.OptimisedSort
    }.get(b7, b1.QuickSort)
def fonk5():
    global b4, a1, a2, a3, a4
    if len(sys.argv) > 1:
        b4, a1, a2, a3, a4 = sys.argv[1:6]
        b5['CSVFileName'], b5['Output'] = sys.argv[6:8]
    else:
        b4 = input('Write the algorithm to be used: (QuickSort, SortMedianOfThree, OptimisedSort):\n')
        a1 = input('Write the size of the array:\n')
        a2 = input('All unique elements? (0/1)\n')
        a3 = input('How shuffled should the list be? (0/1/2)\n')
        a4 = input('Repeat sort how many times?\n')
        b5['CSVFileName'] = input('Write input file name:\n')
        b5['Output'] = input('Write output file name:\n')
    for key in ('CSVFileName', 'Output'):
        if not b5[key].endswith('.csv'):
            b5[key] += '.csv'
        b5['Output'] = os.path.abspath(os.path.dirname(sys.argv[0])) + '\\' + b5['Output']
    if a1 != '0':
        b5['CSVFileName'] = os.path.abspath(os.path.dirname(sys.argv[0])) + '\\' + b5['CSVFileName']
    return b4
def fonk6():
    if a1 != '0':
        fonk2(int(a1), True if a2 = = '1' else False, a3)
    return fonk3(b5['CSVFileName'])
def fonk7(b3):
    for _ in range(len(b3)
        b12 = randint(0, len(b3) - 1)
        b13 = randint(0, len(b3) - 1)
        b3[b12], b3[b13] = b3[b13], b3[b12]
    return b3