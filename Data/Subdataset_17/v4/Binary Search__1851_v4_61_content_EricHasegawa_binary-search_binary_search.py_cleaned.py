def binary_search():
    while True:
        try:
            target = int(input("Enter an integer: "))
            break
        except ValueError:
            print("You did not enter an integer. Please try again.")
    with open('numberlist.txt') as numberlist:
        split_list = numberlist.read().split(", ")
    results = list(map(int, split_list))
    sorted_results = sorted(results)
    low = 0
    high = len(sorted_results) - 1
    while high > low:
        middle = (high + low)
        if target == sorted_results[middle]:
            print("Target found!")
            break
        elif middle == low:
            print("Target not found.")
            break
        elif target > sorted_results[middle]:
            low = middle
        elif target < sorted_results[middle]:
            high = middle
    while True:
        yn = input("Would you like to test another number? (y/n): ").lower()
        if yn == 'y':
            binary_search()
            break
        elif yn == 'n':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
binary_search()