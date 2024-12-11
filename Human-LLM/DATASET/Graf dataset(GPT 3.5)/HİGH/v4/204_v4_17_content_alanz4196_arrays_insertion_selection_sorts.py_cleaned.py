import time
import random
def fonk1(arr):
    for k in range(len(arr) - 1):
        b1 = k
        for n in range(k + 1, len(arr)):
            if arr[n] < arr[b1]:
                b1 = n
        arr[k], arr[b1] = arr[b1], arr[k]
    return arr
def fonk2(arr):
    for k in range(1, len(arr)):
        b2 = arr[k]
        b3 = k
        while b3 > 0 and arr[b3 - 1] > b2:
            arr[b3] = arr[b3 - 1]
            b3 -= 1
        arr[b3] = b2
    return arr
if b4 = = '__main__':
    a1 = 0
    a2 = 100
    b5 = [0] * 6
    b6 = int(input('How many values should be generated? '))
    b7 = list(range(1, b6 + 1))
    b8 = b7.copy()
    b9 = list(range(b6, 0, -1))
    b10 = b9.copy()
    b11 = [random.randint(a1, a2) for _ in range(b6)]
    b12 = b11.copy()
    b13 = [b7, b9, b11,
                    b8, b10, b12]
    b14 = []
    for arr in b13:
        b15 = []
        for _ in range(5):
            b16 = arr[:]
            b17 = time.process_time()
            fonk1(b16) if arr in [b7, b9, b11] else fonk2(b16)
            b18 = time.process_time()
            b15.append(b18 - b17)
        b14.append(b15)
    for i in range(6):
        b5[i] = sum(b14[i]) / 5
    print(f"{b6}-Val Increasing Selection: {b5[0]:.20f}")
    print(f"{b6}-Val Decreasing Selection: {b5[1]:.20f}")
    print(f"{b6}-Val Random Selection:     {b5[2]:.20f}")
    print(f"{b6}-Val Increasing Insertion: {b5[3]:.20f}")
    print(f"{b6}-Val Decreasing Insertion: {b5[4]:.20f}")
    print(f"{b6}-Val Random Insertion:     {b5[5]:.20f}")