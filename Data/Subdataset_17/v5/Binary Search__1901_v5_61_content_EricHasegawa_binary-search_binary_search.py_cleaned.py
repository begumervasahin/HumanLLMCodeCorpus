def binary_search():
    while True:
        target = get_target_number()
        number_list = read_number_list("numberlist.txt")
        sorted_list = sorted(number_list)
        if perform_binary_search(sorted_list, target):
            print("Target found!")
        else:
            print("Target not found.")
        if not ask_to_continue():
            print("Exiting. Goodbye!")
            break
def get_target_number():
    while True:
        try:
            return int(input("Enter an integer: "))
        except ValueError:
            print("You did not enter an integer. Please try again.")
def read_number_list(filename):
    with open(filename) as file:
        contents = file.read()
        return list(map(int, contents.split(", ")))
def perform_binary_search(sorted_list, target):
    low, high = 0, len(sorted_list) - 1
    while low <= high:
        middle = (low + high)
        if target == sorted_list[middle]:
            return True
        elif target > sorted_list[middle]:
            low = middle + 1
        else:
            high = middle - 1
    return False
def ask_to_continue():
    while True:
        yn = input("Would you like to test another number? (y/n): ").lower()
        if yn in ['y', 'n']:
            return yn == 'y'
        print("Invalid input. Please enter 'y' or 'n'.")
binary_search()