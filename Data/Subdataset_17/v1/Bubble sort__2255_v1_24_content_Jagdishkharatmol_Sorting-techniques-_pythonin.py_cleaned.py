import time
def bubble_sort(lst):
    for j in range(len(lst) - 1, 0, -1):
        for i in range(j):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
def insertion_sort(lst):
    for i in range(1, len(lst)):
        currentvalue = lst[i]
        position = i
        while position > 0 and lst[position - 1] > currentvalue:
            lst[position] = lst[position - 1]
            position = position - 1
        lst[position] = currentvalue
def merge_sort(alist):
    if len(alist) > 1:
        mid = len(alist)
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        merge_sort(lefthalf)
        merge_sort(righthalf)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
def selection_sort(lst):
    for fillslot in range(len(lst) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if lst[location] > lst[positionOfMax]:
                positionOfMax = location
        lst[fillslot], lst[positionOfMax] = lst[positionOfMax], lst[fillslot]
def main():
    separator = '_' * 80
    print(f"{separator}\n")
    str = "Sort techniques on dataset"
    print(str.center(80))
    print(f"\n{separator}\n\n")
    while True:
        print("Enter \n 1 for Bubble Sort \n 2 for Insertion Sort \n 3 for Merge Sort \n 4 for Selection Sort")
        cho = int(input("\nEnter your choice: "))
        lst = []
        n = int(input("\nHow many numbers do you want to enter: "))
        for i in range(n):
            num = int(input("Enter the number: "))
            lst.append(num)
        if cho == 1:
            start = time.time()
            bubble_sort(lst)
            end = time.time()
            print("\nThe list after Bubble Sorting is: {}".format(lst))
            print("The time taken by the sorting process: {:.6f} seconds".format(end - start))
        elif cho == 2:
            start = time.time()
            insertion_sort(lst)
            end = time.time()
            print("\nThe list after Insertion Sorting is: {}".format(lst))
            print("The time taken by the sorting process: {:.6f} seconds".format(end - start))
        elif cho == 3:
            start = time.time()
            merge_sort(lst)
            end = time.time()
            print("\nThe list after Merge Sorting is: {}".format(lst))
            print("The time taken by the sorting process: {:.6f} seconds".format(end - start))
        elif cho == 4:
            start = time.time()
            selection_sort(lst)
            end = time.time()
            print("\nThe list after Selection Sorting is: {}".format(lst))
            print("The time taken by the sorting process: {:.6f} seconds".format(end - start))
        else:
            print("Invalid choice! Please enter a valid option.")
        n = int(input("\nEnter 1 to continue and 0 to exit: "))
        if n == 0:
            break
if __name__ == "__main__":
    main()