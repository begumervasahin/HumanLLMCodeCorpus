def binary_search():
    while True:
        try:
            target = int(input("Enter an integer to search: "))
            break
        except ValueError:
            print("Error: Please enter an integer.")
    with open('numberlist.txt') as file:
        numbers = file.read().split(", ")
    numbers = list(map(int, numbers))
    sorted_numbers = sorted(numbers)
    high = len(sorted_numbers) - 1
    low = 0
    while high >= low:
        middle = (high + low)
        if target == sorted_numbers[middle]:
            print("Target found.")
            return
        elif middle == low:
            print("Target not found.")
            return
        elif target > sorted_numbers[middle]:
            low = middle + 1
        else:
            high = middle - 1
    print("Target not found.")
    while True:
        yn = input("Would you like to test another number? (y/n): ")
        if yn == 'y':
            binary_search()
            break
        elif yn == 'n':
            print("Program terminated.")
            break
        else:
            print("Error: Please enter 'y' or 'n'.")
if __name__ == "__main__":
    binary_search()