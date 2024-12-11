
print("Shank's algorithm!\n")
print("\nS table\n")
for power_of_45 in range(46):
    b1 = (5 ** (45 * power_of_45)) % 2017
    print(f"{power_of_45} {b1}\n")
print("\nT table\n")
for power_of_5 in range(46):
    b1 = (1736 * (5 ** power_of_5)) % 2017
    print(f"{power_of_5} {b1}\n")
print("\nPairs (x, y) where S[x] == T[y]\n")
for x in range(46):
    b2 = (5 ** (45 * x)) % 2017
    for y in range(46):
        b3 = (1736 * (5 ** y)) % 2017
        if b2 = = b3:
            print(f"{x} {y}\n")