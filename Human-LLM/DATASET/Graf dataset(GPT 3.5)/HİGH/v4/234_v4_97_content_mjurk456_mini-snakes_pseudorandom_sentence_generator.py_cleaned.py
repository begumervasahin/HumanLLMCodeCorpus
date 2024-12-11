import random
b1 = []
b2 = []
b3 = []
b4 = []
with open("b4.txt", "r") as fverb:
    b4 = [word.strip() for word in fverb.readlines()]
with open("b1.txt", "r") as fadverb:
    b1 = [word.strip() for word in fadverb.readlines()]
with open("b2.txt", "r") as fnoun:
    b2 = [word.strip() for word in fnoun.readlines()]
with open("b3.txt", "r") as fadj:
    b3 = [word.strip() for word in fadj.readlines()]
while True:
    try:
        b5 = int(input("How many sentences do you want to generate? "))
        break
    except ValueError:
        print("Wrong input. Please use integer numbers!")
for _ in range(b5):
    b6 = (
        "A " + random.choice(b3) + " " +
        random.choice(b2) + " " + random.choice(b4) +
        " a " + random.choice(b3) + " " +
        random.choice(b2) + " " + random.choice(b1) + "."
    )
    print(b6)