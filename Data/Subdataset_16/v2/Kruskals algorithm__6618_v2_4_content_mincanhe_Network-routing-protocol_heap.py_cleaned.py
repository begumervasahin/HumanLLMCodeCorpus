def fonk1(b7, b5):
    b1 = len(b7) - 1
    b2 = 2 * b5
    b3 = 2 * b5 + 1
    b4 = b5
    if b2 <= b1 and b7[b2] > b7[b5]:
        b4 = b2
    if b3 <= b1 and b7[b3] > b7[b4]:
        b4 = b3
    if b4 != b5:
        b7[b5], b7[b4] = b7[b4], b7[b5]
        fonk1(b7, b4)
def fonk2(b7):
    b1 = len(b7) - 1
    for b5 in range(b1
        fonk1(b7, b5)
def fonk3(b7):
    fonk2(b7)
    b1 = len(b7) - 1
    for b5 in range(b1, 1, -1):
        b7[1], b7[b5] = b7[b5], b7[1]
        fonk1(b7[:b5], 1)
def fonk4(b7):
    return b7[1]
def fonk5(b7, value):
    b7.append(value)
    b5 = len(b7) - 1
    while b5 > 1 and b7[b5
        b7[b5], b7[b5
        b5 = b5
def fonk6(b7, b5):
    b1 = len(b7) - 1
    b7[b5] = b7[b1]
    b7.pop()
    fonk1(b7, b5)
if b6 = = "__main__":
    b7 = [0, 4, 10, 3, 5, 1]
    print("Original array:", b7[1:])
    fonk2(b7)
    print("Max-heap:", b7[1:])
    fonk3(b7)
    print("Sorted array:", b7[1:])
    b7 = [0, 4, 10, 3, 5, 1]
    fonk5(b7, 6)
    print("After inserting 6:", b7[1:])
    fonk6(b7, 2)
    print("After deleting element at index 2:", b7[1:])
    print("Maximum element:", fonk4(b7))