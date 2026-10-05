def binary_search_iterative(array, value):
    minimum = 0
    maximum = len(array) - 1
    while minimum <= maximum:
        middle = (minimum + maximum)
        if array[middle] == value:
            return "Value {} is at position {} in the array".format(value, middle)
        elif array[middle] > value:
            maximum = middle - 1
        else:
            minimum = middle + 1
    return "Value {} is not in the array".format(value)
def binary_search_recursive(array, value, minimum, maximum):
    if minimum > maximum:
        return "Value {} is not in the array".format(value)
    middle = (minimum + maximum)
    if array[middle] == value:
        return "Value {} is at position {} in the array".format(value, middle)
    elif array[middle] > value:
        return binary_search_recursive(array, value, minimum, middle - 1)
    else:
        return binary_search_recursive(array, value, middle + 1, maximum)
if __name__ == '__main__':
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23,
                     29, 31, 37, 41, 43, 47, 53, 59,
                     61, 67, 71, 73, 79, 83, 89, 97,
                     101, 103, 107, 109, 113]
    print(binary_search_iterative(prime_numbers, 73))
    print(binary_search_iterative(prime_numbers, 4))
    print(binary_search_recursive(prime_numbers, 73, 0, len(prime_numbers) - 1))
    print(binary_search_recursive(prime_numbers, 4, 0, len(prime_numbers) - 1))