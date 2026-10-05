from matplotlib import pyplot as plt
from tqdm import tqdm
import random
from time import time
'''Utility Functions'''
def generate_random_list(n, low=0, high=100):
    return [random.randint(low, high) for _ in range(n)]
def measure_sort_time(sort_func, array):
    start_time = time()
    sort_func(array)
    end_time = time()
    return end_time - start_time
def average_sort_time(sort_func, array, trials=500):
    total_time = sum(measure_sort_time(sort_func, array) for _ in range(trials))
    return total_time / trials
def is_sorted(array):
    return all(array[i] <= array[i + 1] for i in range(len(array) - 1))
'''Sorting Algorithms'''
def insertion_sort(array):
    for j in range(len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(1, n - i):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
def heap_sort(array):
    def sift_down(array, start, end):
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and array[child] < array[child + 1]:
                child += 1
            if array[root] < array[child]:
                array[root], array[child] = array[child], array[root]
                root = child
            else:
                break
    n = len(array)
    for start in range((n - 2)
        sift_down(array, start, n - 1)
    for end in range(n - 1, 0, -1):
        array[end], array[0] = array[0], array[end]
        sift_down(array, 0, end - 1)
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
def quick_sort(array):
    def partition(array, low, high):
        pivot = array[(low + high)
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while array[i] < pivot:
                i += 1
            j -= 1
            while array[j] > pivot:
                j -= 1
            if i >= j:
                return j
            array[i], array[j] = array[j], array[i]
    def quick_sort_helper(array, low, high):
        if low < high:
            pi = partition(array, low, high)
            quick_sort_helper(array, low, pi)
            quick_sort_helper(array, pi + 1, high)
    quick_sort_helper(array, 0, len(array) - 1)
def radix_sort(array):
    RADIX = 10
    placement = 1
    max_digit = max(array)
    while placement < max_digit:
        buckets = [[] for _ in range(RADIX)]
        for i in array:
            tmp = int((i / placement) % RADIX)
            buckets[tmp].append(i)
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                array[a] = i
                a += 1
        placement *= RADIX
def tim_sort(array):
    return sorted(array)
if __name__ == '__main__':
    input_sizes = list(range(100, 25000, 500))
    sort_times = {
        'bubble_sort': [measure_sort_time(bubble_sort, generate_random_list(i)) for i in tqdm(input_sizes[:10], 'bubble_sort')],
        'selection_sort': [measure_sort_time(selection_sort, generate_random_list(i)) for i in tqdm(input_sizes[:10], 'selection_sort')],
        'insertion_sort': [measure_sort_time(insertion_sort, generate_random_list(i)) for i in tqdm(input_sizes[:10], 'insertion_sort')],
        'merge_sort': [measure_sort_time(merge_sort, generate_random_list(i)) for i in tqdm(input_sizes, 'merge_sort')],
        'heap_sort': [measure_sort_time(heap_sort, generate_random_list(i)) for i in tqdm(input_sizes, 'heap_sort')],
        'quick_sort': [measure_sort_time(quick_sort, generate_random_list(i)) for i in tqdm(input_sizes, 'quick_sort')],
        'radix_sort': [measure_sort_time(radix_sort, generate_random_list(i)) for i in tqdm(input_sizes, 'radix_sort')]
    }
    n_squared = {'bubble_sort', 'selection_sort', 'insertion_sort'}
    for sort in sort_times:
        if sort in n_squared:
            plt.plot(input_sizes[:10], sort_times[sort], label=sort.replace('_', ' ').title())
        else:
            plt.plot(input_sizes, sort_times[sort], label=sort.replace('_', ' ').title())
    plt.legend(loc='lower right')
    plt.ylabel('Time (seconds)')
    plt.xlabel('List Size')
    plt.show()