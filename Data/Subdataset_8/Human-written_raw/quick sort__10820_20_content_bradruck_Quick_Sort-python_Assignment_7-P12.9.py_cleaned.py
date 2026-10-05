from random import randint
from time import time
def quickSort2(values, start, to) :
    if start >= to :
        return
    p = partition(values, start, to)
    quickSort2(values, start, p)
    quickSort2(values, p + 1, to)
def partition(values, start, to) :
    pivot = values[start]
    i = start - 1
    j = to + 1
    while i < j :
        i += 1
        while values[i] < pivot :
            i += 1
        j -= 1
        while values[j] > pivot :
            j -= 1
        if i < j :
            swap(values, i, j)
    return j
def quickSort3(values, start, to) :
    if start >= to : return
    pivot = values[start]
    e = i = start
    g = to
    while i <= to :
        if values[i] < pivot :
            swap(values, i, e)
            e += 1
            i += 1
        elif values[i] == pivot :
            i += 1
        else :
            to -= 1
            swap(values, i, g)
    quickSort3(values, start, e)
    quickSort3(values, g, to)
def swap(values, i, j) :
    temp = values[i]
    values[i] = values[j]
    values[j] = temp
def main() :
    print()
    n = int(input("Enter the list size: "))
    print()
    print("Enter the maximum element number from which to build the list (the minimum is set at 1)")
    x = int(input("(Hint, the lower the number, the higher number of duplicate elements with which to prove the algorithm's speed): "))
    values_2way = []
    for i in range(n) :
        values_2way.append(randint(1, x))
    values_3way = values_2way
    startTime2 = time()
    quickSort2(values_2way, 0, n - 1)
    endTime2 = time()
    print()
    print("The number of seconds for the 2-way sort was:  %.8f" % (endTime2 - startTime2))
    startTime3 = time()
    quickSort3(values_3way, 0, n - 1)
    endTime3 = time()
    print()
    print("The number of seconds for the 3-way sort was:  %.8f" % (endTime3 - startTime3))
    print()
main()