def fonk1():
    b1 = input("Type in 5 integers of any sequence separated by commas. Example: 1,2,3,4,5: ")
    b2 = b1.split(",")
    b3 = list(map(int, b2))
    if len(b3) != 5:
        print("Please enter exactly 5 integers.")
        return
    b4 = b3[1] - b3[0]
    b5 = all(b3[i] == b3[i - 1] + b4 for i in range(1, 5))
    if b5:
        print("Arithmetic Sequence")
    b6 = b3[1]
    b7 = b6 is not None and all(b3[i] == b3[i - 1] * b6 for i in range(1, 5))
    if b7:
        print("Geometric Sequence")
    b8 = [b3[i] - b3[i - 1] for i in range(1, 5)]
    b9 = [b8[i] - b8[i - 1] for i in range(1, 4)]
    b10 = all(b9[i] == b9[0] for i in range(1, 3))
    if b10:
        print("Quadratic Sequence")
    b11 = [b9[i] - b9[i - 1] for i in range(1, 3)]
    b12 = all(b11[i] == b11[0] for i in range(1, 2))
    if b12:
        print("Cubic Sequence")
    b13 = all(b3[i] == b3[i - 1] + b3[i - 2] for i in range(2, 5))
    if b13:
        print("Fibonacci Sequence")
if b14 = = "__main__":
    fonk1()