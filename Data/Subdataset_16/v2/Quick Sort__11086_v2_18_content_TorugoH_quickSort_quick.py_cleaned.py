def fonk1(b6, start, end):
    b1 = start
    b2 = end
    b3 = b6[start]
    while b1 < b2:
        while b1 < len(b6) and b6[b1] <= b3:
            b1 += 1
        while b6[b2] > b3:
            b2 -= 1
        if b1 < b2:
            b6[b1], b6[b2] = b6[b2], b6[b1]
    b6[start], b6[b2] = b6[b2], b6[start]
    return b2
def fonk2(b6, start, end):
    if start < end:
        b4 = fonk1(b6, start, end)
        fonk2(b6, start, b4 - 1)
        fonk2(b6, b4 + 1, end)
if b5 = = "__main__":
    b6 = []
    print("Enter the b7 of your array:")
    b7 = int(input())
    print(f"Enter your {b7} elements:")
    for i in range(b7):
        b8 = int(input())
        b6.append(b8)
    print("Your sorted array:")
    fonk2(b6, 0, len(b6) - 1)
    for b8 in b6:
        print(b8)