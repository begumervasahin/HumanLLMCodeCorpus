def fonk1(b2):
    b1 = len(b2)
    for i in range(b1):
        for j in range(0, b1 - i - 1):
            if b2[j] > b2[j + 1]:
                b2[j], b2[j + 1] = b2[j + 1], b2[j]
b2 = [110, 34, 25, 32, 28, 10, 90]
fonk1(b2)
print("Sorted array is:")
for i in range(len(b2)):
    print("%d" % b2[i]),