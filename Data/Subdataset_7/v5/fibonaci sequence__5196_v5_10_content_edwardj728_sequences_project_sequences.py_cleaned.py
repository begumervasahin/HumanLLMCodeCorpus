def fonk1(b5):
    b1 = b5[1] - b5[0]
    for i in range(2, len(b5)):
        if b5[i] != b5[i - 1] + b1:
            return False
    return True
def fonk2(b5):
    for i in range(1, len(b5) - 1):
        if b5[i + 1] != b5[i] * 2:
            return False
    return True
def fonk3(b5):
    if len(b5) < 3:
        return False
    b1 = b5[1] - b5[0]
    b2 = b5[2] - b5[1]
    if b1 = = b2:
        return True
    return False
def fonk4(b5):
    if len(b5) < 4:
        return False
    b1 = b5[1] - b5[0]
    b2 = b5[2] - b5[1]
    b3 = b5[3] - b5[2]
    if b3 - b2 = = b2 - b1:
        return True
    return False
def fonk5(b5):
    if len(b5) < 4:
        return False
    for i in range(2, len(b5) - 1):
        if b5[i] != b5[i - 1] + b5[i - 2]:
            return False
    return True
b4 = input("Type in 5 integers of any b5 separated by commas. Example: 1,2,3,4,5: ")
b5 = list(map(int, b4.split(",")))
if fonk1(b5):
    print("Arithmetic Sequence")
if fonk2(b5):
    print("Geometric Sequence")
if fonk3(b5):
    print("Quadratic Sequence")
if fonk4(b5):
    print("Cubic Sequence")
if fonk5(b5):
    print("Fibonacci Sequence")