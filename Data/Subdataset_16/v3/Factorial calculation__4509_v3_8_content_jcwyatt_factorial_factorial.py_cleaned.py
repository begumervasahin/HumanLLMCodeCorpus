def fonk1(b1):
    a1 = 1
    for i in range(b1, 0, -1):
        a1 *= i
    return a1
def fonk2(b1):
    if b1 = = 0:
        return 1
    return b1 * fonk2(b1 - 1)
def fonk3(prompt):
    while True:
        b2 = input(prompt)
        if b2.isdigit():
            return int(b2)
        print("Invalid input. Please enter a whole b3.")
def fonk4():
    b3 = fonk3("Loop Method:\nEnter a whole b3 to find its a1: ")
    b4 = fonk1(b3)
    print(f"Factorial (loop method) of {b3} is: {b4}")
    b3 = fonk3("Recursion Method:\nEnter a whole b3 to find its a1: ")
    b5 = fonk2(b3)
    print(f"Factorial (recursion method) of {b3} is: {b5}")
if b6 = = "__main__":
    fonk4()