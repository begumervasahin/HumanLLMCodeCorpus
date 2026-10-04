from time import time
from random import randrange
from linkedlistuno import linkedlistuno
from selectionsort import selectionsort
mylist = []
mylinkedlist = linkedlistuno()
for i in range(10000):
    j = randrange(-1000, 1001)
    mylist.insert(0, j)
    mylinkedlist.add(j)
start1 = time()
selectionsort(mylist)
end1 = time()
start2 = time()
mylinkedlist.selectionsort()
end2 = time()
print("Time for normal list:", end1 - start1)
print("Time for linked list:", end2 - start2)