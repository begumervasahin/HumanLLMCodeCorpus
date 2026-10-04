def binary_search_iterative(array, value):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high)
        if array[mid] == value:
            return f"Value {value} is at the {mid} position of the array"
        elif array[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    return f"Value {value} is not in the array"
def binary_search_recursive(array, value, low, high):
    if low > high:
        return f"Value {value} is not in the array"
    mid = (low + high)
    if array[mid] == value:
        return f"Value {value} is at the {mid} position of the array"
    elif array[mid] > value:
        return binary_search_recursive(array, value, low, mid - 1)
    else:
        return binary_search_recursive(array, value, mid + 1, high)
if __name__ == '__main__':
    prime_numbers = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
        59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113
    ]
    print(binary_search_iterative(prime_numbers, 73))
    print(binary_search_iterative(prime_numbers, 4))
    print(binary_search_recursive(prime_numbers, 73, 0, len(prime_numbers) - 1))
    print(binary_search_recursive(prime_numbers, 4, 0, len(prime_numbers) - 1))