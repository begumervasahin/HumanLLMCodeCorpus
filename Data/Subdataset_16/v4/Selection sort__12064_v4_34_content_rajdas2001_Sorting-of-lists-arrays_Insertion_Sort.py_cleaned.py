def fonk1(b3):
    for i in range(1, len(b3)):
        b1 = b3[i]
        b2 = i - 1
        while b2 >= 0 and b1 < b3[b2]:
            b3[b2 + 1] = b3[b2]
            b2 -= 1
        b3[b2 + 1] = b1
b3 = [32, 13, 14, 15, 98]
fonk1(b3)
print("Sorted array is:")
for element in b3:
    print(element, b4 = ' ')