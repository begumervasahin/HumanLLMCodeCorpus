def binary_search_iterative(array, value):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right)
        if array[mid] == value:
            return f"Value {value} is at position {mid} in the array"
        elif array[mid] > value:
            right = mid - 1
        else:
            left = mid + 1
    return f"Value {value} is not in the array"
def binary_search_recursive(array, value, left, right):
    if left > right:
        return f"Value {value} is not in the array"
    mid = (left + right)
    if array[mid] == value:
        return f"Value {value} is at position {mid} in the array"
    elif array[mid] > value:
        return binary_search_recursive(array, value, left, mid - 1)
    else:
        return binary_search_recursive(array, value, mid + 1, right)
if __name__ == '__main__':
    prime_numbers = [
        2, 3, 5, 7, 11, 13, 17, 19, 23,
        29, 31, 37, 41, 43, 47, 53, 59,
        61, 67, 71, 73, 79, 83, 89, 97,
        101, 103, 107, 109, 113
    ]
    target_values = [73, 4]
    for value in target_values:
        print("Iterative:", binary_search_iterative(prime_numbers, value))
        print("Recursive:", binary_search_recursive(prime_numbers, value, 0, len(prime_numbers) - 1))