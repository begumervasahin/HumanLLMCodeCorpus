def fonk1(b4):
    if b4 < 1:
        return []
    b1 = [0]
    if b4 > 1:
        b1.append(1)
    for _ in range(2, b4):
        b2 = b1[-1] + b1[-2]
        b1.append(b2)
    return b1
def fonk2(prompt):
    while True:
        try:
            b3 = int(input(prompt))
            if b3 > 0:
                return b3
            else:
                print("Sorry, seems like that is not a positive integer, try again please.")
        except ValueError:
            print("Sorry, I did not understand that input, please input a whole number.")
def fonk3():
    b4 = fonk2("How many Fibonacci numbers do you want to see? ")
    print(f"Producing {b4} Fibonacci numbers...")
    b5 = fonk1(b4)
    print(b5)
if b6 = = "__main__":
    fonk3()