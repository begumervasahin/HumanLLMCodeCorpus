
b1 = input("Type in 5 integers of any b2 separated by commas. Example: 1,2,3,4,5: ")
b2 = list(map(int, b1.split(",")))
if b2[1] == b2[0] + (b2[1] - b2[0]) and b2[2] == b2[1] + (b2[1] - b2[0]):
    print("Arithmetic Sequence")
if b2[1] == b2[0] * 2 and b2[2] == b2[1] * 2 and b2[3] == b2[2] * 2:
    print("Geometric Sequence")
b3 = b2[1] - b2[0]
b4 = b2[2] - b2[1]
if b2[1] == b2[0] + b3 and b2[2] == b2[1] + b4:
    print("Quadratic Sequence")
b5 = b2[3] - b2[2]
if b5 - b4 = = b4 - b3:
    print("Cubic Sequence")
if b2[2] == b2[0] + b2[1] and b2[3] == b2[1] + b2[2]:
    print("Fibonacci Sequence")