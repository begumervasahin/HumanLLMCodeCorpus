import time
decorative_line = '_' * 80
print(f"{decorative_line} \n")
title = "Sort Techniques on Dataset"
print(title.center(80))
print(f"\n{decorative_line}\n\n")
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
def merge_sort(lst):
    def merge(left, right):
        merged = []
        while left and right:
            merged.append(left.pop(0) if left[0] < right[0] else right.pop(0))
        return merged + left + right
    if len(lst) <= 1:
        return lst
    mid = len(lst)
    left_half = merge_sort(lst[:mid])
    right_half = merge_sort(lst[mid:])
    return merge(left_half, right_half)
def selection_sort(lst):
    for fill_slot in range(len(lst) - 1, 0, -1):
        position_of_max = 0
        for location in range(1, fill_slot + 1):
            if lst[location] > lst[position_of_max]:
                position_of_max = location
        lst[fill_slot], lst[position_of_max] = lst[position_of_max], lst[fill_slot]
while True:
    print("Enter:")
    print("1 for Bubble Sort")
    print("2 for Insertion Sort")
    print("3 for Merge Sort")
    print("4 for Selection Sort")
    choice = int(input("\nEnter your choice: "))
    if choice == 1:
        start_time = time.time()
        lst = [int(input("Enter the number: ")) for _ in range(int(input("\nHow many numbers do you want to enter? ")))]
        bubble_sort(lst)
        print("\nThe list after Bubble Sort is:", lst)
        print("The time taken by sorting process:", time.time() - start_time)
    elif choice == 2:
        start_time = time.time()
        lst = [int(input("Enter the number: ")) for _ in range(int(input("\nHow many numbers do you want to enter? ")))]
        insertion_sort(lst)
        print("\nThe list after Insertion Sort is:", lst)
        print("The time taken by sorting process:", time.time() - start_time)
    elif choice == 3:
        start_time = time.time()
        lst = [int(input("Enter the number: ")) for _ in range(int(input("\nHow many numbers do you want to enter? ")))]
        lst = merge_sort(lst)
        print("\nThe list after Merge Sort is:", lst)
        print("The time taken by sorting process:", time.time() - start_time)
    elif choice == 4:
        start_time = time.time()
        lst = [int(input("Enter the number: ")) for _ in range(int(input("\nHow many numbers do you want to enter? ")))]
        selection_sort(lst)
        print("\nThe list after Selection Sort is:", lst)
        print("The time taken by sorting process:", time.time() - start_time)
    option = int(input("\nEnter 1 to continue and 0 to exit: "))
    print("\n\n")
    if option == 0:
        break