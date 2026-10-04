
import time
from timeit import Timer
def merge_and_count(left, right):
    merged = []
    count_merge = 0
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            count_merge += len(left) - i
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, count_merge
def count_inversion_merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers, 0
    mid = len(numbers)
    left_sorted, left_count = count_inversion_merge_sort(numbers[:mid])
    right_sorted, right_count = count_inversion_merge_sort(numbers[mid:])
    sorted_list, merge_count = merge_and_count(left_sorted, right_sorted)
    return sorted_list, left_count + right_count + merge_count
def partition(numbers):
    pivot = numbers[0]
    left, right = [], []
    count = 0
    for num in numbers[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
            count += len(left)
    return left, right, count
def count_inversion_quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers, 0
    left, right, count_partition = partition(numbers)
    left_sorted, left_count = count_inversion_quick_sort(left)
    right_sorted, right_count = count_inversion_quick_sort(right)
    return left_sorted + [numbers[0]] + right_sorted, left_count + right_count + count_partition
def run_count_inversion_merge_sort():
    with open('Q8.txt', 'r') as file:
        numbers = [int(line.strip()) for line in file.readlines()[:100000]]
    _, inversion_count = count_inversion_merge_sort(numbers)
    print('Number of Inversions (Merge Sort):', inversion_count)
def run_count_inversion_quick_sort():
    with open('Q8.txt', 'r') as file:
        numbers = [int(line.strip()) for line in file.readlines()[:100000]]
    _, inversion_count = count_inversion_quick_sort(numbers)
    print('Number of Inversions (Quick Sort):', inversion_count)
if __name__ == '__main__':
    t1 = Timer("run_count_inversion_merge_sort()", "from __main__ import run_count_inversion_merge_sort")
    t2 = Timer("run_count_inversion_quick_sort()", "from __main__ import run_count_inversion_quick_sort")
    turns = 1
    print('Time taken by Merge Sort (run %d time(s)):' % turns)
    print(t1.timeit(turns) / turns)
    print('Time taken by Quick Sort (run %d time(s)):' % turns)
    print(t2.timeit(turns) / turns)