print("Shank's algorithm!\n")
print("\nS table\n")
for x in range(46):
    b1 = (5 ** (45 * x)) % 2017
    print(f"{x} {b1}\n")
print("\nT table\n")
for y in range(46):
    b1 = (1736 * (5 ** y)) % 2017
    print(f"{y} {b1}\n")
print("\nPairs (x, y) where S[x] == T[y]\n")
for x in range(46):
    b2 = (5 ** (45 * x)) % 2017
    for y in range(46):
        b3 = (1736 * (5 ** y)) % 2017
        if b2 = = b3:
            print(f"{x} {y}\n")