def binary_search():
    while True:
        try:
            target = int(input("Enter an integer: "))
            break
        except ValueError:
            print("You did not enter an integer. Please try again.")
    with open('numberlist.txt', 'r') as file:
        number_list = file.read().split(", ")
    results = list(map(int, number_list))
    sorted_results = sorted(results)
    low = 0
    high = len(sorted_results) - 1
    while low <= high:
        middle = (low + high)
        if target == sorted_results[middle]:
            print("Target found!")
            break
        elif target > sorted_results[middle]:
            low = middle + 1
        else:
            high = middle - 1
    else:
        print("Target not found.")
    while True:
        yn = input("Would you like to test another number? (y/n): ").lower()
        if yn == 'y':
            binary_search()
            break
        elif yn == 'n':
            print("Exiting program. Goodbye!")
            break
        else:
            print("You did not enter 'y' or 'n'. Please try again.")
binary_search()