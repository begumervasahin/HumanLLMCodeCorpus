import hashlib
import os
from pathlib import Path
import time
import exifread
from matplotlib import pyplot as plt
from tqdm import tqdm
import random
'''Utility Functions'''
def rand_list(n, low=0, high=100):
    return [random.randint(low, high) for _ in range(n)]
def sort_time(sort_function, array):
    random.shuffle(array)
    start = time.time()
    sort_function(array)
    stop = time.time()
    return stop - start
def avg_sort_time(sort_function, array, trials=500):
    total_time = sum(sort_time(sort_function, array) for _ in range(trials))
    return total_time / trials
def is_sorted(array):
    return all(array[i] >= array[i - 1] for i in range(1, len(array)))
'''Sorting Algorithms'''
def insertion_sort(array):
    for j in range(len(array)):
        key, i = array[j], j - 1
        while i >= 0 and array[i] > key:
            array[i + 1], i = array[i], i - 1
        array[i + 1] = key
    return array
def bubble_sort(array):
    n = len(array)
    while True:
        swapped = False
        for i in range(1, n):
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
                swapped = True
        if not swapped:
            break
        n -= 1
    return array
def selection_sort(array):
    n = len(array)
    for k in range(n):
        min_index = k
        for j in range(k + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[k], array[min_index] = array[min_index], array[k]
    return array
def heap_sort(array):
    def sift_down(array, start, end):
        root = start
        while 2 * root + 1 < end:
            child = 2 * root + 1
            if child + 1 < end and array[child] < array[child + 1]:
                child += 1
            if array[root] < array[child]:
                array[root], array[child] = array[child], array[root]
                root = child
            else:
                break
    n = len(array)
    for start in range((n - 2)
        sift_down(array, start, n)
    for end in range(n - 1, 0, -1):
        array[end], array[0] = array[0], array[end]
        sift_down(array, 0, end)
    return array
def merge_sort(array):
    if len(array) > 1:
        mid = len(array)
        left_half = array[:mid]
        right_half = array[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1
    return array
def quick_sort(array):
    def quick_sort_helper(array, first, last):
        if first < last:
            split_point = partition(array, first, last)
            quick_sort_helper(array, first, split_point - 1)
            quick_sort_helper(array, split_point + 1, last)
    def partition(array, first, last):
        pivot_value = array[first]
        left_mark = first + 1
        right_mark = last
        done = False
        while not done:
            while left_mark <= right_mark and array[left_mark] <= pivot_value:
                left_mark += 1
            while right_mark >= left_mark and array[right_mark] >= pivot_value:
                right_mark -= 1
            if right_mark < left_mark:
                done = True
            else:
                array[left_mark], array[right_mark] = array[right_mark], array[left_mark]
        array[first], array[right_mark] = array[right_mark], array[first]
        return right_mark
    quick_sort_helper(array, 0, len(array) - 1)
    return array
def radix_sort(array):
    mod, div = 10, 1
    while True:
        buckets = [[] for _ in range(10)]
        for n in array:
            buckets[(n % mod)
        mod, div = mod * 10, div * 10
        if len(buckets[0]) == len(array):
            return buckets[0]
        array = [num for bucket in buckets for num in bucket]
def tim_sort(array):
    return sorted(array)
if __name__ == '__main__':
    input_sizes = [i for i in range(100, 25000, 500)]
    sort_times = {
        'bubble_sort': [sort_time(bubble_sort, rand_list(i)) for i in tqdm(input_sizes[:10], 'bubble_sort')],
        'selection_sort': [sort_time(selection_sort, rand_list(i)) for i in tqdm(input_sizes[:10], 'selection_sort')],
        'insertion_sort': [sort_time(insertion_sort, rand_list(i)) for i in tqdm(input_sizes[:10], 'insertion_sort')],
        'merge_sort': [sort_time(merge_sort, rand_list(i)) for i in tqdm(input_sizes, 'merge_sort')],
        'heap_sort': [sort_time(heap_sort, rand_list(i)) for i in tqdm(input_sizes, 'heap_sort')],
        'quick_sort': [sort_time(quick_sort, rand_list(i)) for i in tqdm(input_sizes, 'quick_sort')],
        'radix_sort': [sort_time(radix_sort, rand_list(i)) for i in tqdm(input_sizes, 'radix_sort')]
    }
    n_squared_sorts = {'bubble_sort', 'selection_sort', 'insertion_sort'}
    for sort_name, times in sort_times.items():
        if sort_name in n_squared_sorts:
            plt.plot(input_sizes[:10], times, label=sort_name.replace('_', ' ').title())
        else:
            plt.plot(input_sizes, times, label=sort_name.replace('_', ' ').title())
    plt.legend(loc='lower right')
    plt.ylabel('Time (seconds)')
    plt.xlabel('List Size')
    plt.title('Sorting Algorithms Time Complexity')
    plt.show()