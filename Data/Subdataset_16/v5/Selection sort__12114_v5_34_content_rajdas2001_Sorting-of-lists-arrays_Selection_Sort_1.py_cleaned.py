def fonk1(b4):
    b1 = len(b4)
    for i in range(b1):
        b2 = i
        for j in range(i + 1, b1):
            if b4[j] < b4[b2]:
                b2 = j
        b4[i], b4[b2] = b4[b2], b4[i]
    return b4
if b3 = = "__main__":
    b4 = [49, 25, 26, 2, 99]
    b5 = fonk1(b4)
    print("Sorted array is:")
    for element in b5:
        print(element, b6 = ' ')