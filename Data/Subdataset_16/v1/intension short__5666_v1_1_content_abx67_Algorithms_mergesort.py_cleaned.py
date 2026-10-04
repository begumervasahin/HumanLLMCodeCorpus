def fonk1(b5, left, b4, right):
    b1 = b5[left:b4+1]
    b2 = b5[b4+1:right+1]
    a1 = 0
    a2 = 0
    b3 = left
    while a1 < len(b1) and a2 < len(b2):
        if b1[a1] <= b2[a2]:
            b5[b3] = b1[a1]
            a1 += 1
        else:
            b5[b3] = b2[a2]
            a2 += 1
        b3 += 1
    while a1 < len(b1):
        b5[b3] = b1[a1]
        a1 += 1
        b3 += 1
    while a2 < len(b2):
        b5[b3] = b2[a2]
        a2 += 1
        b3 += 1
def fonk2(b5, left, right):
    if left < right:
        b4 = left + (right - left)
        fonk2(b5, left, b4)
        fonk2(b5, b4 + 1, right)
        fonk1(b5, left, b4, right)
b5 = [12, 11, 13, 5, 6, 7]
print("Original array:", b5)
fonk2(b5, 0, len(b5) - 1)
print("Sorted array:", b5)