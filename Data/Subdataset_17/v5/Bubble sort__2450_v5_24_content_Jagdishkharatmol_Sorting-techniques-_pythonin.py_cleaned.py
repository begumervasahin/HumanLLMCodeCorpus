import time
def bubble_sort(lst):
    n = len(lst)
    for j in range(n - 1, 0, -1):
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
    if len(lst) > 1:
        mid = len(lst)
        left_half = lst[:mid]
        right_half = lst[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                lst[k] = left_half[i]
                i += 1
            else:
                lst[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            lst[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            lst[k] = right_half[j]
            j += 1
            k += 1
def selection_sort(lst):
    for fillslot in range(len(lst) - 1, 0, -1):
        position_of_max = 0
        for location in range(1, fillslot + 1):
            if lst[location] > lst[position_of_max]:
                position_of_max = location
        lst[fillslot], lst[position_of_max] = lst[position_of_max], lst[fillslot]
def get_sorting_choice():
    print("Enter the number corresponding to the sorting algorithm:")
    print(" 1. Bubble Sort")
    print(" 2. Insertion Sort")
    print(" 3. Merge Sort")
    print(" 4. Selection Sort")
    while True:
        try:
            choice = int(input("\nEnter your choice: "))
            if choice in {1, 2, 3, 4}:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def get_numbers():
    while True:
        try:
            n = int(input("\nHow many numbers do you want to enter? "))
            if n > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    lst = []
    for _ in range(n):
        while True:
            try:
                num = int(input("Enter a number: "))
                lst.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    return lst
def main():
    separator = '_' * 80
    print(f"{separator}\n")
    print("Sort techniques on dataset".center(80))
    print(f"\n{separator}\n\n")
    while True:
        choice = get_sorting_choice()
        numbers = get_numbers()
        start_time = time.time()
        if choice == 1:
            bubble_sort(numbers)
            print("\nThe list after bubble sorting is {}".format(numbers))
        elif choice == 2:
            insertion_sort(numbers)
            print("\nThe list after insertion sorting is {}".format(numbers))
        elif choice == 3:
            merge_sort(numbers)
            print("\nThe list after merge sorting is {}".format(numbers))
        elif choice == 4:
            selection_sort(numbers)
            print("\nThe list after selection sorting is {}".format(numbers))
        end_time = time.time()
        print("The time taken by the sorting process: {:.5f} seconds".format(end_time - start_time))
        continue_choice = input("Enter 'y' to continue or any other key to exit: ").strip().lower()
        if continue_choice != 'y':
            break
if __name__ == "__main__":
    main()