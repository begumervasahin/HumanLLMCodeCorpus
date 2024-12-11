def fonk1(b6):
    for i in range(1, len(b6) - 1):
        if b6[i + 1] != b6[i] + (b6[i] - b6[i - 1]):
            return False
    return True
def fonk2(b6):
    for i in range(1, len(b6) - 1):
        if b6[i + 1] != b6[i] * 2:
            return False
    return True
def fonk3(b6):
    if len(b6) < 3:
        return False
    b1 = [b6[i] - b6[i - 1] for i in range(1, len(b6))]
    return all(b2 = = b1[0] for b2 in b1)
def fonk4(b6):
    if len(b6) < 4:
        return False
    b1 = [b6[i] - b6[i - 1] for i in range(1, len(b6))]
    b3 = [b1[i + 1] - b1[i] for i in range(0, len(b1) - 1)]
    return all(b4 = = b3[0] for b4 in b3)
def fonk5(b6):
    if len(b6) < 4:
        return False
    return all(b6[i] == b6[i - 1] + b6[i - 2] for i in range(2, len(b6)))
b5 = input("Type in 5 integers of any b6 separated by commas. Example: 1,2,3,4,5: ")
b6 = list(map(int, b5.split(",")))
if fonk1(b6):
    print("Arithmetic Sequence")
if fonk2(b6):
    print("Geometric Sequence")
if fonk3(b6):
    print("Quadratic Sequence")
if fonk4(b6):
    print("Cubic Sequence")
if fonk5(b6):
    print("Fibonacci Sequence")