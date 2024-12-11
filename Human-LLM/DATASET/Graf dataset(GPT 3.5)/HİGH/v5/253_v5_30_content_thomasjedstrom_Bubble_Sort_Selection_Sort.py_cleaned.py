import random
import datetime
b1 = []
def fonk1(x, b2 = 100):
    for _ in range(b2):
        b3 = random.randint(0, 10000)
        x.append(b3)
    print('\nThis is your Sample List')
    print(b1)
def fonk2(a):
    b4 = datetime.datetime.now()
    b5 = len(a)
    for i in range(b5 - 1):
        for j in range(b5 - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    print('\nThis is your Bubble Sort')
    print(a)
    b6 = datetime.datetime.now()
    b7 = b6 - b4
    print('This operation took ' + str(b7) + ' seconds to complete')
def fonk3(a):
    b4 = datetime.datetime.now()
    b5 = len(a)
    for i in range(b5):
        b8 = i
        for j in range(i + 1, b5):
            if a[j] < a[b8]:
                b8 = j
        if b8 != i:
            a[i], a[b8] = a[b8], a[i]
    print('\nThis is your Selection Sort')
    print(a)
    b6 = datetime.datetime.now()
    b7 = b6 - b4
    print('This operation took ' + str(b7) + ' seconds to complete')
if b9 = = "__main__":
    fonk1(b1)
    b10 = b1.copy()
    fonk2(b10)
    b11 = b1.copy()
    fonk3(b11)