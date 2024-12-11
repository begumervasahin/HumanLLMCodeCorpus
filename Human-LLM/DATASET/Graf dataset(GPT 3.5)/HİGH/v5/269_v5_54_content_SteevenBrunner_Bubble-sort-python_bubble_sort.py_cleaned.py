import random
from time import time
a1 = 10001
b1 = random.sample(range(1, a1), a1 - 1)
def fonk1(arr):
    b2 = False
    while not b2:
        b2 = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                b2 = False
    return arr
b3 = b1[:]
b4 = time()
fonk1(b3)
b5 = time() - b4
print(f"Bubble sort: {b5} seconds to sort a list of {a1 - 1} items.")
b6 = b1[:]
b7 = time()
b6.sort()
b8 = time() - b7
print(f"System sort (Timsort): {b8} seconds to sort a list of {a1 - 1} items.")