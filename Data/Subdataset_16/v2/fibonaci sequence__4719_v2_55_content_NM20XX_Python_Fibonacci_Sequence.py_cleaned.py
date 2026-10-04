def fonk1(n):
    x, b1 = 0, 1
    for _ in range(n):
        yield x
        x, b1 = b1, x + b1
def fonk2():
    while True:
        try:
            b2 = int(input("Enter a b2 in the Fibonacci sequence: "))
            if b2 <= 0:
                print("Please enter a positive integer.")
            else:
                return b2
        except ValueError:
            print("Error: Please enter an integer value.")
def fonk3():
    b3 = fonk2()
    print(f"Fibonacci sequence up to {b3} terms:")
    for number in fonk1(b3):
        print(number, b4 = ", ")
    print()
if b5 = = "__main__":
    fonk3()