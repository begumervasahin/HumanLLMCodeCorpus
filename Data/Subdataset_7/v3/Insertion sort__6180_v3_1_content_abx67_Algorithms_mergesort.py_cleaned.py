def fonk1(b7, b1, right, b5):
    if b1 = = b5 == right:
        return
    b2 = b7[b1:b5 + 1]
    b3 = b7[b5 + 1:right + 1]
    i, j, b4 = 0, 0, b1
    while i < len(b2) and j < len(b3):
        if b2[i] <= b3[j]:
            b7[b4] = b2[i]
            i += 1
        else:
            b7[b4] = b3[j]
            j += 1
        b4 += 1
    while i < len(b2):
        b7[b4] = b2[i]
        i += 1
        b4 += 1
    while j < len(b3):
        b7[b4] = b3[j]
        j += 1
        b4 += 1
def fonk2(b7, b1, right):
    if b1 < right:
        b5 = (b1 + right)
        fonk2(b7, b1, b5)
        fonk2(b7, b5 + 1, right)
        fonk1(b7, b1, right, b5)
if b6 = = "__main__":
    b7 = [38, 27, 43, 3, 9, 82, 10]
    fonk2(b7, 0, len(b7) - 1)
    print("Sorted array:", b7)