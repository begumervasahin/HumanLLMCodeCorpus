def fonk1(b3):
    b1 = len(b3)
    for i in range(b1):
        b2 = i
        for j in range(i + 1, b1):
            if b3[j] < b3[b2]:
                b2 = j
        b3[i], b3[b2] = b3[b2], b3[i]
    return b3
b3 = [49, 25, 26, 2, 99]
b4 = fonk1(b3)
print("Sorted array is:")
for element in b4:
    print(element, b5 = ' ')