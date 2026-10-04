import time
import random
def fonk1(b4):
    b1 = time.time()
    for i in range(len(b4) - 1):
        b2 = i
        for j in range(i + 1, len(b4)):
            if b4[b2] > b4[j]:
                b2 = j
        b4[i], b4[b2] = b4[b2], b4[i]
    b3 = time.time()
    print(f"Sorting completed in {b3 - b1:.6f} seconds")
    return b4
def fonk2():
    b4 = [random.randint(0, 100) for _ in range(10)]
    print("Original b4:", b4)
    b5 = fonk1(b4)
    print("Sorted b4:", b5)
if b6 = = "__main__":
    fonk2()