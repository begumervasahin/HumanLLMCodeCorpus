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
            j += 1
            count_merge += len(left) - i
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, count_merge
def count_inversions_merge_sort(nums):
    if len(nums) <= 1:
        return nums, 0
    mid = len(nums)
    left_sorted, left_count = count_inversions_merge_sort(nums[:mid])
    right_sorted, right_count = count_inversions_merge_sort(nums[mid:])
    merged_sorted, merge_count = merge_and_count(left_sorted, right_sorted)
    total_count = left_count + right_count + merge_count
    return merged_sorted, total_count
def partition(nums):
    left = []
    right = []
    pivot = nums[0]
    nums = nums[::-1]
    count = 0
    for num in nums[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
            count += len(left)
    count += len(left)
    left.reverse()
    right.reverse()
    return left, right, count
def count_inversions_quick_sort(nums):
    if len(nums) <= 1:
        return nums, 0
    left, right, throw_count = partition(nums)
    left_sorted, left_count = count_inversions_quick_sort(left)
    right_sorted, right_count = count_inversions_quick_sort(right)
    total_count = left_count + right_count + throw_count
    return left_sorted + [nums[0]] + right_sorted, total_count
def run_count_inversions_merge_sort():
    with open('Q8.txt', 'r') as file:
        numbers = [int(line.strip()) for line in file.readlines()[:100000]]
    sorted_numbers, inversion_count = count_inversions_merge_sort(numbers)
    print('Number of Inversions:')
    print(inversion_count)
def run_count_inversions_quick_sort():
    with open('Q8.txt', 'r') as file:
        numbers = [int(line.strip()) for line in file.readlines()[:100000]]
    sorted_numbers, inversion_count = count_inversions_quick_sort(numbers)
    print('Number of Inversions:')
    print(inversion_count)
if __name__ == '__main__':
    from timeit import Timer
    t1 = Timer("run_count_inversions_merge_sort()", "from __main__ import run_count_inversions_merge_sort")
    turns = 1
    print('Time: (ran %d time(s))' % turns)
    print(t1.timeit(turns) / turns)
    t2 = Timer("run_count_inversions_quick_sort()", "from __main__ import run_count_inversions_quick_sort")
    turns = 1
    print('Time: (ran %d time(s))' % turns)
    print(t2.timeit(turns) / turns)