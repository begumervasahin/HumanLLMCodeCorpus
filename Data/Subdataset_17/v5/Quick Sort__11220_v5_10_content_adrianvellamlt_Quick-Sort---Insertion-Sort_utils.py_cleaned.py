import time
import numpy as np
import hashlib
import quicksort as qsort
import sys
import os
from random import randint
qs = qsort.QuickSort()
time_array = []
arr = []
chosen_algorithm = ''
arr_size = 0
is_unique = 1
shuffle = 0
repeat = 0
definitions = {
    'CSVFileName': 'randomNumDump.csv',
    'Output': 'output.csv',
    'TimeLog': 'timelog.csv'
}
def timed_sort_function(function):
    global time_array
    global arr
    global repeat
    for i in range(int(repeat)):
        arr = setup_array()
        start_time = time.time()
        sort_func = choose_algorithm(function)
        arr = sort_func(arr)
        elapsed_time = (time.time() - start_time) * 1000
        print(hashlib.sha512(', '.join(map(str, arr)).encode('utf-8')).hexdigest())
        print(f'{i}. function [{sort_func.__name__}] finished in {elapsed_time:.2f} ms')
        time_array.append(elapsed_time)
    mean_time = sum(time_array) / len(time_array)
    time_array.append(f'Mean :: {mean_time:.2f}')
    np.savetxt(definitions['TimeLog'], time_array, fmt='%s', delimiter=',')
    np.savetxt(definitions['Output'], arr, fmt='%d', delimiter=',')
def new_array_to_csv(size, is_unique, shuffle):
    arr = list(np.random.choice(size, size, replace=not is_unique))
    print('Array Size ::', len(arr))
    if shuffle == '0':
        arr.sort()
    elif shuffle == '1':
        arr.sort()
        arr = slightly_shuffle(arr)
    np.savetxt(definitions['CSVFileName'], arr, fmt='%d', delimiter=',')
def csv_to_array(path):
    return list(np.genfromtxt(path, delimiter=',', dtype=int))
def choose_algorithm(func):
    return {
        'QuickSort': qs.QuickSort,
        'SortMedianOfThree': qs.SortMedianOfThree,
        'OptimisedSort': qs.OptimisedSort
    }.get(func, qs.QuickSort)
def initial_setup():
    global chosen_algorithm
    global arr_size
    global is_unique
    global shuffle
    global repeat
    if len(sys.argv) > 1:
        chosen_algorithm = sys.argv[1]
        arr_size = sys.argv[2]
        is_unique = sys.argv[3]
        shuffle = sys.argv[4]
        repeat = sys.argv[5]
        definitions['CSVFileName'] = sys.argv[6]
        definitions['Output'] = sys.argv[7]
    else:
        chosen_algorithm = input('Choose the algorithm to be used: (QuickSort, SortMedianOfThree, OptimisedSort):\n')
        arr_size = input('Enter the size of the array:\n')
        is_unique = input('All unique elements? (0/1)\n')
        shuffle = input('How shuffled should the list be? (0/1/2)\n')
        repeat = input('Repeat sort how many times?\n')
        definitions['CSVFileName'] = input('Enter input file name:\n')
        definitions['Output'] = input('Enter output file name:\n')
    if not definitions['CSVFileName'].endswith('.csv'):
        definitions['CSVFileName'] += '.csv'
    if not definitions['Output'].endswith('.csv'):
        definitions['Output'] += '.csv'
    base_path = os.path.abspath(os.path.dirname(sys.argv[0]))
    definitions['Output'] = os.path.join(base_path, definitions['Output'])
    if arr_size != '0':
        definitions['CSVFileName'] = os.path.join(base_path, definitions['CSVFileName'])
    return chosen_algorithm
def setup_array():
    global arr_size
    global is_unique
    global shuffle
    if arr_size != '0':
        new_array_to_csv(int(arr_size), is_unique == '1', shuffle)
    return csv_to_array(definitions['CSVFileName'])
def slightly_shuffle(arr):
    for _ in range(len(arr)
        rand_no1 = randint(0, len(arr) - 1)
        rand_no2 = randint(0, len(arr) - 1)
        arr[rand_no1], arr[rand_no2] = arr[rand_no2], arr[rand_no1]
    return arr
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "runtests":
        print('Running tests')
    else:
        initial_setup()
        timed_sort_function(chosen_algorithm)