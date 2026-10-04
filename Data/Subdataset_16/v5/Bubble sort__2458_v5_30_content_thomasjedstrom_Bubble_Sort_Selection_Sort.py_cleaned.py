import random
import datetime
def fonk1(b1 = 100, upper_limit=10000):
    b2 = [random.randint(0, upper_limit) for _ in range(b1)]
    print('\nThis is your Sample List')
    print(b2)
    return b2
def fonk2(b2):
    b3 = datetime.datetime.now()
    b4 = len(b2)
    for i in range(b4):
        for j in range(0, b4 - i - 1):
            if b2[j] > b2[j + 1]:
                b2[j], b2[j + 1] = b2[j + 1], b2[j]
    b5 = datetime.datetime.now()
    print('\nThis is your Bubble Sort')
    print(b2)
    print(f'This operation took {b5 - b3} seconds to complete')
    return b2
def fonk3(b2):
    b3 = datetime.datetime.now()
    b4 = len(b2)
    for i in range(b4):
        b6 = i
        for j in range(i + 1, b4):
            if b2[j] < b2[b6]:
                b6 = j
        b2[i], b2[b6] = b2[b6], b2[i]
    b5 = datetime.datetime.now()
    print('\nThis is your Selection Sort')
    print(b2)
    print(f'This operation took {b5 - b3} seconds to complete')
    return b2
b7 = fonk1()
b8 = b7[:]
b9 = b7[:]
fonk2(b8)
fonk3(b9)