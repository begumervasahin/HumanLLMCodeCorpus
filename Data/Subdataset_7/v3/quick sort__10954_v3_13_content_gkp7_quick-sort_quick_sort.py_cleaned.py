def fonk1(arr):
    fonk2(arr, 0, len(arr) - 1)
def fonk2(arr, first, last):
    if first < last:
        b1 = fonk3(arr, first, last)
        fonk2(arr, first, b1 - 1)
        fonk2(arr, b1 + 1, last)
def fonk3(arr, first, last):
    b2 = arr[first]
    b3 = first + 1
    b4 = last
    while b3 <= b4:
        while b3 <= b4 and arr[b3] <= b2:
            b3 += 1
        while arr[b4] >= b2 and b4 >= b3:
            b4 -= 1
        if b4 < b3:
            break
        arr[b3], arr[b4] = arr[b4], arr[b3]
    arr[first], arr[b4] = arr[b4], arr[first]
    return b4
if b5 = = "__main__":
    b6 = [57, 26, 93, 77, 33, 44, 50, 20]
    fonk1(b6)
    print(b6)