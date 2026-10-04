import time
from random import randint
def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
def main():
    print("Quick Sort")
    randlist = [[] for _ in range(10)]
    startTimeList = [0] * 10
    endTimeList = [0] * 10
    inputSize = 100000
    i = 0
    while inputSize <= 10000000:
        randlist[i] = [randint(1, inputSize) for _ in range(inputSize)]
        print("Clock {} is ticking....".format(i + 1))
        startTimeList[i] = time.time()
        quickSort(randlist[i], 0, len(randlist[i]) - 1)
        endTimeList[i] = time.time()
        print("Time taken for InputSize({}) is {} seconds ".format(inputSize, endTimeList[i] - startTimeList[i]))
        inputSize += 1100000
        i += 1
if __name__ == "__main__":
    main()