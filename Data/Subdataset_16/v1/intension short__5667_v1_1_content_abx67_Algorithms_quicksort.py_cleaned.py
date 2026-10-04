def fonk1(b3, left, right):
    if left >= right:
        return right
    else:
        b1 = left
        b2 = b3[right]
        print("b2:", b2)
        for i in range(left, right + 1):
            print("i:", i)
            if b3[i] <= b2:
                if i != b1:
                    b3[i], b3[b1] = b3[b1], b3[i]
                b1 += 1
        return b1 - 1
def fonk2(b3, left, right):
    if left < right:
        b1 = fonk1(b3, left, right)
        print("b1:", b1, "left:", left, "right:", right)
        print("b3:", b3)
        if b1 >= left + 1:
            fonk2(b3, left, b1 - 1)
        if b1 <= right - 1:
            fonk2(b3, b1 + 1, right)
b3 = [3, 6, 8, 10, 1, 2, 1]
fonk2(b3, 0, len(b3) - 1)
print("Sorted array:", b3)