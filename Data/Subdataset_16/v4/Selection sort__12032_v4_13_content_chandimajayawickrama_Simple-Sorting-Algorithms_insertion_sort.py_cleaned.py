import time
import random
def fonk1(b6):
    b1 = time.time()
    for i in range(1, len(b6)):
        b2 = b6[i]
        b3 = i - 1
        while b3 >= 0 and b2 < b6[b3]:
            b6[b3 + 1] = b6[b3]
            b3 -= 1
        b6[b3 + 1] = b2
    b4 = time.time()
    print(f"Sorted b6: {b6}")
    print(f"Time taken: {b4 - b1} seconds")
    return b6
if b5 = = "__main__":
    b6 = [random.randint(0, 100) for _ in range(10)]
    print(f"Original b6: {b6}")
    fonk1(b6)