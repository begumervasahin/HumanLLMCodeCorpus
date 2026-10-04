import time
import random
def fonk1(b5):
    b1 = time.time()
    for i in range(len(b5) - 1):
        b2 = i
        for j in range(i + 1, len(b5)):
            if b5[b2] > b5[j]:
                b2 = j
        b5[i], b5[b2] = b5[b2], b5[i]
    b3 = time.time()
    print(f"Time taken to sort the b5: {b3 - b1} seconds")
    return b5
if b4 = = "__main__":
    b5 = [random.randint(0, 1000) for _ in range(100)]
    print("Original b5:", b5)
    b6 = fonk1(b5)
    print("Sorted b5:", b6)