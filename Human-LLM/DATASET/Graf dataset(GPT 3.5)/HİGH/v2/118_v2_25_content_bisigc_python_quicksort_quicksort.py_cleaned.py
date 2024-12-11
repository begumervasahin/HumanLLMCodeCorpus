def fonk1(b3, left, right):
    if left < right:
        b1 = b3[left]
        b2 = left
        for i in range(left + 1, right):
            if b3[i] < b1:
                b2 += 1
                b3[b2], b3[i] = b3[i], b3[b2]
        b3[left], b3[b2] = b3[b2], b3[left]
        fonk1(b3, left, b2)
        fonk1(b3, b2 + 1, right)
b3 = [3, 6, 8, 1, 5, 2, 7, 4]
fonk1(b3, 0, len(b3))
print(b3)