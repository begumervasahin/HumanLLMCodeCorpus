def fonk1(n):
    a1 = 0
    a2 = 1
    for _ in range(n):
        yield a1
        a1, a2 = a2, a1 + a2
def fonk2():
    while True:
        try:
            b1 = int(input("Enter the b1 in the Fibonacci sequence: "))
            if b1 <= 0:
                print("Please enter a positive value.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer value.")
    print("Fibonacci sequence up to b1", b1, ":")
    a3 = 0
    a1, a2 = 0, 1
    while a3 < b1:
        if b1 = = 1:
            print(a1)
        else:
            print(a1, b2 = ', ')
            a1, a2 = a2, a1 + a2
        a3 += 1
def fonk3():
    b3 = input("Choose an approach (1 - Generator Function, 2 - While Loop): ")
    if b3 = = "1":
        b1 = get_input()
        for n in fonk1(b1):
            print(n)
    elif b3 = = "2":
        fonk2()
    else:
        print("Invalid b3. Please enter either '1' or '2'.")
if b4 = = "__main__":
    fonk3()