def fonk1(arr: list) -> None:
    b1 = len(arr)
    for passnum in range(b1 - 1, 0, -1):
        for i in range(passnum):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
def fonk2() -> None:
    b2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    fonk1(b2)
    print("Sorted list:", b2)
if b3 = = "__main__":
    fonk2()