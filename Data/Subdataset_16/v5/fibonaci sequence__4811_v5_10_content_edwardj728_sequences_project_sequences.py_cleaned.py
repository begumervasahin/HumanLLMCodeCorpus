def fonk1():
    b1 = input("Type in 5 integers of any sequence separated by commas. Example: 1,2,3,4,5: ")
    b2 = fonk2(b1)
    if len(b2) != 5:
        print("Please enter exactly 5 integers.")
        return
    fonk3(b2)
def fonk2(b1):
    try:
        return list(map(int, b1.split(",")))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        sys.exit()
def fonk3(lst):
    if fonk4(lst):
        print("Arithmetic Sequence")
    if fonk5(lst):
        print("Geometric Sequence")
    if fonk6(lst):
        print("Quadratic Sequence")
    if fonk7(lst):
        print("Cubic Sequence")
    if fonk8(lst):
        print("Fibonacci Sequence")
def fonk4(lst):
    b3 = lst[1] - lst[0]
    return all(lst[i] == lst[i - 1] + b3 for i in range(1, 5))
def fonk5(lst):
    if lst[0] == 0:
        return False
    b4 = lst[1]
    return all(lst[i] == lst[i - 1] * b4 for i in range(1, 5))
def fonk6(lst):
    b5 = [lst[i] - lst[i - 1] for i in range(1, 5)]
    b6 = [b5[i] - b5[i - 1] for i in range(1, 4)]
    return all(b6[i] == b6[0] for i in range(1, 3))
def fonk7(lst):
    b5 = [lst[i] - lst[i - 1] for i in range(1, 5)]
    b6 = [b5[i] - b5[i - 1] for i in range(1, 4)]
    b7 = [b6[i] - b6[i - 1] for i in range(1, 3)]
    return all(b7[i] == b7[0] for i in range(1, 2))
def fonk8(lst):
    return all(lst[i] == lst[i - 1] + lst[i - 2] for i in range(2, 5))
if b8 = = "__main__":
    fonk1()