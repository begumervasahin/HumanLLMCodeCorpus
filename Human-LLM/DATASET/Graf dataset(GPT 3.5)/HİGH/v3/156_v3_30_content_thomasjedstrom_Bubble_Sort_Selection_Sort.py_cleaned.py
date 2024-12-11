import random
import time
def fonk1(b6):
    for _ in range(100):
        b1 = random.randint(0, 10000)
        b6.append(b1)
    print('\nThis is your Sample List:')
    print(b6)
def fonk2(b6):
    b2 = time.time()
    for i in range(len(b6) - 1):
        for j in range(len(b6) - 1):
            if b6[j] > b6[j + 1]:
                b6[j], b6[j + 1] = b6[j + 1], b6[j]
    print('\nThis is your Bubble Sort:')
    print(b6)
    b3 = time.time()
    b4 = b3 - b2
    print(f'This operation took {b4:.6f} seconds to complete')
def fonk3(b6):
    b2 = time.time()
    for x in range(len(b6)):
        for y in range(len(b6) - 1 - x):
            if b6[y] > b6[y + 1]:
                b6[y], b6[y + 1] = b6[y + 1], b6[y]
    print('\nThis is your Selection Sort:')
    print(b6)
    b3 = time.time()
    b4 = b3 - b2
    print(f'This operation took {b4:.6f} seconds to complete')
if b5 = = "__main__":
    b6 = []
    fonk1(b6)
    fonk2(b6[:])
    fonk3(b6[:])