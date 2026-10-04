import time
import random
from linkedlistuno import linkedlistuno
from selectionsort import selectionsort
def fonk1():
    b1 = []
    b2 = linkedlistuno()
    for _ in range(10000):
        b3 = random.randrange(-1000, 1001)
        b1.insert(0, b3)
        b2.add(b3)
    b4 = time.time()
    selectionsort(b1)
    b5 = time.time()
    b6 = time.time()
    b2.selectionsort()
    b7 = time.time()
    print("Time for normal list:", b5 - b4)
    print("Time for linked list:", b7 - b6)
if b8 = = "__main__":
    fonk1()