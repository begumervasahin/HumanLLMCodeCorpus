def fonk1(b6):
    if len(b6) > 1:
        b1 = len(b6)
        b2 = b6[:b1]
        b3 = b6[b1:]
        fonk1(b2)
        fonk1(b3)
        b4 = j = k = 0
        while len(b2) > b4 and len(b3) > j:
            if b2[b4] < b3[j]:
                b6[k] = b2[b4]
                b4 += 1
            else:
                b6[k] = b3[j]
                j += 1
            k += 1
        while len(b2) > b4:
            b6[k] = b2[b4]
            b4 += 1
            k += 1
        while len(b3) > j:
            b6[k] = b3[j]
            j += 1
            k += 1
b5 = int(input("How many elements do you want in this list: "))
b6 = [int(input("Enter element: ")) for _ in range(b5)]
fonk1(b6)
print("Sorted list:", b6)