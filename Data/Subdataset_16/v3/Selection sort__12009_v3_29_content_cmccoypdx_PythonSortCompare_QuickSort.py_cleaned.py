import random
def fonk1(b5, low, high):
    b1 = b5[low]
    b2 = low
    b3 = high + 1
    while True:
        while b2 < high and b5[b2] < b1:
            b2 += 1
        while b3 > low and b5[b3] > b1:
            b3 -= 1
        if b2 >= b3:
            break
        b5[b2], b5[b3] = b5[b3], b5[b2]
    b5[low], b5[b3] = b5[b3], b5[low]
    return b3
def fonk2(b5, low, high):
    if low < high:
        b4 = fonk1(b5, low, high)
        fonk2(b5, low, b4 - 1)
        fonk2(b5, b4 + 1, high)
def fonk3(b5):
    fonk2(b5, 0, len(b5) - 1)
def fonk4():
    b5 = [random.randint(1, 100) for _ in range(10)]
    print("Array before sorting:", b5)
    fonk3(b5)
    print("Array after sorting:", b5)
if b6 = = "__main__":
    fonk4()