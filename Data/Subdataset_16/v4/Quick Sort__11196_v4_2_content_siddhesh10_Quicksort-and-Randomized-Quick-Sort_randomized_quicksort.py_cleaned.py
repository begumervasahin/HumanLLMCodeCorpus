import random
def fonk1(b6, low, high):
    b1 = random.randint(low, high - 1)
    b2 = b6[b1]
    b6[b1], b6[high] = b6[high], b6[b1]
    b3 = low
    for j in range(low, high):
        if b6[j] <= b2:
            b6[b3], b6[j] = b6[j], b6[b3]
            b3 += 1
    b6[b3], b6[high] = b6[high], b6[b3]
    return b3
def fonk2(b6, low, high):
    if low < high:
        b4 = fonk1(b6, low, high)
        fonk2(b6, low, b4 - 1)
        fonk2(b6, b4 + 1, high)
if b5 = = "__main__":
    b6 = [10, 7, 8, 9, 1, 5]
    b7 = len(b6)
    fonk2(b6, 0, b7 - 1)
    print("Sorted array is:")
    print(b6)