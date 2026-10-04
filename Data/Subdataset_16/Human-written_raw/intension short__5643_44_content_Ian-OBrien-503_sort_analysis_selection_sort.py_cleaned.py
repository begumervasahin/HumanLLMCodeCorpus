import random
import numpy as np
import time
a1 = 40
b1 = np.random.randint(0,99999,a1)
b1 = np.random.randint(0,99999,a1)
b2 = time.clock()
for i in range(a1):
    b3 = i
    for j in range (i+1, a1):
        if (b1[b3] > b1[j]):
            b3 = j
    b1[i], b1[b3] = b1[b3], b1[i]
b4 = time.clock()
print(b1)
b5 = b4 - b2
print("\n\n", b5, "seconds of execution for selection sort RNDM ORDER && ARR_SIZE:", a1)
b1 = np.random.randint(0,99999,a1)
for i in range(a1):
    b3 = i
    for j in range (i+1, a1):
        if (b1[b3] > b1[j]):
            b3 = j
    b1[i], b1[b3] = b1[b3], b1[i]
b2 = time.clock()
for i in range(a1):
    b3 = i
    for j in range (i+1, a1):
        if (b1[b3] > b1[j]):
            b3 = j
    b1[i], b1[b3] = b1[b3], b1[i]
b4 = time.clock()
print(b1)
b5 = b4 - b2
print("\n\n", b5, "seconds of execution for selection sort ASCENDING ORDER && ARR_SIZE:", a1)
b1 = np.random.randint(0,99999,a1)
for i in range(a1):
    b3 = i
    for j in range (i+1, a1):
        if (b1[b3] < b1[j]):
            b3 = j
    b1[i], b1[b3] = b1[b3], b1[i]
b2 = time.clock()
for i in range(a1):
    b3 = i
    for j in range (i+1, a1):
        if (b1[b3] > b1[j]):
            b3 = j
    b1[i], b1[b3] = b1[b3], b1[i]
b4 = time.clock()
print(b1)
b5 = b4 - b2
print("\n\n", b5, "seconds of execution for selection sort REVERSE ORDER && ARR_SIZE:", a1)