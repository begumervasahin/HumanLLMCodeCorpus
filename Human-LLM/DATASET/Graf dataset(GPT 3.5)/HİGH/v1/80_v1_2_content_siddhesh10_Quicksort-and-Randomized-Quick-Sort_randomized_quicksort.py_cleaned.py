import random
def fonk1(b5, low, high):
    b1 = low
    b2 = random.randint(low, high - 1)
    b3 = b5[b2]
    b5[high], b5[b2] = b5[b2], b5[high]
    for j in range(low, high):
        if b5[j] <= b3:
            b5[b1], b5[j] = b5[j], b5[b1]
            b1 = b1 + 1
    b5[b1], b5[high] = b5[high], b5[b1]
    return b1
def fonk2(b5, low, high):
    if low < high:
        b4 = fonk1(b5, low, high)
        fonk2(b5, low, b4 - 1)
        fonk2(b5, b4 + 1, high)
b5 = [10, 7, 8, 9, 1, 5]
b6 = len(b5)
fonk2(b5, 0, b6 - 1)
print("Sorted array is:")
print(b5)