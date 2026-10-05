import time
LINE_SEPARATOR = '_' * 80
TITLE = "Sort Techniques on Dataset"
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
def display_menu():
    print("Enter:")
    print("1 for Bubble Sort")
    print("2 for Insertion Sort")
    print("3 for Merge Sort")
    print("4 for Selection Sort")
def main():
    print(LINE_SEPARATOR)
    print(TITLE.center(80))
    print(LINE_SEPARATOR + "\n\n")
    while True:
        display_menu()
        choice = int(input("\nEnter your choice: "))
        if choice not in [1, 2, 3, 4]:
            print("Invalid choice. Please select again.")
            continue
        lst = []
        num_count = int(input("\nHow many numbers do you want to enter? "))
        for i in range(num_count):
            num = int(input("Enter the number: "))
            lst.append(num)
        start_time = time.time()
        if choice == 1:
            bubble_sort(lst)
            print("\nThe list after Bubble Sort is:", lst)
        elif choice == 2:
            insertion_sort(lst)
            print("\nThe list after Insertion Sort is:", lst)
        elif choice == 3:
            merge_sort(lst)
            print("\nThe list after Merge Sort is:", lst)
        elif choice == 4:
            selection_sort(lst)
            print("\nThe list after Selection Sort is:", lst)
        end_time = time.time()
        print("The time taken by sorting process:", end_time - start_time)
        continue_option = input("\nEnter 1 to continue and 0 to exit: ")
        if continue_option != '1':
            break
        print("\n\n")
if __name__ == "__main__":
    main()