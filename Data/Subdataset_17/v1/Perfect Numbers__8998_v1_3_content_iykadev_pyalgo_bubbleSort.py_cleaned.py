def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
def bubble_sort_main():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubbleSort(alist)
    print("Sorted list:", alist)
if __name__ == "__main__":
    bubble_sort_main()