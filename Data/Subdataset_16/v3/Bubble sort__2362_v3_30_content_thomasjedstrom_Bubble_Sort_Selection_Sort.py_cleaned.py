import random
import datetime
def fonk1(b1 = 100, max_value=10000):
    b2 = [random.randint(0, max_value) for _ in range(b1)]
    print('\nThis is your Sample List:')
    print(b2)
    return b2
def fonk2(b2):
    b3 = datetime.datetime.now()
    b4 = len(b2)
    for i in range(b4 - 1):
        for j in range(b4 - 1 - i):
            if b2[j] > b2[j + 1]:
                b2[j], b2[j + 1] = b2[j + 1], b2[j]
    b5 = datetime.datetime.now()
    print('\nThis is your Bubble Sort:')
    print(b2)
    print('This operation took ' + str(b5 - b3) + ' seconds to complete')
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
    print('\nThis is your Selection Sort:')
    print(b2)
    print('This operation took ' + str(b5 - b3) + ' seconds to complete')
b7 = fonk1()
fonk2(b7.copy())
fonk3(b7.copy())