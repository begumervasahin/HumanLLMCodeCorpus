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
def count_inversion_merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr)
    left, left_count = count_inversion_merge_sort(arr[:mid])
    right, right_count = count_inversion_merge_sort(arr[mid:])
    merged, merge_count = merge_and_count(left, right)
    total_count = left_count + right_count + merge_count
    return merged, total_count
def partition(arr):
    pivot = arr[0]
    left = []
    right = []
    count = 0
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
            count += len(left)
    count += len(left)
    return left, right, count
def count_inversion_quick_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    left, right, count_partition = partition(arr)
    sorted_left, left_count = count_inversion_quick_sort(left)
    sorted_right, right_count = count_inversion_quick_sort(right)
    total_count = left_count + right_count + count_partition
    return sorted_left + [arr[0]] + sorted_right, total_count
def run_count_inversion_merge_sort():
    with open('Q8.txt', 'r') as file:
        numbers = file.read().splitlines()[:100000]
    numbers = [int(n) for n in numbers]
    _, inversion_count = count_inversion_merge_sort(numbers)
    print('Number of Inversions:', inversion_count)
def run_count_inversion_quick_sort():
    with open('Q8.txt', 'r') as file:
        numbers = file.read().splitlines()[:100000]
    numbers = [int(n) for n in numbers]
    _, inversion_count = count_inversion_quick_sort(numbers)
    print('Number of Inversions:', inversion_count)
if __name__ == '__main__':
    from timeit import Timer
    turns = 1
    t1 = Timer("run_count_inversion_merge_sort()", "from __main__ import run_count_inversion_merge_sort")
    time_merge_sort = t1.timeit(turns) / turns
    print('Merge Sort Time: (run {} time(s))'.format(turns))
    print(time_merge_sort)
    t2 = Timer("run_count_inversion_quick_sort()", "from __main__ import run_count_inversion_quick_sort")
    time_quick_sort = t2.timeit(turns) / turns
    print('Quick Sort Time: (run {} time(s))'.format(turns))
    print(time_quick_sort)