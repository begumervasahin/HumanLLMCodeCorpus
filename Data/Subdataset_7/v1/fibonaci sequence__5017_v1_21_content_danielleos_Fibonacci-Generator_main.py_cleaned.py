def fonk1(b3):
    b1 = []
    a1 = 0
    a2 = 0
    a3 = 0
    for b2 in range(1, b3):
        if b2 = = 1:
            b1.append(a1)
            a1 = a1 + 1
            b1.append(a1)
            a3 = a2
            a2 = a1
        else:
            a1 = a3 + a2
            b1.append(a1)
            a3 = a2
            a2 = a1
    return b1
while True:
    try:
        b3 = int(input("How many Fibonacci numbers do you want to see? "))
    except ValueError:
        print("Sorry, I did not understand that input. Please input a whole b3.")
        continue
    if b3 <= 0:
        print("Sorry, please enter a positive integer.")
        continue
    else:
        print(f"Producing {b3} Fibonacci numbers...")
        b4 = fonk1(b3)
        print(f"Fibonacci numbers: {b4}")
        break