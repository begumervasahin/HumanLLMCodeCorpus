def fonk1(arr: list, value: any, b4: b1 = 0, b2: b1 = None) -> b1:
    if b2 is None:
        b2 = len(arr) - 1
    while b4 <= b2:
        b3 = (b4 + b2)
        if arr[b3] < value:
            b4 = b3 + 1
        elif arr[b3] > value:
            b2 = b3 - 1
        else:
            return b3
    return -1
def fonk2() -> None:
    b5 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    a1 = 7
    b6 = fonk1(b5, a1)
    print(f"Index of {a1} in the list: {b6}")
if b7 = = "__main__":
    fonk2()