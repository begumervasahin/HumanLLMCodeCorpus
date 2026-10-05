def linear_search(elements, target):
    iterations = 0
    for index, element in enumerate(elements):
        iterations += 1
        if element == target:
            print("Item found at index:", index)
            return index
    print("Item not found")
    return -1
def main():
    try:
        num_elements = int(input("Enter the number of elements: "))
        elements = [input(f"Enter element {i+1}: ") for i in range(num_elements)]
        print("The list is:", elements)
        target = input("Enter the item to find: ")
        linear_search(elements, target)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of elements.")
if __name__ == "__main__":
    main()