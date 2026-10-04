import random
import timeit
def printArray(arr):
    print(' '.join(str(i) for i in arr))
def insertionsort(arr):
    N = len(arr)
    for i in range(1, N):
        j = i - 1
        temp = arr[i]
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist)
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i+1
            else:
                alist[k] = righthalf[j]
                j = j+1
            k = k+1
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i+1
            k = k+1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j+1
            k = k+1
def UNHSort(blist):
    M = len(blist)
    for i in range(M-1, 0, -1):
        for j in range(1, i):
            if blist[j] > blist[j+1]:
                temp = blist[j]
                blist[j] = blist[j+1]
                blist[j+1] = temp
insertion_randoms = merge_randoms = UNH_randoms = random.sample(range(10000), 10000)
print("Initial Array :",)
printArray(insertion_randoms)
insertion_start = timeit.default_timer()
insertionsort(insertion_randoms)
insertion_stop = timeit.default_timer()
merge_start = timeit.default_timer()
mergeSort(merge_randoms)
merge_stop = timeit.default_timer()
UNH_start = timeit.default_timer()
UNHSort(UNH_randoms)
UNH_stop = timeit.default_timer()
print("Insertion Sort Time: ", insertion_stop - insertion_start)
print("Merge Sort Time: ", merge_stop - merge_start)
print("UNH Sort Time: ", UNH_stop - UNH_start)