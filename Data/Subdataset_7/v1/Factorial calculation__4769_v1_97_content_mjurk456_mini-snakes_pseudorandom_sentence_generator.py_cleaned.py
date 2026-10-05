import random
def fonk1():
    b1 = []
    b2 = []
    b3 = []
    b4 = []
    with open("b4.txt", "r") as fverb:
        b4 = fverb.readlines()
    with open("b1.txt", "r") as fadverb:
        b1 = fadverb.readlines()
    with open("b2.txt", "r") as fnoun:
        b2 = fnoun.readlines()
    with open("b3.txt", "r") as fadj:
        b3 = fadj.readlines()
    while True:
        try:
            b5 = int(input("How many sentences do you want to generate? "))
            break
        except ValueError:
            print("Wrong input, please use integer numbers!")
    for i in range(b5):
        b6 = (
            "A " + b3[random.randrange(len(b3))].strip() +
            " " + b2[random.randrange(len(b2))].strip() +
            " " + b4[random.randrange(len(b4))].strip() +
            " a " + b3[random.randrange(len(b3))].strip() +
            " " + b2[random.randrange(len(b2))].strip() +
            " " + b1[random.randrange(len(b1))].strip() + "."
        )
        print(b6)
if b7 = = "__main__":
    fonk1()