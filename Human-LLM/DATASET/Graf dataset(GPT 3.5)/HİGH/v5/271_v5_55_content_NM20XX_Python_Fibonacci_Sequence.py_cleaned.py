def fonk1(n):
    x, b1 = 0, 1
    for _ in range(n):
        yield x
        x, b1 = b1, x + b1
def fonk2(prompt):
    while True:
        try:
            b2 = int(input(prompt))
            if b2 <= 0:
                print("Please enter a positive value.")
            else:
                return b2
        except ValueError:
            print("Invalid input. Please enter an integer value.")
def fonk3():
    b2 = fonk2("Enter the number of Fibonacci numbers to generate: ")
    print("Fibonacci sequence up to b2", b2, ":")
    for n in fonk1(b2):
        print(n)
if b3 = = "__main__":
    fonk3()