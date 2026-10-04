import time
count = 0
def mergeSort(arr):
    global count
    if len(arr) > 1:
        mid = len(arr)
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            count += 1
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            count += 1
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            count += 1
            arr[k] = R[j]
            j += 1
            k += 1
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
if __name__ == '__main__':
    start = time.time()
    with open("case") as fp:
        arr = fp.read().split()
    list2 = [int(num) for num in arr]
    mergeSort(list2)
    print("Sorted array is: ", end="\n")
    printList(list2)
    print("Number of comparisons:", count)
    end = time.time()
    print("Time taken:", end - start)