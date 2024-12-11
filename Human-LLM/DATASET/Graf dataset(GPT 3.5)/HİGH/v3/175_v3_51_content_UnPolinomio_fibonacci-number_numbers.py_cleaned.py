def fonk1(length):
    b1 = [1, 1]
    for i in range(length - 2):
        b2 = b1[-1] + b1[-2]
        b1.append(b2)
    for index, b4 in enumerate(b1):
        print(f"{index + 1}.- {b4}")
def fonk2(prompt):
    while True:
        b3 = input(prompt)
        if b3.isdigit():
            b4 = int(b3)
            if b4 >= 2:
                return b4
            else:
                print("\nError: Please insert a positive b4 greater than or equal to 2.")
        else:
            print("\nError: Please insert an integer b4.")
b5 = fonk2("\nHow many Fibonacci numbers do you want to calculate?\n>> ")
fonk1(b5)