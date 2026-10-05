def linear_search(arr, val):
    for index, element in enumerate(arr):
        if element == val:
            return index
    return -1
def main():
    n = int(input("Enter the size of the array: "))
    arr = []
    for i in range(n):
        element = int(input("Enter element {} of the array: ".format(i+1)))
        arr.append(element)
    print("Array:", arr)
    search_value = int(input("Enter the value you want to search for: "))
    index = linear_search(arr, search_value)
    if index != -1:
        print("The value", search_value, "is found at index", index)
    else:
        print("Value not found in the array")
if __name__ == "__main__":
    main()