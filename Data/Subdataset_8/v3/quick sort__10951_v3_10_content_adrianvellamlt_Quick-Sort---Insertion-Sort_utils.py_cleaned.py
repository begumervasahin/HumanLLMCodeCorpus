import time
import numpy as np
import hashlib
import quicksort as qsort
import sys
import os
from random import randint
CSV_FILE_NAME = 'randomNumDump.csv'
OUTPUT_FILE_NAME = 'output.csv'
TIME_LOG_FILE_NAME = 'timelog.csv'
qs = qsort.QuickSort()
def timed_sort_function(function):
    time_array = []
    for _ in range(int(repeat)):
        arr = setup_up_array()
        start_time = time.time()
        func = choose_algorithm(function)
        arr = func(arr)
        elapsed_time = time.time() - start_time
        print(hashlib.sha512(', '.join([str(x) for x in arr]).encode('utf-8')).hexdigest())
        print('Function [{}] finished in {} ms'.format(func.__name__, elapsed_time * 1000))
        time_array.append(elapsed_time * 1000)
    time_array.append('Mean :: {0}'.format(sum(time_array) / len(time_array)))
    np.savetxt(TIME_LOG_FILE_NAME, time_array, fmt='%s', delimiter=',')
    np.savetxt(OUTPUT_FILE_NAME, arr, fmt='%d', delimiter=',')
def new_array_to_csv(size, is_unique, shuffle):
    arr = list(np.random.choice(size, size, replace=not is_unique))
    print('Array Size ::', len(arr))
    if shuffle == '0':
        arr.sort()
    elif shuffle == '1':
        arr.sort()
        arr = slightly_shuffle(arr)
    np.savetxt(CSV_FILE_NAME, arr, fmt='%d', delimiter=',')
def csv_to_array(path):
    return list(np.genfromtxt(path, delimiter=',', dtype=None))
def choose_algorithm(func):
    return {
        qs.QuickSort.__name__: qs.QuickSort,
        qs.SortMedianOfThree.__name__: qs.SortMedianOfThree,
        qs.OptimisedSort.__name__: qs.OptimisedSort
    }.get(func, qs.QuickSort)
def initial_setup():
    if len(sys.argv) > 1:
        chosen_algorithm = sys.argv[1]
        arr_size = sys.argv[2]
        is_unique = sys.argv[3]
        shuffle = sys.argv[4]
        repeat = sys.argv[5]
        csv_file_name = sys.argv[6]
        output_file_name = sys.argv[7]
    else:
        chosen_algorithm = input('Write the algorithm to be used: (QuickSort, SortMedianOfThree, OptimisedSort):\n')
        arr_size = input('Write the size of the array:\n')
        is_unique = input('All unique elements? (0/1)\n')
        shuffle = input('How shuffled should the list be? (0/1/2)\n')
        repeat = input('Repeat sort how many times?\n')
        csv_file_name = input('Write input file name:\n')
        output_file_name = input('Write output file name:\n')
    csv_file_name = os.path.abspath(os.path.dirname(sys.argv[0])) + '\\' + csv_file_name
    output_file_name = os.path.abspath(os.path.dirname(sys.argv[0])) + '\\' + output_file_name
    if arr_size != '0':
        csv_file_name = os.path.abspath(os.path.dirname(sys.argv[0])) + '\\' + CSV_FILE_NAME
    return chosen_algorithm, repeat, csv_file_name, output_file_name
def setup_up_array():
    if arr_size != '0':
        new_array_to_csv(int(arr_size), True if is_unique == '1' else False, shuffle)
    return csv_to_array(CSV_FILE_NAME)
def slightly_shuffle(arr):
    for _ in range(len(arr)
        rand_no1 = randint(0, len(arr) - 1)
        rand_no2 = randint(0, len(arr) - 1)
        arr[rand_no1], arr[rand_no2] = arr[rand_no2], arr[rand_no1]
    return arr
if __name__ == "__main__":
    chosen_algorithm, repeat, csv_file_name, output_file_name = initial_setup()
    timed_sort_function(chosen_algorithm)