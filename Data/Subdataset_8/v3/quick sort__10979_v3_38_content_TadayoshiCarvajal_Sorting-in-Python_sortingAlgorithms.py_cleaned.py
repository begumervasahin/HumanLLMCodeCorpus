from matplotlib import pyplot as plt
from tqdm import tqdm
from random import randint
from time import time
def generate_random_list(n, low=0, high=100):
    return [randint(low, high) for _ in range(n)]
def measure_sort_time(sort_func, arr):
    start_time = time()
    sort_func(arr)
    end_time = time()
    return end_time - start_time
def average_sort_time(sort_func, arr, trials=500):
    total_time = sum(measure_sort_time(sort_func, arr) for _ in range(trials))
    return total_time / trials
def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True
def insertion_sort(arr):
    for j in range(len(arr)):
        key, i = arr[j], j - 1
        while i > -1 and arr[i] > key:
            arr[i + 1], i = arr[i], i - 1
        arr[i + 1] = key
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)
        left_half, right_half = arr[:mid], arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left, right = 2 * i + 1, 2 * i + 2
        if left < n and arr[i] < arr[left]:
            largest = left
        if right < n and arr[largest] < arr[right]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    n = len(arr)
    for i in range(n
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
def quick_sort(arr):
    def partition(arr, low, high):
        pivot = arr[(low + high)
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while arr[i] < pivot:
                i += 1
            j -= 1
            while arr[j] > pivot:
                j -= 1
            if i >= j:
                return j
            arr[i], arr[j] = arr[j], arr[i]
    def quick_sort_helper(arr, low, high):
        if low < high:
            partition_index = partition(arr, low, high)
            quick_sort_helper(arr, low, partition_index)
            quick_sort_helper(arr, partition_index + 1, high)
    quick_sort_helper(arr, 0, len(arr) - 1)
def radix_sort(arr):
    def counting_sort(arr, exp):
        output = [0] * len(arr)
        count = [0] * 10
        for i in range(len(arr)):
            index = arr[i]
            count[index % 10] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        i = len(arr) - 1
        while i >= 0:
            index = arr[i]
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1
        i = 0
        for i in range(len(arr)):
            arr[i] = output[i]
    max_num = max(arr)
    exp = 1
    while max_num
        counting_sort(arr, exp)
        exp *= 10
    return arr
def tim_sort(arr):
    return sorted(arr)
if __name__ == '__main__':
    input_sizes = [i for i in range(100, 25000, 500)]
    sort_functions = {
        'bubble_sort': bubble_sort,
        'selection_sort': selection_sort,
        'insertion_sort': insertion_sort,
        'merge_sort': merge_sort,
        'heap_sort': heap_sort,
        'quick_sort': quick_sort,
        'radix_sort': radix_sort
    }
    sort_times = {sort_name: [average_sort_time(sort_functions[sort_name], generate_random_list(size)) for size in tqdm(input_sizes, sort_name)] for sort_name in sort_functions}
    for sort_name, times in sort_times.items():
        plt.plot(input_sizes, times, label=sort_name.replace('_', ' ').title())
    plt.legend(loc='lower right')
    plt.ylabel('Time (seconds)')
    plt.xlabel('List Size')
    plt.show()