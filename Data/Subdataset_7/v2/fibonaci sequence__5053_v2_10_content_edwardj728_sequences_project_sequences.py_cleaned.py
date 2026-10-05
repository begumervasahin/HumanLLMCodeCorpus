def fonk1(b8):
    for i in range(1, len(b8) - 1):
        if b8[i + 1] != b8[i] + (b8[i] - b8[i - 1]):
            return False
    return True
def fonk2(b8):
    for i in range(1, len(b8) - 1):
        if b8[i + 1] != b8[i] * 2:
            return False
    return True
def fonk3(b8):
    if len(b8) < 3:
        return False
    b1 = b8[1] - b8[0]
    b2 = b8[2] - b8[1]
    for i in range(2, len(b8)):
        if b8[i] != b8[i - 1] + b2:
            return False
    return True
def fonk4(b8):
    if len(b8) < 4:
        return False
    b1 = b8[1] - b8[0]
    b2 = b8[2] - b8[1]
    b3 = b8[3] - b8[2]
    b4 = b2 - b1
    b5 = b3 - b2
    return b4 = = b5
def fonk5(b8):
    if len(b8) < 4:
        return False
    for i in range(2, len(b8) - 1):
        if b8[i] != b8[i - 1] + b8[i - 2]:
            return False
    return True
b6 = input("Type in 5 integers of any b8 separated by commas. Example: 1,2,3,4,5: ")
b7 = b6.split(",")
b8 = list(map(int, b7))
if fonk1(b8):
    print("Arithmetic Sequence")
if fonk2(b8):
    print("Geometric Sequence")
if fonk3(b8):
    print("Quadratic Sequence")
if fonk4(b8):
    print("Cubic Sequence")
if fonk5(b8):
    print("Fibonacci Sequence")