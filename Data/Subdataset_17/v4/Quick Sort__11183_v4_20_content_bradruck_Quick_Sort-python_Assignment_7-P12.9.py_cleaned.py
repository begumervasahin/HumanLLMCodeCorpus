from random import randint
from time import time
def quick_sort_2way(values, start, end):
    if start >= end:
        return
    pivot_index = partition_2way(values, start, end)
    quick_sort_2way(values, start, pivot_index)
    quick_sort_2way(values, pivot_index + 1, end)
def partition_2way(values, start, end):
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
        values[i], values[j] = values[j], values[i]
def quick_sort_3way(values, start, end):
    if start >= end:
        return
    pivot = values[start]
    lt = start
    gt = end
    i = start
    while i <= gt:
        if values[i] < pivot:
            values[lt], values[i] = values[i], values[lt]
            lt += 1
            i += 1
        elif values[i] > pivot:
            values[i], values[gt] = values[gt], values[i]
            gt -= 1
        else:
            i += 1
    quick_sort_3way(values, start, lt - 1)
    quick_sort_3way(values, gt + 1, end)
def main():
    print()
    n = int(input("Enter the list size: "))
    print()
    x = int(input("Enter the maximum element number (minimum is set at 1): "))
    print("(Hint, the lower the number, the higher number of duplicate elements with which to prove the algorithm's speed)")
    print()
    values = [randint(1, x) for _ in range(n)]
    values_2way = values[:]
    values_3way = values[:]
    start_time_2way = time()
    quick_sort_2way(values_2way, 0, n - 1)
    end_time_2way = time()
    print("The number of seconds for the 2-way sort was:  %.8f" % (end_time_2way - start_time_2way))
    start_time_3way = time()
    quick_sort_3way(values_3way, 0, n - 1)
    end_time_3way = time()
    print("The number of seconds for the 3-way sort was:  %.8f" % (end_time_3way - start_time_3way))
    print()
if __name__ == "__main__":
    main()