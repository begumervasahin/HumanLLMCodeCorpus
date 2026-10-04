import random
def fonk1(b5, low, high):
    b1 = random.randint(low, high - 1)
    b2 = b5[b1]
    b5[b1], b5[high] = b5[high], b5[b1]
    b3 = low
    for j in range(low, high):
        if b5[j] <= b2:
            b5[b3], b5[j] = b5[j], b5[b3]
            b3 += 1
    b5[b3], b5[high] = b5[high], b5[b3]
    return b3
def fonk2(b5, low, high):
    if low < high:
        b3 = fonk1(b5, low, high)
        fonk2(b5, low, b3 - 1)
        fonk2(b5, b3 + 1, high)
if b4 = = "__main__":
    b5 = [10, 7, 8, 9, 1, 5]
    b6 = len(b5)
    fonk2(b5, 0, b6 - 1)
    print("Sorted array is:")
    print(b5)