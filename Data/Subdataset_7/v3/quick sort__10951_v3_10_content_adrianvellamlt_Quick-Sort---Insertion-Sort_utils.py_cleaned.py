import time
import numpy as np
import hashlib
import quicksort as qsort
import sys
import os
from random import randint
b1 = 'randomNumDump.csv'
b2 = 'output.csv'
b3 = 'timelog.csv'
b4 = qsort.QuickSort()
def fonk1(function):
    b5 = []
    for _ in range(int(b16)):
        b6 = fonk6()
        b7 = time.time()
        b8 = fonk4(function)
        b6 = b8(b6)
        b9 = time.time() - b7
        print(hashlib.sha512(', '.join([str(x) for x in b6]).encode('utf-8')).hexdigest())
        print('Function [{}] finished in {} ms'.format(b8.b21, b9 * 1000))
        b5.append(b9 * 1000)
    b5.append('Mean :: {0}'.format(sum(b5) / len(b5)))
    np.savetxt(b3, b5, b10 = '%s', b12=',')
    np.savetxt(b2, b6, b10 = '%d', b12=',')
def fonk2(size, b15, b11):
    b6 = list(np.random.choice(size, size, replace=not b15))
    print('Array Size ::', len(b6))
    if b11 = = '0':
        b6.sort()
    elif b11 = = '1':
        b6.sort()
        b6 = fonk7(b6)
    np.savetxt(b1, b6, b10 = '%d', b12=',')
def fonk3(path):
    return list(np.genfromtxt(path, b12 = ',', dtype=None))
def fonk4(b8):
    return {
        b4.QuickSort.b21: b4.QuickSort,
        b4.SortMedianOfThree.b21: b4.SortMedianOfThree,
        b4.OptimisedSort.b21: b4.OptimisedSort
    }.get(b8, b4.QuickSort)
def fonk5():
    if len(sys.argv) > 1:
        b13 = sys.argv[1]
        b14 = sys.argv[2]
        b15 = sys.argv[3]
        b11 = sys.argv[4]
        b16 = sys.argv[5]
        b17 = sys.argv[6]
        b18 = sys.argv[7]
    else:
        b13 = input('Write the algorithm to be used: (QuickSort, SortMedianOfThree, OptimisedSort):\n')
        b14 = input('Write the size of the array:\n')
        b15 = input('All unique elements? (0/1)\n')
        b11 = input('How shuffled should the list be? (0/1/2)\n')
        b16 = input('Repeat sort how many times?\n')
        b17 = input('Write input file name:\n')
        b18 = input('Write output file name:\n')
    b17 = os.path.abspath(os.path.dirname(sys.argv[0])) + '\\' + b17
    b18 = os.path.abspath(os.path.dirname(sys.argv[0])) + '\\' + b18
    if b14 != '0':
        b17 = os.path.abspath(os.path.dirname(sys.argv[0])) + '\\' + b1
    return b13, b16, b17, b18
def fonk6():
    if b14 != '0':
        fonk2(int(b14), True if b15 = = '1' else False, b11)
    return fonk3(b1)
def fonk7(b6):
    for _ in range(len(b6)
        b19 = randint(0, len(b6) - 1)
        b20 = randint(0, len(b6) - 1)
        b6[b19], b6[b20] = b6[b20], b6[b19]
    return b6
if b21 = = "__main__":
    b13, b16, b17, b18 = fonk5()
    fonk1(b13)