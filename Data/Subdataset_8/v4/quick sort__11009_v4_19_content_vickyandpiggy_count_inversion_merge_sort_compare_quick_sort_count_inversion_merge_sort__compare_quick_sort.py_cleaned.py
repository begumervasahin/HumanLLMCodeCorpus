def merge_and_count(left, right):
    merged = []
    count_merge = 0
    i, j = 0, 0
    for k in range(len(left) + len(right)):
        if i < len(left) and (j >= len(right) or left[i] <= right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            count_merge += len(left) - i
    return merged, count_merge
def count_inversion_merge_sort(nums):
    if len(nums) <= 1:
        return nums, 0
    mid = len(nums)
    left_sorted, left_count = count_inversion_merge_sort(nums[:mid])
    right_sorted, right_count = count_inversion_merge_sort(nums[mid:])
    merged_sorted, merge_count = merge_and_count(left_sorted, right_sorted)
    total_count = left_count + right_count + merge_count
    return merged_sorted, total_count
def partition(nums):
    left = []
    right = []
    pivot = nums[0]
    nums = nums[::-1]
    count = 0
    for i in range(1, len(nums)):
        if nums[i] < pivot:
            left.append(nums[i])
        else:
            right.append(nums[i])
            count += len(left)
    count += len(left)
    nums = nums[::-1]
    left.reverse()
    right.reverse()
    return left, right, count
def count_inversion_quick_sort(nums):
    if len(nums) <= 1:
        return nums, 0
    left, right, throw_count = partition(nums)
    left_sorted, left_count = count_inversion_quick_sort(left)
    right_sorted, right_count = count_inversion_quick_sort(right)
    total_count = left_count + right_count + throw_count
    return left_sorted + [nums[0]] + right_sorted, total_count
def run_count_inversion_merge_sort():
    with open('Q8.txt', 'r') as f:
        numbers = f.readlines()
    numbers = [int(n.strip()) for n in numbers[:100000]]
    sorted_numbers, inversion_count = count_inversion_merge_sort(numbers)
    print('Number of Inversions:')
    print(inversion_count)
def run_count_inversion_quick_sort():
    with open('Q8.txt', 'r') as f:
        numbers = f.readlines()
    numbers = [int(n.strip()) for n in numbers[:100000]]
    sorted_numbers, inversion_count = count_inversion_quick_sort(numbers)
    print('Number of Inversions:')
    print(inversion_count)
if __name__ == '__main__':
    from timeit import Timer
    t1 = Timer("run_count_inversion_merge_sort()", "from __main__ import run_count_inversion_merge_sort")
    turns = 1
    print('Time: (ran %d time(s))' % turns)
    print(t1.timeit(turns) / turns)
    t2 = Timer("run_count_inversion_quick_sort()", "from __main__ import run_count_inversion_quick_sort")
    turns = 1
    print('Time: (ran %d time(s))' % turns)
    print(t2.timeit(turns) / turns)