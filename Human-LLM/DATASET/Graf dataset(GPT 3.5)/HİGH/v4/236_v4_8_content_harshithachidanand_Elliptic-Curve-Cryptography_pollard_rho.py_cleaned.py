
b1 = (5 ** 30) % 2017
print("Initial value (S1):", b1, "\n")
b2 = []
for i in range(1, 10):
    b3 = (b1 ** 2) % 2017
    if 1 <= b3 <= 672:
        b4 = "S0"
    elif 673 <= b3 <= 1345:
        b4 = "S1"
    elif 1346 <= b3 <= 2016:
        b4 = "S2"
    else:
        b4 = "Oops"
    print(f"{b4}: {b3}\n")
    b2.append(b1)
    b2.append(b3)
    b5 = (1736 * b3) % 2017
    if 1 <= b5 <= 672:
        b6 = "S0"
    elif 673 <= b5 <= 1345:
        b6 = "S1"
    elif 1346 <= b5 <= 2016:
        b6 = "S2"
    else:
        b6 = "Oops"
    print(f"{b6}: {b5}\n")
    b1 = b5
print("Values list:", b2)
b7 = {val: [i for i, v in enumerate(b2) if v == val] for val in b2}
print("Mapped values:", b7)