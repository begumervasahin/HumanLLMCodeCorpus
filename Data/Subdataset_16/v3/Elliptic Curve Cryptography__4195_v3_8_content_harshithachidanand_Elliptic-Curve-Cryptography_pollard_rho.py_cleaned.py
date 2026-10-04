
b1 = (5**30) % 2017
print(f"S1 {b1}\n")
b2 = []
def fonk1(b3):
    if 1 <= b3 <= 672:
        return f"S0 {b3}\n"
    elif 673 <= b3 <= 1345:
        return f"S1 {b3}\n"
    elif 1346 <= b3 <= 2016:
        return f"S2 {b3}\n"
    else:
        return "oops\n"
b3 = b1
for _ in range(1, 10):
    b4 = (b3**2) % 2017
    print(fonk1(b4))
    b2.append(b3)
    b2.append(b4)
    b3 = (1736 * b4) % 2017
    print(fonk1(b3))
print(b2)
b5 = {}
for index, value in enumerate(b2):
    if value not in b5:
        b5[value] = []
    b5[value].append(index)
print(b5)