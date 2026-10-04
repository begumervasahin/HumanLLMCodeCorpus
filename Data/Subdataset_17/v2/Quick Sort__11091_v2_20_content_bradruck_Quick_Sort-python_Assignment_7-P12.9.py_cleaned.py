from random import randint
from time import time
def quick_sort_two_way(values, start, end):
    if start >= end:
        return
    pivot_index = partition_two_way(values, start, end)
    quick_sort_two_way(values, start, pivot_index)
    quick_sort_two_way(values, pivot_index + 1, end)
def partition_two_way(values, start, end):
    pivot = values[start]
    i = start - 1
    j = end + 1
    while True:
        i += 1
        while values[i] < pivot:
            i += 1
        j -= 1
        while values[j] > pivot:
            j -= 1
        if i >= j:
            return j
        swap(values, i, j)
def quick_sort_three_way(values, start, end):
    if start >= end:
        return
    pivot = values[start]
    low = mid = start
    high = end
    while mid <= high:
        if values[mid] < pivot:
            swap(values, low, mid)
            low += 1
            mid += 1
        elif values[mid] == pivot:
            mid += 1
        else:
            swap(values, mid, high)
            high -= 1
    quick_sort_three_way(values, start, low - 1)
    quick_sort_three_way(values, high + 1, end)
def swap(values, i, j):
    values[i], values[j] = values[j], values[i]
def main():
    print()
    n = int(input("Enter the list size: "))
    print("\nEnter the maximum element number for the list (minimum is set to 1): ")
    x = int(input("(Hint: Lower numbers result in more duplicate elements for speed testing): "))
    values_two_way = [randint(1, x) for _ in range(n)]
    values_three_way = values_two_way[:]
    start_time_two_way = time()
    quick_sort_two_way(values_two_way, 0, n - 1)
    end_time_two_way = time()
    print("\nTime taken for 2-way sort: %.8f seconds" % (end_time_two_way - start_time_two_way))
    start_time_three_way = time()
    quick_sort_three_way(values_three_way, 0, n - 1)
    end_time_three_way = time()
    print("\nTime taken for 3-way sort: %.8f seconds" % (end_time_three_way - start_time_three_way))
    print()
if __name__ == "__main__":
    main()