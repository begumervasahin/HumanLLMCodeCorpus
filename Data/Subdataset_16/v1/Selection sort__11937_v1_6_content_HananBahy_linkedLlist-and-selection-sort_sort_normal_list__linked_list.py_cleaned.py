from time import time
from random import randrange
from linkedlistuno import linkedlistuno
from selectionsort import selectionsort
b1 = []
b2 = linkedlistuno()
for i in range(10000):
    b3 = randrange(-1000, 1001)
    b1.insert(0, b3)
    b2.add(b3)
b4 = time()
selectionsort(b1)
b5 = time()
b6 = time()
b2.selectionsort()
b7 = time()
print("Time for normal list:", b5 - b4)
print("Time for linked list:", b7 - b6)