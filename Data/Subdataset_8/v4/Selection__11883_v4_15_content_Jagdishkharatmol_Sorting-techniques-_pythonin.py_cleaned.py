import time
line_separator = '_' * 80
title = "Sort techniques on dataset"
print(line_separator)
print(title.center(80))
print(line_separator + "\n\n")
while True:
    print("Enter \n 1 for bubble sort \n 2 for insertion sort \n 3 for merge sort \n 4 for selection sort")
    choice = int(input("\nEnter your choice: "))
    if choice == 1:
        start_time = time.time()
        def bubble_sort(lst):
            for j in range(len(lst) - 1, 0, -1):
                for i in range(j):
                    if lst[i] > lst[i + 1]:
                        temp = lst[i]
                        lst[i] = lst[i + 1]
                        lst[i + 1] = temp
        lst = []
        num_count = int(input("\nHow many numbers do you want to enter? "))
        for i in range(num_count):
            num = int(input("Enter the number: "))
            lst.append(num)
        bubble_sort(lst)
        print("\nThe list after bubble sorting is:", lst)
        end_time = time.time()
        print("The time taken by sorting process:", end_time - start_time)
    elif choice == 2:
        start_time = time.time()
        def insertion_sort(lst):
            for i in range(1, len(lst)):
                current_value = lst[i]
                position = i
                while position > 0 and lst[position - 1] > current_value:
                    lst[position] = lst[position - 1]
                    position -= 1
                lst[position] = current_value
        lst = []
        num_count = int(input("\nHow many numbers do you want to enter? "))
        for i in range(num_count):
            num = int(input("Enter the number: "))
            lst.append(num)
        insertion_sort(lst)
        print("\nThe list after insertion sorting is:", lst)
        end_time = time.time()
        print("The time taken by sorting process:", end_time - start_time)
    elif choice == 3:
        start_time = time.time()
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
        alist = []
        num_count = int(input("\nHow many numbers do you want to enter? "))
        for i in range(num_count):
            num = int(input("Enter the number: "))
            alist.append(num)
        merge_sort(alist)
        print("\nThe list after merge sorting is:", alist)
        end_time = time.time()
        print("The time taken by sorting process:", end_time - start_time)
    elif choice == 4:
        start_time = time.time()
        def selection_sort(lst):
            for fillslot in range(len(lst) - 1, 0, -1):
                position_of_max = 0
                for location in range(1, fillslot + 1):
                    if lst[location] > lst[position_of_max]:
                        position_of_max = location
                temp = lst[fillslot]
                lst[fillslot] = lst[position_of_max]
                lst[position_of_max] = temp
        lst = []
        num_count = int(input("\nHow many numbers do you want to enter? "))
        for i in range(num_count):
            num = int(input("Enter the number: "))
            lst.append(num)
        selection_sort(lst)
        print("\nThe list after selection sorting is:", lst)
        end_time = time.time()
        print("The time taken by sorting process:", end_time - start_time)
    continue_option = int(input("\nEnter 1 to continue and 0 to exit: "))
    print("\n\n")
    if continue_option == 0:
        break