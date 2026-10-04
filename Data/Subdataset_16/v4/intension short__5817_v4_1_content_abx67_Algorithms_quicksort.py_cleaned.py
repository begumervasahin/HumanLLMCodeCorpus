def fonk1(b3, left, right):
    if left >= right:
        return right
    b1 = b3[right]
    b2 = left
    print(f"Pivot: {b1}")
    for i in range(left, right + 1):
        print(f"Index: {i}")
        if b3[i] <= b1:
            if i != b2:
                b3[i], b3[b2] = b3[b2], b3[i]
            b2 += 1
    return b2 - 1
def fonk2(b3, left, right):
    if left < right:
        b2 = fonk1(b3, left, right)
        print(f"Split index: {b2}, Left: {left}, Right: {right}")
        print(f"Array after partition: {b3}")
        if b2 >= left + 1:
            fonk2(b3, left, b2 - 1)
        if b2 <= right - 1:
            fonk2(b3, b2 + 1, right)
b3 = [3, 6, 8, 10, 1, 2, 1]
fonk2(b3, 0, len(b3) - 1)
print(f"Sorted array: {b3}")