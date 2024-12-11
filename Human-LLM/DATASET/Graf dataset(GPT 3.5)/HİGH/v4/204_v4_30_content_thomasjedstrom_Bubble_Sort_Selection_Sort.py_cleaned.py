import random
import datetime
b1 = []
def fonk1(x):
    for counter in range(0, 100):
        b2 = random.randint(0, 10000)
        x.append(b2)
    print('\nThis is your Sample List')
    print(b1)
fonk1(b1)
def fonk2(a):
    b3 = datetime.datetime.now()
    for counter in range(0, (len(a)-1)):
        for z in range(0, len(a)-1):
            if a[z] > a[z+1]:
                b4 = a[z]
                a[z] = a[z+1]
                a[z+1] = b4
    print('\nThis is your Bubble Sort')
    print(a)
    b5 = datetime.datetime.now()
    b6 = b5 - b3
    print('This operation took ' + str(b6) + ' seconds to complete')
fonk2(b1)
def fonk3(a):
    b3 = datetime.datetime.now()
    for x in range(0, len(a)):
        b7 = len(a) - 1 - x
        if x < b7:
            for z in range(x, b7+1):
                if a[z] < a[x]:
                    a[z], a[x] = a[x], a[z]
                if a[z] > a[b7]:
                    a[z], a[b7] = a[b7], a[z]
    print('\nThis is your Selection Sort')
    print(a)
    b5 = datetime.datetime.now()
    b6 = b5 - b3
    print('This operation took ' + str(b6) + ' seconds to complete')
fonk3(b1)