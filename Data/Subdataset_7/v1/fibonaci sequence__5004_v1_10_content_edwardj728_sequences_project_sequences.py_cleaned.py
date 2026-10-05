def fonk1(sequence):
    for i in range(1, len(sequence) - 1):
        if sequence[i + 1] != sequence[i] + (sequence[i] - sequence[i - 1]):
            return False
    return True
def fonk2(sequence):
    for i in range(1, len(sequence) - 1):
        if sequence[i + 1] != sequence[i] * 2:
            return False
    return True
def fonk3(sequence):
    if len(sequence) < 3:
        return False
    b1 = sequence[1] - sequence[0]
    b2 = sequence[2] - sequence[1]
    for i in range(2, len(sequence)):
        if sequence[i] != sequence[i - 1] + b2:
            return False
    return True
def fonk4(sequence):
    if len(sequence) < 4:
        return False
    b1 = sequence[1] - sequence[0]
    b2 = sequence[2] - sequence[1]
    b3 = sequence[3] - sequence[2]
    b4 = b2 - b1
    b5 = b3 - b2
    return b4 = = b5
def fonk5(sequence):
    if len(sequence) < 4:
        return False
    for i in range(2, len(sequence) - 1):
        if sequence[i] != sequence[i - 1] + sequence[i - 2]:
            return False
    return True
b6 = input("Type in 5 integers of any sequence separated by commas. Example: 1,2,3,4,5: ")
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