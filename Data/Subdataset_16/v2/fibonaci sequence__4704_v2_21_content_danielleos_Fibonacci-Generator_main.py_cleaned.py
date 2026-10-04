def fonk1(b1):
    if b1 = = 1:
        return [0]
    b2 = [0, 1]
    for _ in range(2, b1):
        b3 = b2[-1] + b2[-2]
        b2.append(b3)
    return b2
def fonk2():
    while True:
        try:
            b1 = int(input("How many Fibonacci numbers do you want to see? "))
        except ValueError:
            print("Sorry, I did not understand that input, please input a whole number.")
            continue
        if b1 <= 0:
            print("Sorry, seems like that is not a positive integer, try again please.")
            continue
        else:
            print(f"Producing {b1} Fibonacci numbers...")
            b4 = fonk1(b1)
            print(b4)
            break
if b5 = = "__main__":
    fonk2()