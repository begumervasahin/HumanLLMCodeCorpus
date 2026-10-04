import time
from random import randrange
from linkedlistuno import LinkedListUno
from selectionsort import selection_sort
def fonk1(a1, b6):
    b1 = []
    b2 = LinkedListUno()
    for _ in range(a1):
        b3 = randrange(*b6)
        b1.append(b3)
        b2.add(b3)
    return b1, b2
def fonk2(sort_function, data_structure):
    b4 = time.time()
    sort_function(data_structure)
    b5 = time.time()
    return b5 - b4
def fonk3():
    a1 = 10000
    b6 = (-1000, 1001)
    b1, b2 = fonk1(a1, b6)
    b7 = fonk2(selection_sort, b1.copy())
    b8 = fonk2(b2.selection_sort, b2)
    print("Time for normal list:", b7)
    print("Time for linked list:", b8)
if b9 = = "__main__":
    fonk3()