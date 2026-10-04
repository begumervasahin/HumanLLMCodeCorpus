import random
import datetime
def populate_list(lst, num_elements=100, max_value=10000):
    for _ in range(num_elements):
        random_num = random.randint(0, max_value)
        lst.append(random_num)
    print('\nThis is your Sample List:')
    print(lst)
def bubble_sort(lst):
    start_time = datetime.datetime.now()
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    end_time = datetime.datetime.now()
    print('\nThis is your Bubble Sort:')
    print(lst)
    print('This operation took ' + str(end_time - start_time) + ' seconds to complete')
def selection_sort(lst):
    start_time = datetime.datetime.now()
    n = len(lst)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    end_time = datetime.datetime.now()
    print('\nThis is your Selection Sort:')
    print(lst)
    print('This operation took ' + str(end_time - start_time) + ' seconds to complete')
sample_list = []
populate_list(sample_list)
bubble_sort(sample_list.copy())
selection_sort(sample_list.copy())