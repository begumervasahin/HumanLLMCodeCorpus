def fonk1(arr: list, value: any, b3: b1 = 0, b2: b1 = -1) -> b1:
    if not arr:
        return -1
    if b2 = = -1:
        b2 = len(arr) - 1
    if b3 = = b2:
        return b3 if arr[b3] == value else -1
    b4 = (b3 + b2)
    if arr[b4] > value:
        return fonk1(arr, value, b3, b4 - 1)
    elif arr[b4] < value:
        return fonk1(arr, value, b4 + 1, b2)
    else:
        return b4
def fonk2() -> None:
    b5 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    a1 = 7
    b6 = fonk1(b5, a1)
    print(f"Index of {a1} in the list: {b6}")
if b7 = = "__main__":
    fonk2()