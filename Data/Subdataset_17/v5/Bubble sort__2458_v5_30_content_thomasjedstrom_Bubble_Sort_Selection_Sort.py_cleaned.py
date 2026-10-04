import random
import datetime
def populate_list(size=100, upper_limit=10000):
    lst = [random.randint(0, upper_limit) for _ in range(size)]
    print('\nThis is your Sample List')
    print(lst)
    return lst
def bubble_sort(lst):
    start_time = datetime.datetime.now()
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    end_time = datetime.datetime.now()
    print('\nThis is your Bubble Sort')
    print(lst)
    print(f'This operation took {end_time - start_time} seconds to complete')
    return lst
def selection_sort(lst):
    start_time = datetime.datetime.now()
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    end_time = datetime.datetime.now()
    print('\nThis is your Selection Sort')
    print(lst)
    print(f'This operation took {end_time - start_time} seconds to complete')
    return lst
sample_list = populate_list()
bubble_sort_list = sample_list[:]
selection_sort_list = sample_list[:]
bubble_sort(bubble_sort_list)
selection_sort(selection_sort_list)