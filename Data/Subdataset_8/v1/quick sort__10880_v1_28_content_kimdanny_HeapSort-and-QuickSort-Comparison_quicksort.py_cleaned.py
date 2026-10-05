import time
from random import randint
def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
print("Quick Sort")
randlist = [[] for _ in range(10)]
startTimeList = [[] for _ in range(10)]
endTimeList = [[] for _ in range(10)]
inputSize = 100000
i = 0
while inputSize <= 10000000:
    for _ in range(inputSize):
        num = randint(1, inputSize)
        randlist[i].append(num)
    print("Clock {} is ticking....".format(i + 1))
    startTimeList[i] = time.time()
    quickSort(randlist[i], 0, len(randlist[i]) - 1)
    endTimeList[i] = time.time()
    print("Time taken for InputSize({}) is {} second ".format(inputSize, endTimeList[i] - startTimeList[i]))
    inputSize += 1100000
    i += 1