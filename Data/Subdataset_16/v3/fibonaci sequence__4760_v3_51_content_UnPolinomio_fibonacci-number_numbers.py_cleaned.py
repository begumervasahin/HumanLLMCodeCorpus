def fonk1(how_many):
    b1 = [1, 1]
    for i in range(2, how_many):
        b2 = b1[i - 1] + b1[i - 2]
        b1.append(b2)
    for index, number in enumerate(b1):
        print(f"{index + 1}.- {number}")
def fonk2():
    b3 = input("\nHow many numbers do you want to calculate?\n>> ")
    if not b3:
        print("\nError: Please insert a value.")
        return
    try:
        b3 = int(b3)
    except ValueError:
        print("\nError: Insert an integer number please.")
        return
    if b3 < 2:
        print("\nError: Please insert a positive number; where number >= 2.")
    else:
        fonk1(b3)
if b4 = = "__main__":
    fonk2()