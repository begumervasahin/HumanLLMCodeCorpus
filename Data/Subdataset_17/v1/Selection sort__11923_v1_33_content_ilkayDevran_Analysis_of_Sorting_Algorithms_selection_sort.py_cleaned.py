def selectionSort(alist):
    for j in range(0, len(alist) - 1):
        smallest = j
        for i in range(j + 1, len(alist)):
            if alist[i] < alist[smallest]:
                smallest = i
        alist[j], alist[smallest] = alist[smallest], alist[j]
if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("Original list:", alist)
    selectionSort(alist)
    print("Sorted list:", alist)