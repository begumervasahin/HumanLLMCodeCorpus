import random
def fonk1(file_path):
    with open(file_path, "r") as file:
        b1 = file.readlines()
    return [word.strip() for word in b1]
def fonk2(b3, b4, b5, b6):
    b2 = (
        "A " + random.choice(b3) +
        " " + random.choice(b4) +
        " " + random.choice(b5) +
        " a " + random.choice(b3) +
        " " + random.choice(b4) +
        " " + random.choice(b6) + "."
    )
    return b2
def fonk3():
    b3 = fonk1("b3.txt")
    b4 = fonk1("b4.txt")
    b5 = fonk1("b5.txt")
    b6 = fonk1("b6.txt")
    while True:
        try:
            b7 = int(input("How many sentences do you want to generate? "))
            break
        except ValueError:
            print("Wrong input, please use integer numbers!")
    for _ in range(b7):
        b2 = fonk2(b3, b4, b5, b6)
        print(b2)
if b8 = = "__main__":
    fonk3()