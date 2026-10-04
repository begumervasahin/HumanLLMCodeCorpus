
b1 = (5**30) % 2017
print(f"S1 {b1}\n")
b2 = []
for i in range(1, 10):
    b3 = (b1**2) % 2017
    if 1 <= b3 <= 672:
        print(f"S0 {b3}\n")
    elif 673 <= b3 <= 1345:
        print(f"S1 {b3}\n")
    elif 1346 <= b3 <= 2016:
        print(f"S2 {b3}\n")
    else:
        print("oops\n")
    b2.append(b1)
    b2.append(b3)
    b1 = (1736 * b3) % 2017
    if 1 <= b1 <= 672:
        print(f"S0 {b1}\n")
    elif 673 <= b1 <= 1345:
        print(f"S1 {b1}\n")
    elif 1346 <= b1 <= 2016:
        print(f"S2 {b1}\n")
    else:
        print("oops\n")
print(b2)
b4 = {b1: [i for i in range(len(b2)) if b2[i] == b1] for b1 in b2}
print(b4)