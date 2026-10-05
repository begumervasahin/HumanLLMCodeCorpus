import random
def fonk1(filename):
    with open(filename, "r") as file:
        return [word.strip() for word in file.readlines()]
def fonk2(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Wrong input. Please use integer numbers!")
def fonk3(b3, b4, b5, b6, count):
    for _ in range(count):
        b1 = (
            "A " + random.choice(b3) + " " +
            random.choice(b4) + " " + random.choice(b5) +
            " a " + random.choice(b3) + " " +
            random.choice(b4) + " " + random.choice(b6) + "."
        )
        print(b1)
if b2 = = "__main__":
    b3 = fonk1("b3.txt")
    b4 = fonk1("b4.txt")
    b5 = fonk1("b5.txt")
    b6 = fonk1("b6.txt")
    b7 = fonk2("How many sentences do you want to generate? ")
    fonk3(b3, b4, b5, b6, b7)