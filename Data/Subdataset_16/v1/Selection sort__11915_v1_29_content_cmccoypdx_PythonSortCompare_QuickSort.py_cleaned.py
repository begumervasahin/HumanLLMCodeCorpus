import random
def fonk1(a, l, r):
    b1 = a[l]
    b2 = l
    b3 = r + 1
    while True:
        while True:
            b2 += 1
            if b2 >= len(a) or a[b2] >= b1:
                break
        while True:
            b3 -= 1
            if b3 < 0 or a[b3] <= b1:
                break
        if b2 >= b3:
            break
        a[b2], a[b3] = a[b3], a[b2]
    a[l], a[b3] = a[b3], a[l]
    return b3
def fonk2(a, l, r):
    if l < r:
        b4 = fonk1(a, l, r)
        fonk2(a, l, b4 - 1)
        fonk2(a, b4 + 1, r)
def fonk3(a):
    fonk2(a, 0, len(a) - 1)
if b5 = = "__main__":
    b6 = [random.randint(1, 100) for _ in range(10)]
    print("Array before sorting:", b6)
    fonk3(b6)
    print("Array after sorting:", b6)