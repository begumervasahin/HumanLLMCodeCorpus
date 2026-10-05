def linear_search(arr, val):
    found = False
    for index, element in enumerate(arr):
        if element == val:
            print(f"The value {val} is found at index {index}")
            found = True
    if not found:
        print(f"The value {val} is not found in the array")
def get_array_size_from_user():
    return int(input("Enter the size of the array: "))
def get_array_elements_from_user(size):
    arr = []
    for i in range(size):
        element = int(input(f"Enter element {i + 1}: "))
        arr.append(element)
    return arr
def display_array(arr):
    print("Array:", arr)
def get_search_value_from_user():
    return int(input("Enter the value you want to search for: "))
def main():
    array_size = get_array_size_from_user()
    arr = get_array_elements_from_user(array_size)
    display_array(arr)
    search_value = get_search_value_from_user()
    linear_search(arr, search_value)
if __name__ == "__main__":
    main()