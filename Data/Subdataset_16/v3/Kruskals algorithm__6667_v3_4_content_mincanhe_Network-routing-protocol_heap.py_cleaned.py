def fonk1(b8, b5):
    b1 = len(b8) - 1
    b2 = 2 * b5
    b3 = 2 * b5 + 1
    b4 = b5
    if b2 <= b1 and b8[b2] > b8[b5]:
        b4 = b2
    if b3 <= b1 and b8[b3] > b8[b4]:
        b4 = b3
    if b4 != b5:
        b8[b5], b8[b4] = b8[b4], b8[b5]
        fonk1(b8, b4)
def fonk2(b8):
    b1 = len(b8) - 1
    for b5 in range(b1
        fonk1(b8, b5)
def fonk3(b8):
    fonk2(b8)
    b1 = len(b8) - 1
    for b5 in range(b1, 1, -1):
        b8[1], b8[b5] = b8[b5], b8[1]
        fonk1(b8[:b5], 1)
def fonk4(b8):
    return b8[1]
def fonk5(b8, value):
    b8.append(value)
    b5 = len(b8) - 1
    while b5 > 1 and b8[b5
        b8[b5], b8[b5
        b5 = b5
def fonk6(b8, b5):
    b1 = len(b8) - 1
    b8[b5] = b8[b1]
    b8.pop()
    fonk1(b8, b5)
def fonk7(b8, b6 = ""):
    if b6:
        print(b6)
    print(b8[1:])
if b7 = = "__main__":
    b8 = [0, 4, 10, 3, 5, 1]
    fonk7(b8, "Original array:")
    fonk2(b8)
    fonk7(b8, "Max-heap:")
    fonk3(b8)
    fonk7(b8, "Sorted array:")
    b8 = [0, 4, 10, 3, 5, 1]
    fonk5(b8, 6)
    fonk7(b8, "After inserting 6:")
    fonk6(b8, 2)
    fonk7(b8, "After deleting element at index 2:")
    print("Maximum element:", fonk4(b8))