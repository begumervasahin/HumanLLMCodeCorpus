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
    b5 = int(input('How many values should be generated? '))
    a1 = 0
    a2 = 100
    b6 = list(range(1, b5 + 1))
    b7 = list(range(b5, 0, -1))
    b8 = [random.randint(a1, a2) for _ in range(b5)]
    b9 = b6.copy()
    b10 = b7.copy()
    b11 = b8.copy()
    b12 = [b6, b7, b8, b9, b10, b11]
    b13 = [[] for _ in range(6)]
    for idx, arr in enumerate(b12):
        for _ in range(5):
            b14 = arr.copy()
            b15 = time.perf_counter()
            if idx < 3:
                fonk1(b14)
            else:
                fonk2(b14)
            b16 = time.perf_counter()
            b13[idx].append(b16 - b15)
    b17 = [sum(times) / 5 for times in b13]
    print(f'{b5}-Val Increasing Selection: {b17[0]:.20f}')
    print(f'{b5}-Val Decreasing Selection: {b17[1]:.20f}')
    print(f'{b5}-Val Random Selection:     {b17[2]:.20f}')
    print(f'{b5}-Val Increasing Insertion: {b17[3]:.20f}')
    print(f'{b5}-Val Decreasing Insertion: {b17[4]:.20f}')
    print(f'{b5}-Val Random Insertion:     {b17[5]:.20f}')