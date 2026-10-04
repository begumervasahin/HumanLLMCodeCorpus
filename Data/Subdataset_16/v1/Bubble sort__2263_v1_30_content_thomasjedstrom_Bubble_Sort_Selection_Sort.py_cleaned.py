import random
import datetime
def fonk1(x):
    for counter in range(100):
        b1 = random.randint(0, 10000)
        x.append(b1)
    print('\nThis is your Sample List')
    print(x)
def fonk2(a):
    b2 = datetime.datetime.now()
    for counter in range(len(a) - 1):
        for z in range(len(a) - 1):
            if a[z] > a[z + 1]:
                a[z], a[z + 1] = a[z + 1], a[z]
    print('\nThis is your Bubble Sort')
    print(a)
    b3 = datetime.datetime.now()
    b4 = b3 - b2
    print('This operation took ' + str(b4) + ' seconds to complete')
def fonk3(a):
    b2 = datetime.datetime.now()
    for x in range(len(a)):
        b5 = len(a) - 1 - x
        if x < b5:
            for z in range(x, b5 + 1):
                if a[z] < a[x]:
                    a[z], a[x] = a[x], a[z]
                if a[z] > a[b5]:
                    a[z], a[b5] = a[b5], a[z]
    print('\nThis is your Selection Sort')
    print(a)
    b3 = datetime.datetime.now()
    b4 = b3 - b2
    print('This operation took ' + str(b4) + ' seconds to complete')
b6 = []
fonk1(b6)
fonk2(b6.copy())
fonk3(b6.copy())