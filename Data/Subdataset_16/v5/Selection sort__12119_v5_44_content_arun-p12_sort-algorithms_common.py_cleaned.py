def fonk1(arr):
    if not isinstance(arr, list):
        print("List expected. Got:", type(arr))
        exit(1)
    b1 = arr[0]
    a1 = 0
    for i in range(1, len(arr)):
        if arr[i] < b1:
            b1 = arr[i]
            a1 = i
    return b1, a1
def fonk2(arr):
    if not isinstance(arr, list):
        print("List expected. Got:", type(arr))
        exit(1)
    b2 = arr[0]
    a2 = 0
    for i in range(1, len(arr)):
        if arr[i] > b2:
            b2 = arr[i]
            a2 = i
    return b2, a2
def fonk3(b6, b5):
    return b5, b6
if b3 = = "__main__":
    b4 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    b1, a1 = fonk1(b4)
    print(f"Minimum value: {b1} at index {a1}")
    b2, a2 = fonk2(b4)
    print(f"Maximum value: {b2} at index {a2}")
    b6, b5 = 10, 20
    b6, b5 = fonk3(b6, b5)
    print(f"Swapped values: b6 = {b6}, b5 = {b5}")