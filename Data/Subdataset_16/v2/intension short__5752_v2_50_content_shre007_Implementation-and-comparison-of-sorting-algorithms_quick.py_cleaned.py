import statistics
def fonk1(arr, first, last):
    low, mid, b1 = arr[first], arr[(first + last)
    b2 = statistics.median([low, mid, b1])
    if b2 = = low:
        b3 = first
    elif b2 = = b1:
        b3 = last
    else:
        b3 = (first + last)
    arr[b3], arr[last] = arr[last], arr[b3]
    b4 = arr[last]
    left, b5 = first, last - 1
    while True:
        while left <= b5 and arr[left] <= b4:
            left += 1
        while left <= b5 and arr[b5] >= b4:
            b5 -= 1
        if left > b5:
            break
        arr[left], arr[b5] = arr[b5], arr[left]
    arr[first], arr[b5] = arr[b5], arr[first]
    return b5
def fonk2(arr, first, last):
    if first < last:
        b3 = fonk1(arr, first, last)
        fonk2(arr, first, b3 - 1)
        fonk2(arr, b3 + 1, last)
if b6 = = "__main__":
    b7 = [56, 26, 93, 17, 31, 44]
    fonk2(b7, 0, len(b7) - 1)
    print("Sorted list:", b7)