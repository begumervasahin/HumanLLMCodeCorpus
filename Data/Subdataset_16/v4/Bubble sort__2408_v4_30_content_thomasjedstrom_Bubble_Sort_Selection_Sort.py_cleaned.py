import random
import datetime
def fonk1(lst, b1 = 100, upper_limit=10000):
    for _ in range(b1):
        b2 = random.randint(0, upper_limit)
        lst.append(b2)
    print('\nThis is your Sample List')
    print(lst)
def fonk2(lst):
    b3 = datetime.datetime.now()
    b4 = len(lst)
    for i in range(b4):
        for j in range(0, b4 - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    b5 = datetime.datetime.now()
    print('\nThis is your Bubble Sort')
    print(lst)
    print(f'This operation took {b5 - b3} seconds to complete')
def fonk3(lst):
    b3 = datetime.datetime.now()
    b4 = len(lst)
    for i in range(b4):
        b6 = i
        for j in range(i + 1, b4):
            if lst[j] < lst[b6]:
                b6 = j
        lst[i], lst[b6] = lst[b6], lst[i]
    b5 = datetime.datetime.now()
    print('\nThis is your Selection Sort')
    print(lst)
    print(f'This operation took {b5 - b3} seconds to complete')
b7 = []
fonk1(b7)
b8 = b7[:]
b9 = b7[:]
fonk2(b8)
fonk3(b9)