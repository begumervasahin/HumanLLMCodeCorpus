def fonk1(length):
    b1 = [1, 1]
    for i in range(2, length):
        b1.append(b1[i-1] + b1[i-2])
    for index, number in enumerate(b1, 1):
        print(f"{index}. {number}")
b2 = input("\nHow many Fibonacci numbers do you want to calculate?\n>> ")
if b2.strip() == "":
    print("\nError: Please insert a value.")
else:
    try:
        b3 = int(b2)
        if b3 < 2:
            raise ValueError("Quantity must be greater than or equal to 2.")
    except ValueError:
        print("\nError: Please insert an integer greater than or equal to 2.")
    else:
        fonk1(b3)