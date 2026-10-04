import statistics
def fonk1(b8, first, last):
    b1 = (first + last)
    b2 = [b8[first], b8[b1], b8[last]]
    b3 = statistics.median(b2)
    if b3 = = b8[first]:
        return first
    elif b3 = = b8[last]:
        return last
    else:
        return b1
def fonk2(b8, first, last):
    b4 = fonk1(b8, first, last)
    b8[b4], b8[last] = b8[last], b8[b4]
    b5 = b8[last]
    left, b6 = first, last - 1
    while True:
        while left <= b6 and b8[left] <= b5:
            left += 1
        while left <= b6 and b8[b6] >= b5:
            b6 -= 1
        if left > b6:
            break
        b8[left], b8[b6] = b8[b6], b8[left]
    b8[left], b8[last] = b8[last], b8[left]
    return left
def fonk3(b8, first, last):
    if first < last:
        b4 = fonk2(b8, first, last)
        fonk3(b8, first, b4 - 1)
        fonk3(b8, b4 + 1, last)
if b7 = = "__main__":
    b8 = [56, 26, 93, 17, 31, 44]
    fonk3(b8, 0, len(b8) - 1)
    print("Sorted array:", b8)