def fonk1(how_many):
    b1 = [1, 1]
    for i in range(how_many - 2):
        b2 = i + 2
        b1.append(b1[b2 - 1] + b1[b2 - 2])
    for i, num in enumerate(b1):
        print(f"{i + 1}.- {num}")
b3 = input("\nHow many numbers do you want to calculate?\n>> ")
if b3 = = "":
    print("\nError: Please insert a value.")
else:
    try:
        b3 = int(b3)
    except ValueError:
        print("\nError: Insert an integer number please.")
    else:
        if b3 < 2:
            print("\nError: Please insert a positive number; where number >= 2.")
        else:
            fonk1(b3)