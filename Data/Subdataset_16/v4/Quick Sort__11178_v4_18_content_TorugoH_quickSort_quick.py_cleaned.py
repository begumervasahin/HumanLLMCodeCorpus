def fonk1(b5, start, end):
    b1 = start
    b2 = end
    b3 = b5[start]
    while b1 < b2:
        while b1 < b2 and b5[b1] <= b3:
            b1 += 1
        while b5[b2] > b3:
            b2 -= 1
        if b1 < b2:
            b5[b1], b5[b2] = b5[b2], b5[b1]
    b5[start], b5[b2] = b5[b2], b5[start]
    return b2
def fonk2(b5, start, end):
    if start < end:
        b4 = fonk1(b5, start, end)
        fonk2(b5, start, b4 - 1)
        fonk2(b5, b4 + 1, end)
def fonk3():
    b5 = []
    print("Enter the b6 of the array:")
    b6 = int(input())
    print(f"Enter {b6} elements:")
    for _ in range(b6):
        b7 = int(input())
        b5.append(b7)
    print("Sorted array:")
    fonk2(b5, 0, len(b5) - 1)
    for b7 in b5:
        print(b7)
if b8 = = "__main__":
    fonk3()