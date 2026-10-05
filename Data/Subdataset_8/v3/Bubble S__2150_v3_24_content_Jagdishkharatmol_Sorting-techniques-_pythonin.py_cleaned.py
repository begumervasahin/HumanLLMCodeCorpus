import time
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
    for fill_slot in range(len(lst) - 1, 0, -1):
        position_of_max = 0
        for location in range(1, fill_slot + 1):
            if lst[location] > lst[position_of_max]:
                position_of_max = location
        lst[fill_slot], lst[position_of_max] = lst[position_of_max], lst[fill_slot]
def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid integer.")
def main():
    while True:
        print("_" * 80)
        print("Sort techniques on dataset".center(80))
        print("_" * 80)
        print("Enter:")
        print("1 for Bubble Sort")
        print("2 for Insertion Sort")
        print("3 for Merge Sort")
        print("4 for Selection Sort")
        choice = get_integer_input("\nEnter your choice: ")
        if choice == 1:
            lst = [get_integer_input("Enter a number: ") for _ in range(get_integer_input("How many numbers do you want to enter: "))]
            start_time = time.time()
            bubble_sort(lst)
            print(f"The list after Bubble Sort: {lst}")
            print(f"Time taken: {time.time() - start_time} seconds")
        elif choice == 2:
            lst = [get_integer_input("Enter a number: ") for _ in range(get_integer_input("How many numbers do you want to enter: "))]
            start_time = time.time()
            insertion_sort(lst)
            print(f"The list after Insertion Sort: {lst}")
            print(f"Time taken: {time.time() - start_time} seconds")
        elif choice == 3:
            alist = [get_integer_input("Enter a number: ") for _ in range(get_integer_input("How many numbers do you want to enter: "))]
            start_time = time.time()
            merge_sort(alist)
            print(f"The list after Merge Sort: {alist}")
            print(f"Time taken: {time.time() - start_time} seconds")
        elif choice == 4:
            lst = [get_integer_input("Enter a number: ") for _ in range(get_integer_input("How many numbers do you want to enter: "))]
            start_time = time.time()
            selection_sort(lst)
            print(f"The list after Selection Sort: {lst}")
            print(f"Time taken: {time.time() - start_time} seconds")
        else:
            print("Invalid choice!")
        continue_input = get_integer_input("\nEnter 1 to continue and 0 to exit: ")
        if continue_input == 0:
            break
if __name__ == "__main__":
    main()