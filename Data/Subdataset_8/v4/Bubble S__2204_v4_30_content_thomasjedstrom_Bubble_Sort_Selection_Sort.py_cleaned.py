import random
import datetime
sample_list = []
def populate_list(x):
    for counter in range(0, 100):
        random_num = random.randint(0, 10000)
        x.append(random_num)
    print('\nThis is your Sample List')
    print(sample_list)
populate_list(sample_list)
def bubble_sort(a):
    startTime = datetime.datetime.now()
    for counter in range(0, (len(a)-1)):
        for z in range(0, len(a)-1):
            if a[z] > a[z+1]:
                temp = a[z]
                a[z] = a[z+1]
                a[z+1] = temp
    print('\nThis is your Bubble Sort')
    print(a)
    endTime = datetime.datetime.now()
    calcdTime = endTime - startTime
    print('This operation took ' + str(calcdTime) + ' seconds to complete')
bubble_sort(sample_list)
def selection_sort(a):
    startTime = datetime.datetime.now()
    for x in range(0, len(a)):
        y = len(a) - 1 - x
        if x < y:
            for z in range(x, y+1):
                if a[z] < a[x]:
                    a[z], a[x] = a[x], a[z]
                if a[z] > a[y]:
                    a[z], a[y] = a[y], a[z]
    print('\nThis is your Selection Sort')
    print(a)
    endTime = datetime.datetime.now()
    calcdTime = endTime - startTime
    print('This operation took ' + str(calcdTime) + ' seconds to complete')
selection_sort(sample_list)