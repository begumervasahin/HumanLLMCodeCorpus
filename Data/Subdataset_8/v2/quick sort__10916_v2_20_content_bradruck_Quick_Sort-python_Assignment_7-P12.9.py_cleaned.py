from random import randint
from time import time
def quick_sort_2_way(values, start, end):
    if start >= end:
        return
    pivot_index = partition_2_way(values, start, end)
    quick_sort_2_way(values, start, pivot_index)
    quick_sort_2_way(values, pivot_index + 1, end)
def partition_2_way(values, start, end):
    pivot = values[start]
    left = start - 1
    right = end + 1
    while True:
        left += 1
        while values[left] < pivot:
            left += 1
        right -= 1
        while values[right] > pivot:
            right -= 1
        if left >= right:
            return right
        values[left], values[right] = values[right], values[left]
def quick_sort_3_way(values, start, end):
    if start >= end:
        return
    pivot = values[start]
    equal_to_pivot_index = i = start
    greater_than_pivot_index = end
    while i <= greater_than_pivot_index:
        if values[i] < pivot:
            values[i], values[equal_to_pivot_index] = values[equal_to_pivot_index], values[i]
            equal_to_pivot_index += 1
            i += 1
        elif values[i] == pivot:
            i += 1
        else:
            values[i], values[greater_than_pivot_index] = values[greater_than_pivot_index], values[i]
            greater_than_pivot_index -= 1
    quick_sort_3_way(values, start, equal_to_pivot_index)
    quick_sort_3_way(values, greater_than_pivot_index + 1, end)
def main():
    print()
    n = int(input("Enter the size of the list: "))
    print()
    print("Enter the maximum value for list elements (minimum is set at 1)")
    x = int(input("(Hint: lower numbers result in more duplicate elements for testing algorithm speed): "))
    values_2_way = [randint(1, x) for _ in range(n)]
    values_3_way = values_2_way.copy()
    start_time_2_way = time()
    quick_sort_2_way(values_2_way, 0, n - 1)
    end_time_2_way = time()
    print()
    print("Time taken for 2-way sort: %.8f seconds" % (end_time_2_way - start_time_2_way))
    start_time_3_way = time()
    quick_sort_3_way(values_3_way, 0, n - 1)
    end_time_3_way = time()
    print()
    print("Time taken for 3-way sort: %.8f seconds" % (end_time_3_way - start_time_3_way))
    print()
if __name__ == "__main__":
    main()