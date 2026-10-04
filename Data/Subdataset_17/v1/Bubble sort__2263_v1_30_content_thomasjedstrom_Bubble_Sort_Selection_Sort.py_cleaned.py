import random
import datetime
def pop(x):
    for counter in range(100):
        random_num = random.randint(0, 10000)
        x.append(random_num)
    print('\nThis is your Sample List')
    print(x)
def bubble_sort(a):
    start_time = datetime.datetime.now()
    for counter in range(len(a) - 1):
        for z in range(len(a) - 1):
            if a[z] > a[z + 1]:
                a[z], a[z + 1] = a[z + 1], a[z]
    print('\nThis is your Bubble Sort')
    print(a)
    end_time = datetime.datetime.now()
    calc_time = end_time - start_time
    print('This operation took ' + str(calc_time) + ' seconds to complete')
def selection_sort(a):
    start_time = datetime.datetime.now()
    for x in range(len(a)):
        y = len(a) - 1 - x
        if x < y:
            for z in range(x, y + 1):
                if a[z] < a[x]:
                    a[z], a[x] = a[x], a[z]
                if a[z] > a[y]:
                    a[z], a[y] = a[y], a[z]
    print('\nThis is your Selection Sort')
    print(a)
    end_time = datetime.datetime.now()
    calc_time = end_time - start_time
    print('This operation took ' + str(calc_time) + ' seconds to complete')
sample_list = []
pop(sample_list)
bubble_sort(sample_list.copy())
selection_sort(sample_list.copy())