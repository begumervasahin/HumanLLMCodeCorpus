def linear_search(arr, val):
    found = False
    for i, element in enumerate(arr):
        if element == val:
            print(f"The value {val} is found at index {i}")
            found = True
    if not found:
        print(f"The value {val} is not found in the array")
def main():
    array_size = int(input("Enter the size of the array: "))
    arr = []
    for i in range(array_size):
        element = int(input(f"Enter element {i + 1}: "))
        arr.append(element)
    print("Array:", arr)
    search_value = int(input("Enter the value you want to search for: "))
    linear_search(arr, search_value)
if __name__ == "__main__":
    main()