import random
import numpy as np
import time
def fonk1(b6):
    b1 = time.process_time()
    b2 = len(b6)
    for i in range(b2):
        b3 = i
        for j in range(i + 1, b2):
            if b6[b3] > b6[j]:
                b3 = j
        b6[i], b6[b3] = b6[b3], b6[i]
    b4 = time.process_time()
    b5 = b4 - b1
    return b5
def fonk2():
    a1 = 40
    b6 = np.random.randint(0, 99999, a1)
    print("Random order:")
    print("Before sorting:", b6)
    b5 = fonk1(b6)
    print("After sorting:", b6)
    print("Execution time:", b5, "seconds")
    print("\nAscending order:")
    b6.sort()
    print("Before sorting:", b6)
    b5 = fonk1(b6)
    print("After sorting:", b6)
    print("Execution time:", b5, "seconds")
    print("\nReverse order:")
    b6 = b6[::-1]
    print("Before sorting:", b6)
    b5 = fonk1(b6)
    print("After sorting:", b6)
    print("Execution time:", b5, "seconds")
if b7 = = "__main__":
    fonk2()