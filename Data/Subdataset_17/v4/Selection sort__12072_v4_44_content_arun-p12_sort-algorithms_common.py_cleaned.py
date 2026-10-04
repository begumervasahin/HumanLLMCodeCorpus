def find_minimum(arr):
    if not isinstance(arr, list):
        print("List expected. Got:", type(arr))
        exit(1)
    min_value, min_index = arr[0], 0
    for i in range(1, len(arr)):
        if arr[i] < min_value:
            min_value, min_index = arr[i], i
    return min_value, min_index
def find_maximum(arr):
    if not isinstance(arr, list):
        print("List expected. Got:", type(arr))
        exit(1)
    max_value, max_index = arr[0], 0
    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_value, max_index = arr[i], i
    return max_value, max_index
def swap(a, b):
    return b, a
if __name__ == "__main__":
    test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    min_value, min_index = find_minimum(test_list)
    print(f"Minimum value: {min_value} at index {min_index}")
    max_value, max_index = find_maximum(test_list)
    print(f"Maximum value: {max_value} at index {max_index}")
    a, b = 10, 20
    a, b = swap(a, b)
    print(f"Swapped values: a = {a}, b = {b}")