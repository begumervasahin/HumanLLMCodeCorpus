import statistics
def fonk1(arr, first, last):
    b1 = arr[first]
    b2 = arr[last]
    b3 = (first + last)
    b4 = statistics.median([b1, arr[b3], b2])
    if b4 = = b1:
        b5 = first
    elif b4 = = b2:
        b5 = last
    else:
        b5 = b3
    arr[last], arr[b5] = arr[b5], arr[last]
    b6 = arr[last]
    b7 = first
    b8 = last - 1
    while True:
        while b7 <= b8 and arr[b7] <= b6:
            b7 += 1
        while b7 <= b8 and arr[b8] >= b6:
            b8 -= 1
        if b8 < b7:
            break
        else:
            arr[b7], arr[b8] = arr[b8], arr[b7]
    arr[first], arr[b8] = arr[b8], arr[first]
    return b8
def fonk2(arr, first, last):
    if first < last:
        b9 = fonk1(arr, first, last)
        fonk2(arr, first, b9 - 1)
        fonk2(arr, b9 + 1, last)
b10 = [56, 26, 93, 17, 31, 44]
b11 = len(b10)
fonk2(b10, 0, b11 - 1)
print(b10)