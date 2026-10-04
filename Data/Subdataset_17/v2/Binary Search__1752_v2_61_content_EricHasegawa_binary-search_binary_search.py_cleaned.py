def binary_search():
    while True:
        try:
            target = int(input("Enter an integer to search: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    with open('numberlist.txt', 'r') as file:
        number_list = file.read().split(", ")
    numbers = sorted(map(int, number_list))
    low, high = 0, len(numbers) - 1
    while low <= high:
        mid = (low + high)
        if numbers[mid] == target:
            print(f"Target {target} found in the list!")
            break
        elif numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    else:
        print(f"Target {target} not found in the list.")
    while True:
        retry = input("Would you like to search for another number? (y/n): ").strip().lower()
        if retry == 'y':
            binary_search()
            break
        elif retry == 'n':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")
binary_search()