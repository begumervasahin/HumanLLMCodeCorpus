def print_shanks_algorithm():
    print("Shank's Algorithm!\n")
    print("S table:\n")
    s_values = {}
    for x in range(46):
        val = (5**(45 * x)) % 2017
        s_values[val] = x
        print(f"{x} {val}")
    print("\nT table:\n")
    for y in range(46):
        val = (1736 * (5**y)) % 2017
        print(f"{y}  {val}")
    print("\nMatching Values:\n")
    for y in range(46):
        y_val = (1736 * (5**y)) % 2017
        if y_val in s_values:
            print(f"{s_values[y_val]} {y}")
print_shanks_algorithm()