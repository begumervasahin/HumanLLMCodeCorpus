def fonk1(b4, left, right):
    if left >= right:
        return right
    b1 = b4[right]
    b2 = left
    for i in range(left, right + 1):
        if b4[i] <= b1:
            if i != b2:
                b4[i], b4[b2] = b4[b2], b4[i]
            b2 += 1
    return b2 - 1
def fonk2(b4, left, right):
    if right != left:
        b2 = fonk1(b4, left, right)
        if b2 >= left + 1:
            fonk2(b4, left, b2 - 1)
        if b2 <= right - 1:
            fonk2(b4, b2 + 1, right)
if b3 = = "__main__":
    b4 = [38, 27, 43, 3, 9, 82, 10]
    fonk2(b4, 0, len(b4) - 1)
    print("Sorted array:", b4)