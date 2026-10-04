def fonk1():
    b1 = input("Type in 5 integers of any sequence separated by commas. Example: 1,2,3,4,5: ")
    b2 = b1.split(",")
    b3 = list(map(int, b2))
    if len(b3) != 5:
        print("Please enter exactly 5 integers.")
        return
    if fonk2(b3):
        print("Arithmetic Sequence")
    if fonk3(b3):
        print("This is a Geometric Sequence")
    if fonk4(b3):
        print("This is a Quadratic Sequence")
    if fonk5(b3):
        print("This is a Cubic Sequence")
    if fonk6(b3):
        print("Fibonacci Sequence")
def fonk2(lst):
    b4 = lst[1] - lst[0]
    return all(lst[i] == lst[i - 1] + b4 for i in range(1, 5))
def fonk3(lst):
    if lst[0] == 0:
        return False
    b5 = lst[1]
    return all(lst[i] == lst[i - 1] * b5 for i in range(1, 5))
def fonk4(lst):
    b6 = [lst[i] - lst[i - 1] for i in range(1, 5)]
    b7 = [b6[i] - b6[i - 1] for i in range(1, 4)]
    return all(b7[i] == b7[0] for i in range(1, 3))
def fonk5(lst):
    b6 = [lst[i] - lst[i - 1] for i in range(1, 5)]
    b7 = [b6[i] - b6[i - 1] for i in range(1, 4)]
    b8 = [b7[i] - b7[i - 1] for i in range(1, 3)]
    return all(b8[i] == b8[0] for i in range(1, 2))
def fonk6(lst):
    return all(lst[i] == lst[i - 1] + lst[i - 2] for i in range(2, 5))
if b9 = = "__main__":
    fonk1()