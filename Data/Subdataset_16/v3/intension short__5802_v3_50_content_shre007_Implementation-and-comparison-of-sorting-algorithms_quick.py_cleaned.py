import statistics
def fonk1(arr, first, last):
    b1 = arr[first]
    b2 = arr[(first + last)
    b3 = arr[last]
    b4 = statistics.median([b1, b2, b3])
    if b4 = = b1:
        b5 = first
    elif b4 = = b3:
        b5 = last
    else:
        b5 = (first + last)
    arr[b5], arr[last] = arr[last], arr[b5]
    b6 = first
    b7 = last - 1
    while True:
        while b6 <= b7 and arr[b6] <= b4:
            b6 += 1
        while b6 <= b7 and arr[b7] >= b4:
            b7 -= 1
        if b6 > b7:
            break
        arr[b6], arr[b7] = arr[b7], arr[b6]
    arr[last], arr[b7] = arr[b7], arr[last]
    return b7
def fonk2(arr, first, last):
    if first < last:
        b5 = fonk1(arr, first, last)
        fonk2(arr, first, b5 - 1)
        fonk2(arr, b5 + 1, last)
if b8 = = "__main__":
    b9 = [56, 26, 93, 17, 31, 44]
    fonk2(b9, 0, len(b9) - 1)
    print("Sorted list:", b9)