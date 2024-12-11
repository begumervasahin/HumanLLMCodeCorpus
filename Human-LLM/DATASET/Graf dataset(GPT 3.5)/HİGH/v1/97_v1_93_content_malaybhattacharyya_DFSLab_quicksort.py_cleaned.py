from random import randint, sample
import sys
import time
def fonk1(b7, start, end):
    b1 = b7[end]
    b2 = start - 1
    for j in range(start, end):
        if b7[j] <= b1:
            b2 += 1
            b7[b2], b7[j] = b7[j], b7[b2]
    b7[b2 + 1], b7[end] = b7[end], b7[b2 + 1]
    return b2 + 1
def fonk2(b7, start, end):
    b2 = randint(start, end)
    b7[end], b7[b2] = b7[b2], b7[end]
    return fonk1(b7, start, end)
def fonk3(b7, start, end):
    if end > start:
        b1 = fonk1(b7, start, end)
        fonk3(b7, start, b1 - 1)
        fonk3(b7, b1 + 1, end)
if b3 = = '__main__':
    if len(sys.argv) != 2:
        sys.exit('Usage: %s <number of elements>' % sys.argv[0])
    b4 = int(sys.argv[1])
    if b4 <= 0:
        sys.exit('Usage: %s <number of elements>' % sys.argv[0])
    b5 = sample(range(1000000), b4)
    b6 = time.process_time()
    for _ in range(1000):
        b7 = b5.copy()
        fonk3(b7, 0, b4 - 1)
        for b2 in range(b4 - 1):
            assert b7[b2] <= b7[b2 + 1]
    b8 = time.process_time()
    print("Execution time:", b8 - b6)