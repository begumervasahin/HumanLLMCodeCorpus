import time
def print_horizontal_line():
    print('_' * 80)
def print_centered_string(string):
    print_horizontal_line()
    print(string.center(80))
    print_horizontal_line()
def bubble_sort(lst):
    for j in range(len(lst) - 1, 0, -1):
        for i in range(j):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
def insertion_sort(lst):
    for i in range(1, len(lst)):
        current_value = lst[i]
        position = i
        while position > 0 and lst[position - 1] > current_value:
            lst[position] = lst[position - 1]
            position -= 1
        lst[position] = current_value
def merge_sort(alist):
    if len(alist) > 1:
        mid = len(alist)
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        merge_sort(lefthalf)
        merge_sort(righthalf)
        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1
def selection_sort(lst):
    for fillslot in range(len(lst) - 1, 0, -1):
        position_of_max = 0
        for location in range(1, fillslot + 1):
            if lst[location] > lst[position_of_max]:
                position_of_max = location
        lst[fillslot], lst[position_of_max] = lst[position_of_max], lst[fillslot]
print_horizontal_line()
print()
print_centered_string("Sorting Techniques on Dataset")
while True:
    print("Enter:")
    print("1 for Bubble Sort")
    print("2 for Insertion Sort")
    print("3 for Merge Sort")
    print("4 for Selection Sort")
    choice = int(input("\nEnter your choice: "))
    start_time = time.time()
    lst = []
    n = int(input("\nHow many numbers do you want to enter: "))
    for i in range(n):
        num = int(input("Enter the number: "))
        lst.append(num)
    if choice == 1:
        bubble_sort(lst)
        print("\nThe list after Bubble Sorting is:", lst)
    elif choice == 2:
        insertion_sort(lst)
        print("\nThe list after Insertion Sorting is:", lst)
    elif choice == 3:
        merge_sort(lst)
        print("\nThe list after Merge Sorting is:", lst)
    elif choice == 4:
        selection_sort(lst)
        print("\nThe list after Selection Sorting is:", lst)
    end_time = time.time()
    print("Time taken by the sorting process:", end_time - start_time)
    continue_choice = int(input("\nEnter 1 to continue and 0 to exit: "))
    print("\n\n")
    if continue_choice == 0:
        break