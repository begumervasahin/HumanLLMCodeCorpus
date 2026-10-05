from matplotlib import pyplot as plt
from tqdm import tqdm
import random
from time import time
def rand_list(n, low=0, high=100):
    return [random.randint(low, high) for _ in range(n)]
def sort_time(sort_func, array):
    start = time()
    sort_func(array)
    stop = time()
    return stop - start
def avg_sort_time(sort_func, array, trials=500):
    total_time = sum(sort_time(sort_func, array) for _ in range(trials))
    return total_time / trials
def is_sorted(array):
    return all(array[i] <= array[i+1] for i in range(len(array)-1))
def insertion_sort(array):
    for j in range(len(array)):
        key, i = array[j], j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key
    return array
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
def selection_sort(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array
def heap_sort(array):
    def sift_down(array, start, end):
        root = start
        while True:
            child = root * 2 + 1
            if child > end:
                break
            if child + 1 <= end and array[child] < array[child + 1]:
                child += 1
            if array[root] < array[child]:
                array[root], array[child] = array[child], array[root]
                root = child
            else:
                break
    for start in range(len(array)
        sift_down(array, start, len(array) - 1)
    for end in range(len(array) - 1, 0, -1):
        array[end], array[0] = array[0], array[end]
        sift_down(array, 0, end - 1)
    return array
def merge_sort(array):
    if len(array) <= 1:
        return array
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
    if len(array) <= 1:
        return array
    pivot = array[len(array)
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
def radix_sort(array):
    mod, div = 10, 1
    while True:
        buckets = [[] for _ in range(10)]
        for num in array:
            buckets[(num % mod)
        mod *= 10
        div *= 10
        array = [num for bucket in buckets for num in bucket]
        if len(buckets[0]) == len(array):
            return array
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