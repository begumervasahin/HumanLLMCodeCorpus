def fonk1(b7, start, end):
    b1 = b7[start]
    b2 = start + 1
    b3 = end
    b4 = False
    while not b4:
        while b2 <= b3 and b7[b2] <= b1:
            b2 = b2 + 1
        while b7[b3] >= b1 and b3 >= b2:
            b3 = b3 - 1
        if b3 < b2:
            b4 = True
        else:
            b7[b2], b7[b3] = b7[b3], b7[b2]
    b7[start], b7[b3] = b7[b3], b7[start]
    return b3
def fonk2(b7, start, end):
    if start < end:
        b5 = fonk1(b7, start, end)
        fonk2(b7, start, b5 - 1)
        fonk2(b7, b5 + 1, end)
def fonk3():
    b6 = int(input("Enter the b6 of the array: "))
    print(f"Enter {b6} elements:")
    return [int(input()) for _ in range(b6)]
def fonk4():
    b7 = fonk3()
    fonk2(b7, 0, len(b7) - 1)
    print("Sorted array:")
    for num in b7:
        print(num)
if b8 = = "__main__":
    fonk4()