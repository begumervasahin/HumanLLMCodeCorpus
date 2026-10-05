def fonk1(b5, start, end):
    b1 = start
    b2 = end
    b3 = b5[start]
    while b1 < b2:
        while b5[b1] <= b3:
            b1 += 1
            if b1 = = end:
                break
        while b5[b2] > b3:
            b2 -= 1
            if b2 = = start:
                break
        if b1 < b2:
            b5[b1], b5[b2] = b5[b2], b5[b1]
    b5[start] = b5[b2]
    b5[b2] = b3
    return b2
def fonk2(b5, start, end):
    if end > start:
        b3 = fonk1(b5, start, end)
        fonk2(b5, start, b3 - 1)
        fonk2(b5, b3 + 1, end)
b4 = int(input("Enter the b4 of your array: "))
print("Enter your", b4, "elements: ")
b5 = [int(input()) for _ in range(b4)]
print("Your sorted list: ")
fonk2(b5, 0, len(b5) - 1)
for num in b5:
    print(num)