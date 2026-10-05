def merge_and_count(left, right):
    merged_list = []
    inversion_count = 0
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            merged_list.append(right[j])
            inversion_count += len(left) - i
            j += 1
        else:
            merged_list.append(left[i])
            i += 1
    merged_list.extend(left[i:])
    merged_list.extend(right[j:])
    return merged_list, inversion_count
def count_inversion_merge_sort(numbers):
    count = 0
    length = len(numbers)
    if length <= 1:
        return numbers, count
    mid = length
    left_half, right_half = numbers[:mid], numbers[mid:]
    sorted_left, left_count = count_inversion_merge_sort(left_half)
    sorted_right, right_count = count_inversion_merge_sort(right_half)
    sorted_numbers, merge_count = merge_and_count(sorted_left, sorted_right)
    count = left_count + right_count + merge_count
    return sorted_numbers, count
def partition(numbers):
    count = 0
    left, right = [], []
    pivot = numbers[0]
    for num in numbers[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
            count += len(left)
    return left, right, count
def count_inversion_quick_sort(numbers):
    count = 0
    length = len(numbers)
    if length <= 1:
        return numbers, count
    left, right, throw_count = partition(numbers)
    left_sorted, left_count = count_inversion_quick_sort(left)
    right_sorted, right_count = count_inversion_quick_sort(right)
    count = left_count + right_count + throw_count
    return left_sorted + [numbers[0]] + right_sorted, count
def run_count_inversion_merge_sort():
    import string
    with open('Q8.txt', 'r') as file:
        numbers = file.readlines()
    numbers = [string.atoi(n.strip()) for n in numbers[:100000]]
    sorted_numbers, inversion_count = count_inversion_merge_sort(numbers)
    print('Number of Inversions:')
    print(inversion_count)
def run_count_inversion_quick_sort():
    import string
    with open('Q8.txt', 'r') as file:
        numbers = file.readlines()
    numbers = [string.atoi(n.strip()) for n in numbers[:100000]]
    sorted_numbers, inversion_count = count_inversion_quick_sort(numbers)
    print('Number of Inversions:')
    print(inversion_count)
if __name__ == '__main__':
    from timeit import Timer
    t1 = Timer("run_count_inversion_merge_sort()", "from __main__ import run_count_inversion_merge_sort")
    turns = 1
    print(t1.timeit(turns) / turns)
    t2 = Timer("run_count_inversion_quick_sort()", "from __main__ import run_count_inversion_quick_sort")
    print(t2.timeit(turns) / turns)