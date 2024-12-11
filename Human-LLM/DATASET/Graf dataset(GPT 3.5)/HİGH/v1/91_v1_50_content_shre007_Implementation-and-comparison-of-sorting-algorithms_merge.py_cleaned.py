def fonk1(b5):
    if len(b5) > 1:
        b1 = len(b5)
        b2 = b5[:b1]
        b3 = b5[b1:]
        fonk1(b2)
        fonk1(b3)
        a1 = 0
        a2 = 0
        a3 = 0
        while len(b2) > a1 and len(b3) > a2:
            if b2[a1] < b3[a2]:
                b5[a3] = b2[a1]
                a1 += 1
            else:
                b5[a3] = b3[a2]
                a2 += 1
            a3 += 1
        while len(b2) > a1:
            b5[a3] = b2[a1]
            a1 += 1
            a3 += 1
        while len(b3) > a2:
            b5[a3] = b3[a2]
            a2 += 1
            a3 += 1
b4 = int(input("How many elements do you want in this list: "))
b5 = [int(input("Enter element: ")) for _ in range(b4)]
fonk1(b5)
print("Sorted list:", b5)