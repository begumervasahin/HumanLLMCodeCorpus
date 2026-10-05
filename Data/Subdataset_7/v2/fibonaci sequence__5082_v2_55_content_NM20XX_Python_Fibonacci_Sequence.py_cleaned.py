def fonk1(n):
    x, b1 = 0, 1
    for _ in range(n):
        yield x
        x, b1 = b1, x + b1
def fonk2():
    while True:
        try:
            b2 = int(input("Enter the b2 in the Fibonacci sequence: "))
            if b2 <= 0:
                print("Please enter a positive value.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer value.")
    print("Fibonacci sequence up to b2", b2, ":")
    x, b1 = 0, 1
    for cnt in range(b2):
        if b2 = = 1:
            print(x)
        else:
            print(x, b3 = ', ')
            x, b1 = b1, x + b1
def fonk3():
    print("Choose an approach:")
    print("1 - Generator Function")
    print("2 - While Loop")
    b4 = input("Enter your b4: ")
    if b4 = = "1":
        b2 = int(input("Enter the b2 in the Fibonacci sequence: "))
        print("Fibonacci sequence up to b2", b2, ":")
        for n in fonk1(b2):
            print(n)
    elif b4 = = "2":
        fonk2()
    else:
        print("Invalid b4. Please enter either '1' or '2'.")
if b5 = = "__main__":
    fonk3()