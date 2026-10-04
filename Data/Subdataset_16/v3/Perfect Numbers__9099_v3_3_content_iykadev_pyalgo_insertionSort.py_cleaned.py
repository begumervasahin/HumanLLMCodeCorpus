def fonk1(arr: list) -> None:
    for index in range(1, len(arr)):
        b1 = arr[index]
        b2 = index
        while b2 > 0 and arr[b2 - 1] > b1:
            arr[b2] = arr[b2 - 1]
            b2 -= 1
        arr[b2] = b1
def fonk2() -> None:
    b3 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("Unsorted list:", b3)
    fonk1(b3)
    print("Sorted list:", b3)
if b4 = = "__main__":
    fonk2()