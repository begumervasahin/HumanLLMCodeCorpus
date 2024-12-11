import time
import random
def fonk1(b3):
    b1 = time.time()
    for i in range(1, len(b3)):
        b2 = i
        while b2 > 0 and b3[b2] < b3[b2 - 1]:
            b3[b2], b3[b2 - 1] = b3[b2 - 1], b3[b2]
            b2 -= 1
    return b3
b3 = [random.randint(1, 100) for _ in range(10)]
print("Unsorted b3:", b3)
b4 = fonk1(b3)
print("Sorted b3:", b4)