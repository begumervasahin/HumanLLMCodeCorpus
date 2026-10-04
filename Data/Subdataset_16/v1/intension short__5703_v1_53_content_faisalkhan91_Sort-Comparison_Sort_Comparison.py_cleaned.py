import random
import timeit
def fonk1(arr):
    print(' '.join(str(b7) for b7 in arr))
def fonk2(arr):
    b1 = len(arr)
    for b7 in range(1, b1):
        b2 = b7 - 1
        b3 = arr[b7]
        while b2 >= 0 and b3 < arr[b2]:
            arr[b2 + 1] = arr[b2]
            b2 -= 1
        arr[b2 + 1] = b3
def fonk3(alist):
    if len(alist) > 1:
        b4 = len(alist)
        b5 = alist[:b4]
        b6 = alist[b4:]
        fonk3(b5)
        fonk3(b6)
        b7 = b2 = k = 0
        while b7 < len(b5) and b2 < len(b6):
            if b5[b7] < b6[b2]:
                alist[k] = b5[b7]
                b7 += 1
            else:
                alist[k] = b6[b2]
                b2 += 1
            k += 1
        while b7 < len(b5):
            alist[k] = b5[b7]
            b7 += 1
            k += 1
        while b2 < len(b6):
            alist[k] = b6[b2]
            b2 += 1
            k += 1
def fonk4(blist):
    b8 = len(blist)
    for b7 in range(b8 - 1, 0, -1):
        for b2 in range(1, b7):
            if blist[b2] > blist[b2 + 1]:
                b3 = blist[b2]
                blist[b2] = blist[b2 + 1]
                blist[b2 + 1] = b3
b9 = merge_randoms = UNH_randoms = random.sample(range(10000), 10000)
print("Initial Array:")
fonk1(b9)
b10 = timeit.default_timer()
fonk2(b9)
b11 = timeit.default_timer()
b12 = timeit.default_timer()
fonk3(merge_randoms)
b13 = timeit.default_timer()
b14 = timeit.default_timer()
fonk4(UNH_randoms)
b15 = timeit.default_timer()
print("Insertion Sort Time: ", b11 - b10)
print("Merge Sort Time: ", b13 - b12)
print("UNH Sort Time: ", b15 - b14)