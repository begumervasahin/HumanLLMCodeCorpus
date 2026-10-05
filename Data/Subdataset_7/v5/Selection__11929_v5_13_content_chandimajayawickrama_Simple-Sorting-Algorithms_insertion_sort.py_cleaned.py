import random
def fonk1(b3):
    for i in range(1, len(b3)):
        b1 = i
        while b1 > 0 and b3[b1] < b3[b1 - 1]:
            b3[b1], b3[b1 - 1] = b3[b1 - 1], b3[b1]
            b1 -= 1
    return b3
if b2 = = "__main__":
    b3 = [random.randint(1, 100) for _ in range(10)]
    print("Unsorted b3:", b3)
    b4 = fonk1(b3.copy())
    print("Sorted b3:", b4)