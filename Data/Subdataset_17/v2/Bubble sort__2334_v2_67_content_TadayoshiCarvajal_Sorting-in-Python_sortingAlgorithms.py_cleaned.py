import random
import time
from matplotlib import pyplot as plt
from tqdm import tqdm
def rand_list(n, low=0, high=100):
    return [random.randint(low, high) for _ in range(n)]
def sort_time(sort_func, arr):
    random.shuffle(arr)
    start = time.time()
    sort_func(arr)
    stop = time.time()
    return stop - start
def avg_sort_time(sort_func, arr, trials=500):
    total_time = sum(sort_time(sort_func, arr) for _ in range(trials))
    return total_time / trials
def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr
def bubble_sort(arr):
    n = len(arr)
    for j in range(n - 1):
        swapped = False
        for i in range(n - 1 - j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
    return arr
def selection_sort(arr):
    n = len(arr)
    for k in range(n):
        min_index = k
        for j in range(k + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[k], arr[min_index] = arr[min_index], arr[k]
    return arr
def heap_sort(arr):
    def sift_down(arr, start, end):
        root = start
        while 2 * root + 1 < end:
            child = 2 * root + 1
            if child + 1 < end and arr[child] < arr[child + 1]:
                child += 1
            if arr[root] < arr[child]:
                arr[root], arr[child] = arr[child], arr[root]
                root = child
            else:
                break
    n = len(arr)
    for start in range(n
        sift_down(arr, start, n)
    for end in range(n - 1, 0, -1):
        arr[end], arr[0] = arr[0], arr[end]
        sift_down(arr, 0, end)
    return arr
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)
        left_half = arr[:mid]
        right_half = arr[mid:]
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
    return arr
def quick_sort(arr):
    def quick_sort_helper(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            quick_sort_helper(arr, low, pivot_index - 1)
            quick_sort_helper(arr, pivot_index + 1, high)
    def partition(arr, low, high):
        pivot = arr[low]
        left = low + 1
        right = high
        done = False
        while not done:
            while left <= right and arr[left] <= pivot:
                left += 1
            while arr[right] >= pivot and right >= left:
                right -= 1
            if right < left:
                done = True
            else:
                arr[left], arr[right] = arr[right], arr[left]
        arr[low], arr[right] = arr[right], arr[low]
        return right
    quick_sort_helper(arr, 0, len(arr) - 1)
    return arr
def radix_sort(arr):
    mod = 10
    div = 1
    while True:
        buckets = [[] for _ in range(10)]
        for num in arr:
            buckets[(num % mod)
        mod *= 10
        div *= 10
        if len(buckets[0]) == len(arr):
            return buckets[0]
        arr = [num for bucket in buckets for num in bucket]
def tim_sort(arr):
    return sorted(arr)
if __name__ == '__main__':
    input_sizes = [i for i in range(100, 25000, 500)]
    sort_times = {
        'Bubble Sort': [sort_time(bubble_sort, rand_list(i)) for i in tqdm(input_sizes[:10], desc='Bubble Sort')],
        'Selection Sort': [sort_time(selection_sort, rand_list(i)) for i in tqdm(input_sizes[:10], desc='Selection Sort')],
        'Insertion Sort': [sort_time(insertion_sort, rand_list(i)) for i in tqdm(input_sizes[:10], desc='Insertion Sort')],
        'Merge Sort': [sort_time(merge_sort, rand_list(i)) for i in tqdm(input_sizes, desc='Merge Sort')],
        'Heap Sort': [sort_time(heap_sort, rand_list(i)) for i in tqdm(input_sizes, desc='Heap Sort')],
        'Quick Sort': [sort_time(quick_sort, rand_list(i)) for i in tqdm(input_sizes, desc='Quick Sort')],
        'Radix Sort': [sort_time(radix_sort, rand_list(i)) for i in tqdm(input_sizes, desc='Radix Sort')]
    }
    n_squared_algorithms = {'Bubble Sort', 'Selection Sort', 'Insertion Sort'}
    for sort_name, times in sort_times.items():
        if sort_name in n_squared_algorithms:
            plt.plot(input_sizes[:10], times, label=sort_name)
        else:
            plt.plot(input_sizes, times, label=sort_name)
    plt.legend(loc='lower right')
    plt.ylabel('Time (seconds)')
    plt.xlabel('List Size')
    plt.title('Sorting Algorithm Performance')
    plt.show()