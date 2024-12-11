def fonk1(length):
    b1 = [1, 1]
    for i in range(length - 2):
        b2 = i + 2
        b1.append(b1[b2 - 1] + b1[b2 - 2])
    for index, number in enumerate(b1):
        print(f"{index + 1}.- {number}")
b3 = input("\nHow many Fibonacci numbers do you want to calculate?\n>> ")
if b3 = = "":
    print("\nError: Please insert a value.")
else:
    try:
        b3 = int(b3)
    except ValueError:
        print("\nError: Please insert an integer number.")
    else:
        if b3 < 2:
            print("\nError: Please insert a positive number greater than or equal to 2.")
        else:
            fonk1(b3)