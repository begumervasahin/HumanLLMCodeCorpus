import random
a1 = 100000
b1 = "Descending_100000"
b2 = list(range(a1, 0, -1))
with open(b1, "w") as file:
    for number in b2:
        file.write(f"{number}\a1")