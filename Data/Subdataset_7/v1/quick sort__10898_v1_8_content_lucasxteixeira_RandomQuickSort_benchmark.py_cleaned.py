import timeit
import random
def fonk1(b8, l, r):
    if l < r:
        b1 = fonk2(b8, l, r)
        fonk1(b8, l, b1 - 1)
        fonk1(b8, b1 + 1, r)
def fonk2(b8, l, r):
    b2 = b8[r]
    b3 = l - 1
    for j in range(l, r):
        if b8[j] <= b2:
            b3 += 1
            b8[b3], b8[j] = b8[j], b8[b3]
    b8[b3 + 1], b8[r] = b8[r], b8[b3 + 1]
    return b3 + 1
def fonk3(b8, l, r):
    if l < r:
        b1 = fonk4(b8, l, r)
        fonk3(b8, l, b1 - 1)
        fonk3(b8, b1 + 1, r)
def fonk4(b8, l, r):
    b3 = random.randint(l, r)
    b8[r], b8[b3] = b8[b3], b8[r]
    return fonk2(b8, l, r)
def fonk5(b8, l, r):
    if l < r:
        b1 = fonk6(b8, l, r)
        fonk5(b8, l, b1 - 1)
        fonk5(b8, b1 + 1, r)
def fonk6(b8, l, r):
    b4 = fonk7(b8, l, r)
    b8[r], b8[b4] = b8[b4], b8[r]
    return fonk2(b8, l, r)
def fonk7(b8, l, r):
    b5 = (l + r)
    if b8[l] <= b8[b5] <= b8[r] or b8[r] <= b8[b5] <= b8[l]:
        return b5
    elif b8[b5] <= b8[l] <= b8[r] or b8[r] <= b8[l] <= b8[b5]:
        return l
    else:
        return r
if b6 = = "__main__":
    print("Quick Sort")
    for size in [1000, 10000, 100000]:
        b7 = [random.random() for _ in range(size)]
        print(f"{size} elements:")
        print(min(timeit.Timer('b8 = b7[:]; fonk1(b8, 0, len(b8) - 1)', globals=globals()).repeat(10, 100)))
    print("Random Quick Sort")
    for size in [1000, 10000, 100000]:
        b7 = [random.random() for _ in range(size)]
        print(f"{size} elements:")
        print(min(timeit.Timer('b8 = b7[:]; fonk3(b8, 0, len(b8) - 1)', globals=globals()).repeat(10, 100)))
    print("Median Random Quick Sort")
    for size in [1000, 10000, 100000]:
        b7 = [random.random() for _ in range(size)]
        print(f"{size} elements:")
        print(min(timeit.Timer('b8 = b7[:]; fonk5(b8, 0, len(b8) - 1)', globals=globals()).repeat(10, 100)))