import random
def fonk1(dig):
    b1 = []
    for x in range(dig):
        b1.append(str(random.randint(0, 9)))
    b2 = "".join(b1)
    return b2
def fonk2():
    a1 = 10
    b3 = fonk1(a1)
    print(f"Random number of a1 {a1}: {b3}")
if b4 = = "__main__":
    fonk2()