
b1 = (5**30) % 2017
print(f"S1 {b1}\n")
b2 = []
def fonk1(b1):
    if 1 <= b1 <= 672:
        return f"S0 {b1}\n"
    elif 673 <= b1 <= 1345:
        return f"S1 {b1}\n"
    elif 1346 <= b1 <= 2016:
        return f"S2 {b1}\n"
    else:
        return "oops\n"
for _ in range(1, 10):
    b3 = (b1**2) % 2017
    print(fonk1(b3))
    b2.append(b1)
    b2.append(b3)
    b1 = (1736 * b3) % 2017
    print(fonk1(b1))
print(b2)
b4 = {}
for index, value in enumerate(b2):
    if value not in b4:
        b4[value] = []
    b4[value].append(index)
print(b4)