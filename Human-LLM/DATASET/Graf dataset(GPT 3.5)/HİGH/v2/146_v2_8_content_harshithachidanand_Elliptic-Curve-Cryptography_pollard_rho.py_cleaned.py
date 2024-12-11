
b1 = (5 ** 30) % 2017
print("Initial value (S1): ", b1, "\n")
b2 = []
for i in range(1, 10):
    b3 = (b1 ** 2) % 2017
    if 1 <= b3 <= 672:
        print("Computed value (S0): ", b3, "\n")
    elif 673 <= b3 <= 1345:
        print("Computed value (S1): ", b3, "\n")
    elif 1346 <= b3 <= 2016:
        print("Computed value (S2): ", b3, "\n")
    else:
        print("Oops! Value out of range.\n")
    b2.append(b1)
    b2.append(b3)
    b1 = (1736 * b3) % 2017
    if 1 <= b1 <= 672:
        print("Next value (S0): ", b1, "\n")
    elif 673 <= b1 <= 1345:
        print("Next value (S1): ", b1, "\n")
    elif 1346 <= b1 <= 2016:
        print("Next value (S2): ", b1, "\n")
    else:
        print("Oops! Next value out of range.\n")
print("Computed values: ", b2)
b4 = {b1: [i for i, v in enumerate(b2) if v == b1] for b1 in b2}
print("Indices of computed values: ", b4)