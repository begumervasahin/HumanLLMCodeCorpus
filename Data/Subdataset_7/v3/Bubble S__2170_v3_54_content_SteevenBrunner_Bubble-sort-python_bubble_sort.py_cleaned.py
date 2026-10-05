import random
from time import time
a1 = 10000
a2 = 10000
b1 = random.sample(range(1, a2 + 1), a1)
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
b5 = time()
print(f"Bubble sort took {b5 - b4:.6f} seconds to sort a list of {a1} items.")
b3 = b1[:]
b4 = time()
b3.sort()
b5 = time()
print(f"System Python sort (Timsort) took {b5 - b4:.6f} seconds to sort a list of {a1} items.")