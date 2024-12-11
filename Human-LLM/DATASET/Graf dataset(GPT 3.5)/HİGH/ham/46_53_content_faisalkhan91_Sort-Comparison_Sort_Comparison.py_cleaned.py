import random
import timeit
def fonk1(arr):
    print(' '.join(str(a1) for a1 in arr))
def fonk2(arr):
    b1 = len(arr)
    for a1 in range(1, b1):
        b2 = a1 - 1
        b3 = arr[a1]
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
        a1 = 0
        b2 = 0
        a2 = 0
        while a1 < len(b5) and b2 < len(b6):
            if b5[a1] < b6[b2]:
                alist[a2] = b5[a1]
                a1 = a1+1
            else:
                alist[a2] = b6[b2]
                b2 = b2+1
            a2 = a2+1
        while a1 < len(b5):
            alist[a2] = b5[a1]
            a1 = a1+1
            a2 = a2+1
        while b2 < len(b6):
            alist[a2] = b6[b2]
            b2 = b2+1
            a2 = a2+1
def fonk4(blist):
    b7 = len(blist)
    for a1 in range(b7-1, 0, -1):
        for b2 in range(1, a1):
            if blist[b2] > blist[b2+1]:
                b3 = blist[b2]
                blist[b2] = blist[b2+1]
                blist[b2+1] = b3
b8 = merge_randoms = UNH_randoms = random.sample(range(10000), 10000)
print("Initial Array :",)
fonk1(b8)
b9 = timeit.default_timer()
fonk2(b8)
b10 = timeit.default_timer()
b11 = timeit.default_timer()
fonk3(merge_randoms)
b12 = timeit.default_timer()
b13 = timeit.default_timer()
fonk4(UNH_randoms)
b14 = timeit.default_timer()
print("Insertion Sort Time: ", b10 - b9)
print("Merge Sort Time: ", b12 - b11)
print("UNH Sort Time: ", b14 - b13)