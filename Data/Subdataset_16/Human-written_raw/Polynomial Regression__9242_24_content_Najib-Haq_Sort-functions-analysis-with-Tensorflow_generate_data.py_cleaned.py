import sorting_algos as s
import random
import time
import csv
import sys
a1 = 10000000
a2 = 100000
b1 = [s.bubble_sort, s.selection_sort, s.insertion_sort, s.merge_sort, s.quick_sort, s.heap_sort]
def fonk1(b8, size):
    for i in range(size):
        b8.append(random.randrange(0,a1))
def fonk2(b8, b5, b2 = b1):
    b3 = []
    for func in b2:
        a3 = 0
        b4 = b8.copy()
        for i in range(a2
            if b5 = = False:
                b4 = b8.copy()
            b6 = time.time()
            func(b4)
            a3 += (time.time() - b6)
        b3.append(a3/(a2
    b3.append(b3.index(min(b3)))
    return b3
def fonk3(start_size, end_size):
    b7 = []
    for size in range(start_size, end_size+1, 100):
        print("Generating for array size "+str(size))
        for b10 in range(3):
            b8 = []
            b9 = [size]
            fonk1(b8, size)
            print("b10 is " + str(b10))
            if b10 = = 0:
                b5 = True
                b9 += [1,0,0]
                b8.sort()
            else:
                b5 = False
                if b10 = = 1:
                    b9 += [0,1,0]
                else:
                    b9 += [0,0,1]
                    b8.sort(b11 = True)
            b9 += fonk2(b8, b5)
            b7.append(b9)
    return b7
def fonk4(filename, b9):
    with open(filename,"a",b12 = '') as file:
        b13 = csv.b13(file,dialect=csv.excel)
        b13.writerows(b9)
if b14 = = "__main__":
    random.seed(time.time())
    sys.setrecursionlimit(1000000)
    b7 = fonk3(1300,4000)
    fonk4("b9.csv", b7)
    sys.setrecursionlimit(1000)