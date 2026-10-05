
print("Shank's algorithm!\n")
print("\nS table\n")
for power_of_45 in range(46):
    val = (5 ** (45 * power_of_45)) % 2017
    print(f"{power_of_45} {val}\n")
print("\nT table\n")
for power_of_5 in range(46):
    val = (1736 * (5 ** power_of_5)) % 2017
    print(f"{power_of_5} {val}\n")
print("\nPairs (x, y) where S[x] == T[y]\n")
for x in range(46):
    S_x_val = (5 ** (45 * x)) % 2017
    for y in range(46):
        T_y_val = (1736 * (5 ** y)) % 2017
        if S_x_val == T_y_val:
            print(f"{x} {y}\n")