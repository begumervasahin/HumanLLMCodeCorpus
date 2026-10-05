from random import randint, sample
import sys
import time
def fonk1(arr, start, end):
    b1 = arr[end]
    b2 = start - 1
    for j in range(start, end):
        if arr[j] <= b1:
            b2 += 1
            arr[b2], arr[j] = arr[j], arr[b2]
    arr[b2 + 1], arr[end] = arr[end], arr[b2 + 1]
    return b2 + 1
def fonk2(arr, start, end):
    b3 = randint(start, end)
    arr[end], arr[b3] = arr[b3], arr[end]
    return fonk1(arr, start, end)
def fonk3(arr, start, end):
    if end > start:
        b4 = fonk1(arr, start, end)
        fonk3(arr, start, b4 - 1)
        fonk3(arr, b4 + 1, end)
if b5 = = '__main__':
    if len(sys.argv) != 2:
        sys.exit('Usage: %s <number of elements>' % sys.argv[0])
    b6 = int(sys.argv[1])
    if b6 <= 0:
        sys.exit('Usage: %s <number of elements>' % sys.argv[0])
    b7 = sample(range(1000000), b6)
    b8 = time.process_time()
    for _ in range(1000):
        b9 = b7.copy()
        fonk3(b9, 0, b6 - 1)
        for b2 in range(b6 - 1):
            assert b9[b2] <= b9[b2 + 1]
    b10 = time.process_time()
    print("Execution time:", b10 - b8)