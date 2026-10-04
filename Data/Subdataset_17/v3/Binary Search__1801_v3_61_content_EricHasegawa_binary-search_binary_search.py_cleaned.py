def get_target_input():
    while True:
        try:
            return int(input("Enter an integer to search: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
def read_and_process_number_list(filename='numberlist.txt'):
    with open(filename, 'r') as file:
        number_list = file.read().split(", ")
    return sorted(map(int, number_list))
def perform_binary_search(numbers, target):
    low, high = 0, len(numbers) - 1
    while low <= high:
        mid = (low + high)
        if numbers[mid] == target:
            return True
        elif numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False
def ask_retry():
    while True:
        retry = input("Would you like to search for another number? (y/n): ").strip().lower()
        if retry in ('y', 'n'):
            return retry == 'y'
        print("Invalid input. Please enter 'y' for yes or 'n' for no.")
def binary_search():
    while True:
        target = get_target_input()
        numbers = read_and_process_number_list()
        if perform_binary_search(numbers, target):
            print(f"Target {target} found in the list!")
        else:
            print(f"Target {target} not found in the list.")
        if not ask_retry():
            print("Exiting program. Goodbye!")
            break
binary_search()