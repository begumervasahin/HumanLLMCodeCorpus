from matplotlib import pyplot as plt
from tqdm import tqdm
import random
from time import time
'''Utility Functions'''
def rand_list(n, low=0, high=100):
    return [random.randint(low, high) for _ in range(n)]
def sort_time(f, A):
    start = time()
    f(A)
    stop = time()
    return stop - start
def avg_sort_time(f, A, trials=500):
    total_time = sum(sort_time(f, A) for _ in range(trials))
    return total_time / trials
def is_sorted(A):
    return all(A[i] <= A[i + 1] for i in range(len(A) - 1))
'''Sorting Algorithms'''
def insertion_sort(A):
    for j in range(len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
def bubble_sort(A):
    n = len(A)
    for i in range(n):
        for j in range(1, n - i):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
def selection_sort(A):
    n = len(A)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if A[j] < A[min_index]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]
def heap_sort(A):
    def sift_down(A, start, end):
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and A[child] < A[child + 1]:
                child += 1
            if A[root] < A[child]:
                A[root], A[child] = A[child], A[root]
                root = child
            else:
                break
    n = len(A)
    for start in range((n - 2)
        sift_down(A, start, n - 1)
    for end in range(n - 1, 0, -1):
        A[end], A[0] = A[0], A[end]
        sift_down(A, 0, end - 1)
def merge_sort(A):
    if len(A) > 1:
        mid = len(A)
        left_half = A[:mid]
        right_half = A[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                A[k] = left_half[i]
                i += 1
            else:
                A[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            A[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            A[k] = right_half[j]
            j += 1
            k += 1
def quick_sort(A):
    def partition(A, low, high):
        pivot = A[(low + high)
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while A[i] < pivot:
                i += 1
            j -= 1
            while A[j] > pivot:
                j -= 1
            if i >= j:
                return j
            A[i], A[j] = A[j], A[i]
    def quick_sort_helper(A, low, high):
        if low < high:
            pi = partition(A, low, high)
            quick_sort_helper(A, low, pi)
            quick_sort_helper(A, pi + 1, high)
    quick_sort_helper(A, 0, len(A) - 1)
def radix_sort(A):
    RADIX = 10
    placement = 1
    max_digit = max(A)
    while placement < max_digit:
        buckets = [list() for _ in range(RADIX)]
        for i in A:
            tmp = int((i / placement) % RADIX)
            buckets[tmp].append(i)
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                A[a] = i
                a += 1
        placement *= RADIX
def tim_sort(A):
    return sorted(A)
if __name__ == '__main__':
    input_sizes = list(range(100, 25000, 500))
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