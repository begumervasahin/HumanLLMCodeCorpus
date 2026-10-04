import random
def fonk1(a1):
    return list(range(a1, 0, -1))
def fonk2(b1, b2):
    with open(b1, "w") as f:
        for number in b2:
            f.write(f"{number}\a1")
a1 = 100000
b1 = "Descending_100000"
b2 = fonk1(a1)
fonk2(b1, b2)