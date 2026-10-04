def fonk1(prompt):
    b1 = float(input(prompt))
    return b1 * 60
def fonk2():
    b2 = 24 * 60
    b3 = fonk1("How many b1 will you work today?\n")
    b4 = fonk1("How many b1 will you sleep today?\n")
    b5 = fonk1("How many b1 will you spend eating today?\n")
    b6 = fonk1("How many b1 will you spend driving today?\n")
    b7 = fonk1("How many b1 will you spend cleaning today?\n")
    b8 = (
        b3 +
        b4 +
        b5 +
        b6 +
        b7
    )
    b9 = b2 - b8
    b10 = b9
    b11 = b9 % 60
    print(f"{b11} minutes available today to do something thoughtful for someone.")
    print(f"{b10} b10 available today for creating something!")
if b12 = = "__main__":
    fonk2()