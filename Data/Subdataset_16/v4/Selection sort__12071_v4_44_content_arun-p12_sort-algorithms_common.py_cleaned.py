def fonk1(arr):
    if not isinstance(arr, list):
        print("List expected. Got:", type(arr))
        exit(1)
    min_value, b1 = arr[0], 0
    for i in range(1, len(arr)):
        if arr[i] < min_value:
            min_value, b1 = arr[i], i
    return min_value, b1
def fonk2(arr):
    if not isinstance(arr, list):
        print("List expected. Got:", type(arr))
        exit(1)
    max_value, b2 = arr[0], 0
    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_value, b2 = arr[i], i
    return max_value, b2
def fonk3(b6, b5):
    return b5, b6
if b3 = = "__main__":
    b4 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    min_value, b1 = fonk1(b4)
    print(f"Minimum value: {min_value} at index {b1}")
    max_value, b2 = fonk2(b4)
    print(f"Maximum value: {max_value} at index {b2}")
    b6, b5 = 10, 20
    b6, b5 = fonk3(b6, b5)
    print(f"Swapped values: b6 = {b6}, b5 = {b5}")