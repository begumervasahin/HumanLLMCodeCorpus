from random import randint
from time import time
def quick_sort_2way(values, start, end):
    if start < end:
        pivot_index = partition_2way(values, start, end)
        quick_sort_2way(values, start, pivot_index)
        quick_sort_2way(values, pivot_index + 1, end)
def partition_2way(values, start, end):
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
def quick_sort_3way(values, start, end):
    if start < end:
        lt, gt = partition_3way(values, start, end)
        quick_sort_3way(values, start, lt - 1)
        quick_sort_3way(values, gt + 1, end)
def partition_3way(values, start, end):
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
    return lt, gt
def generate_random_list(size, max_value):
    return [randint(1, max_value) for _ in range(size)]
def main():
    print()
    n = int(input("Enter the list size: "))
    print()
    x = int(input("Enter the maximum element number (minimum is set at 1): "))
    print("(Hint: the lower the number, the higher the number of duplicate elements to demonstrate the algorithm's speed)")
    print()
    values = generate_random_list(n, x)
    values_2way = values[:]
    values_3way = values[:]
    start_time_2way = time()
    quick_sort_2way(values_2way, 0, n - 1)
    end_time_2way = time()
    print(f"The number of seconds for the 2-way sort was: {end_time_2way - start_time_2way:.8f}")
    start_time_3way = time()
    quick_sort_3way(values_3way, 0, n - 1)
    end_time_3way = time()
    print(f"The number of seconds for the 3-way sort was: {end_time_3way - start_time_3way:.8f}")
    print()
if __name__ == "__main__":
    main()