def fonk1(b6):
    b1 = []
    b5, b4, b2 = 0, 0, 0
    for b3 in range(1, b6 + 1):
        if b3 = = 1:
            b1.append(b5)
            b5 += 1
            b1.append(b5)
            b2 = b4
            b4 = b5
        else:
            b5 = b2 + b4
            b1.append(b5)
            b2 = b4
            b4 = b5
    return b1
def fonk2():
    while True:
        try:
            b6 = int(input("How many Fibonacci numbers do you want to see? "))
        except ValueError:
            print("Sorry, I did not understand that input, please input a whole b6.")
            continue
        if b6 <= 0:
            print("Sorry, seems like that is not a positive integer, try again please.")
            continue
        else:
            print(f"Producing {b6} Fibonacci numbers...")
            b7 = fonk1(b6)
            print(b7)
            break
if b8 = = "__main__":
    fonk2()