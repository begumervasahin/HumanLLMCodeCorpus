def fonk1(b5, start, end):
    b1 = b5[start]
    b2 = start + 1
    b3 = end
    while True:
        while b2 <= b3 and b5[b2] <= b1:
            b2 += 1
        while b2 <= b3 and b5[b3] >= b1:
            b3 -= 1
        if b2 <= b3:
            b5[b2], b5[b3] = b5[b3], b5[b2]
        else:
            break
    b5[start], b5[b3] = b5[b3], b5[start]
    return b3
def fonk2(b5, start, end):
    if start < end:
        b4 = fonk1(b5, start, end)
        fonk2(b5, start, b4 - 1)
        fonk2(b5, b4 + 1, end)
def fonk3():
    b5 = []
    b6 = int(input("Enter the b6 of your array: "))
    print(f"Enter your {b6} elements:")
    for _ in range(b6):
        b7 = int(input())
        b5.append(b7)
    fonk2(b5, 0, len(b5) - 1)
    print("Your sorted array:")
    for b7 in b5:
        print(b7)
if b8 = = "__main__":
    fonk3()