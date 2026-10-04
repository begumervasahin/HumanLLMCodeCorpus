import time
import random
import sys
def fonk1(b18):
    b1 = len(b18)
    for b9 in range(b1):
        for b4 in range(0, b1-b9-1):
            if b18[b4] > b18[b4+1]:
                b18[b4], b18[b4+1] = b18[b4+1], b18[b4]
def fonk2(b18):
    b1 = len(b18)
    for b9 in range(b1-1):
        b2 = b9
        for b4 in range(b9+1, b1):
            if b18[b4] < b18[b2]:
                b2 = b4
        b18[b9], b18[b2] = b18[b2], b18[b9]
def fonk3(b18):
    for b9 in range(1, len(b18)):
        b3 = b18[b9]
        b4 = b9-1
        while b4 >= 0 and b3 < b18[b4]:
            b18[b4+1] = b18[b4]
            b4 -= 1
        b18[b4+1] = b3
def fonk4(b18, b15, b11, b16):
    b5 = b11 - b15 + 1
    b6 = b16 - b11
    b7 = b18[b15:b15+b5]
    b8 = b18[b11+1:b11+1+b6]
    b9 = b4 = 0
    b10 = b15
    while b9 < b5 and b4 < b6:
        if b7[b9] <= b8[b4]:
            b18[b10] = b7[b9]
            b9 += 1
        else:
            b18[b10] = b8[b4]
            b4 += 1
        b10 += 1
    while b9 < b5:
        b18[b10] = b7[b9]
        b9 += 1
        b10 += 1
    while b4 < b6:
        b18[b10] = b8[b4]
        b4 += 1
        b10 += 1
def fonk5(b18):
    def fonk6(b18, b15, b16):
        if b15 < b16:
            b11 = b15 + (b16 - b15)
            fonk6(b18, b15, b11)
            fonk6(b18, b11+1, b16)
            fonk4(b18, b15, b11, b16)
    fonk6(b18, 0, len(b18)-1)
def fonk7(b18, low, high):
    b12 = b18[high]
    b9 = low - 1
    for b4 in range(low, high):
        if b18[b4] <= b12:
            b9 += 1
            b18[b9], b18[b4] = b18[b4], b18[b9]
    b18[b9+1], b18[high] = b18[high], b18[b9+1]
    return b9+1
def fonk8(b18):
    def fonk9(b18, low, high):
        if low < high:
            b13 = fonk7(b18, low, high)
            fonk9(b18, low, b13-1)
            fonk9(b18, b13+1, high)
    fonk9(b18, 0, len(b18)-1)
def fonk10(b18, b1, b9):
    b14 = b9
    b15 = 2*b9 + 1
    b16 = 2*b9 + 2
    if b15 < b1 and b18[b15] > b18[b14]:
        b14 = b15
    if b16 < b1 and b18[b16] > b18[b14]:
        b14 = b16
    if b14 != b9:
        b18[b9], b18[b14] = b18[b14], b18[b9]
        fonk10(b18, b1, b14)
def fonk11(b18):
    b1 = len(b18)
    for b9 in range(b1
        fonk10(b18, b1, b9)
    for b9 in range(b1-1, 0, -1):
        b18[0], b18[b9] = b18[b9], b18[0]
        fonk10(b18, b9, 0)
if b17 = = "__main__":
    sys.setrecursionlimit(10000000)
    a1 = 0
    b18 = [random.randrange(0, 1000000000) for _ in range(4000)]
    b18.sort()
    a2 = 100000
    for _ in range(a2):
        b19 = b18.copy()
        b20 = time.time()
        fonk8(b19)
        a1 += time.time() - b20
    print(f"Time taken is {a1 / a2:.5f} seconds")
    print(b19)
    sys.setrecursionlimit(1000)