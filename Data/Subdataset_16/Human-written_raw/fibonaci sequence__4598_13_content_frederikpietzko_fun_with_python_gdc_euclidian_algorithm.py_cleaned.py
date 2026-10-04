def fonk1(b2, b1):
    if b1 = = 0:
        return b2
    if b2 = = 0:
        return b1
    if b2 > b1:
        return fonk1(b2-b1, b1)
    else:
        return fonk1(b2, b1-b2)
def fonk2(b2, b1):
    if b1 = = 0:
        return b2
    else:
        return fonk2(b1, b2 % b1)
if b3 = = "__main__":
    while True:
        b4 = input("Classic (c) or modern euclid (e) algorithm?")
        while True:
            b5 = input(
                "Enter exit to choose algorithm. Otherwise enter b2 number: ")
            if b5.isnumeric():
                b2 = int(b5)
                b1 = int(input("Enter second number: "))
                b6 = fonk1(
                    b2, b1) if b4 = = "c" else fonk2(b2, b1)
                print(b6)
            else:
                break