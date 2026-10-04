def fonk1():
    b1 = input("Type in 5 integers of any sequence separated by commas. Example: 1,2,3,4,5: ")
    b2 = b1.split(",")
    b3 = list(map(int, b2))
    if len(b3) != 5:
        print("Please enter exactly 5 integers.")
        return
    b4 = b3[1] - b3[0]
    if all(b3[i] == b3[i-1] + b4 for i in range(1, 5)):
        print("Arithmetic Sequence")
    if all(b3[i] == b3[i-1] * 2 for i in range(1, 5)):
        print("This is a Geometric Sequence")
    b5 = b3[1] - b3[0]
    b6 = b3[2] - b3[1]
    b7 = b6 - b5
    if b3[1] == b3[0] + b5 and b3[2] == b3[1] + b6:
        print("This is a Quadratic Sequence")
    b8 = b3[1] - b3[0]
    b9 = b3[2] - b3[1]
    b10 = b3[3] - b3[2]
    b11 = b10 - b9
    b12 = b9 - b8
    if b11 = = b12:
        print("This is a Cubic Sequence")
    b13 = b3[0] + b3[1]
    b14 = b3[1] + b3[2]
    if b3[2] == b13 and b3[3] == b14:
        print("Fibonacci Sequence")
if b15 = = "__main__":
    fonk1()