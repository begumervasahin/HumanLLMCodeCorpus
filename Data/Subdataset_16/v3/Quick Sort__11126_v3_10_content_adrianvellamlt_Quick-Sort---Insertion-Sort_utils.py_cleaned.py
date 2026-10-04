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
b5 = True
a2 = 0
a3 = 0
b6 = {
    'CSVFileName': 'randomNumDump.csv',
    'Output': 'output.csv',
    'TimeLog': 'timelog.csv'
}
def fonk1(function):
    global b2, b3, a3
    for i in range(int(a3)):
        b3 = fonk6()
        b7 = time.time()
        b8 = fonk4(function)
        b3 = b8(b3)
        b9 = time.time() - b7
        print(hashlib.sha512(', '.join(map(str, b3)).encode('utf-8')).hexdigest())
        print(f'{i}. function [{b8.b15}] finished in {b9 * 1000} ms')
        b2.append(b9 * 1000)
    b10 = sum(b2) / len(b2)
    b2.append(f'Mean :: {b10}')
    np.savetxt(b6['TimeLog'], b2, b11 = '%s', b13=',')
    np.savetxt(b6['Output'], b3, b11 = '%d', b13=',')
def fonk2(size, is_unique, b12):
    b3 = list(np.random.choice(size, size, replace=not is_unique))
    print('Array Size ::', len(b3))
    if b12 = = 0:
        b3.sort()
    elif b12 = = 1:
        b3.sort()
        b3 = fonk7(b3)
    np.savetxt(b6['CSVFileName'], b3, b11 = '%d', b13=',')
def fonk3(path):
    return list(np.genfromtxt(path, b13 = ',', dtype=int))
def fonk4(func):
    return {
        'QuickSort': b1.quick_sort,
        'SortMedianOfThree': b1.sort_median_of_three,
        'OptimisedSort': b1.optimised_sort
    }.get(func, b1.quick_sort)
def fonk5():
    global b4, a1, b5, a2, a3
    if len(sys.argv) > 1:
        b4 = sys.argv[1]
        a1 = int(sys.argv[2])
        b5 = sys.argv[3] == '1'
        a2 = int(sys.argv[4])
        a3 = int(sys.argv[5])
        b6['CSVFileName'] = sys.argv[6]
        b6['Output'] = sys.argv[7]
    else:
        b4 = input('Choose algorithm (QuickSort, SortMedianOfThree, OptimisedSort):\n')
        a1 = int(input('Enter the size of the array:\n'))
        b5 = input('All unique elements? (0/1)\n') == '1'
        a2 = int(input('Shuffling level (0/1/2):\n'))
        a3 = int(input('Number of times to a3 sort:\n'))
        b6['CSVFileName'] = input('Enter input file name:\n')
        b6['Output'] = input('Enter output file name:\n')
    if not b6['CSVFileName'].endswith('.csv'):
        b6['CSVFileName'] += '.csv'
    if not b6['Output'].endswith('.csv'):
        b6['Output'] += '.csv'
    b6['Output'] = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), b6['Output'])
    if a1 != 0:
        b6['CSVFileName'] = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), b6['CSVFileName'])
def fonk6():
    global a1, b5, a2
    if a1 != 0:
        fonk2(a1, b5, a2)
    return fonk3(b6['CSVFileName'])
def fonk7(b3):
    for _ in range(len(b3)
        rand_no1, b14 = randint(0, len(b3) - 1), randint(0, len(b3) - 1)
        b3[rand_no1], b3[b14] = b3[b14], b3[rand_no1]
    return b3
if b15 = = '__main__':
    fonk5()
    fonk1(b4)