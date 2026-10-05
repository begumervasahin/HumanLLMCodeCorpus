def fonk1(b7, low, b5):
    b1 = low - 1
    b2 = b7[b5]
    for j in range(low, b5):
        if b7[j] <= b2:
            b1 += 1
            b7[b1], b7[j] = b7[j], b7[b1]
    b7[b1 + 1], b7[b5] = b7[b5], b7[b1 + 1]
    return b1 + 1
def fonk2(b7, low, b5):
    b3 = b5 - low + 1
    b4 = [(low, b5)]
    while b4:
        low, b5 = b4.pop()
        b6 = fonk1(b7, low, b5)
        if b6 - 1 > low:
            b4.append((low, b6 - 1))
        if b6 + 1 < b5:
            b4.append((b6 + 1, b5))
b7 = [4, 3, 5, 2, 1, 3, 2, 3]
fonk2(b7, 0, len(b7) - 1)
print("Sorted array is:")
print(*b7)