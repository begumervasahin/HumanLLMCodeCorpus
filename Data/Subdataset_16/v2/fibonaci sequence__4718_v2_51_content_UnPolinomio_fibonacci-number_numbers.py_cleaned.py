def fonk1(how_many):
    b1 = [1, 1]
    for i in range(2, how_many):
        b1.append(b1[i - 1] + b1[i - 2])
    for index, number in enumerate(b1):
        print(f"{index + 1}.- {number}")
def fonk2():
    b2 = input("\nHow many numbers do you want to calculate?\n>> ")
    if not b2:
        print("\nError: Please insert a value.")
        return
    try:
        b2 = int(b2)
    except ValueError:
        print("\nError: Insert an integer number please.")
        return
    if b2 < 2:
        print("\nError: Please insert a positive number; where number >= 2.")
    else:
        fonk1(b2)
if b3 = = "__main__":
    fonk2()