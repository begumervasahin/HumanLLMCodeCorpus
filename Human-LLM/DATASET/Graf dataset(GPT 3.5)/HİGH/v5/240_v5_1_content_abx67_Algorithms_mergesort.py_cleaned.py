def fonk1(b7, b1, end, b5):
    if b1 = = end == b5:
        return
    b2 = b7[b1:b5 + 1]
    b3 = b7[b5 + 1:end + 1]
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
def fonk2(b7, b1, end):
    if b1 < end:
        b5 = (b1 + end)
        fonk2(b7, b1, b5)
        fonk2(b7, b5 + 1, end)
        fonk1(b7, b1, end, b5)
if b6 = = "__main__":
    b7 = [38, 27, 43, 3, 9, 82, 10]
    fonk2(b7, 0, len(b7) - 1)
    print("Sorted array:", b7)