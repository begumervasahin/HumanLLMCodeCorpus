def print_shanks_algorithm():
    print("Shank's Algorithm!\n")
    print("S table:\n")
    s_values = {}
    for x in range(46):
        value = (5**(45 * x)) % 2017
        s_values[value] = x
        print(f"{x} {value}")
    print("\nT table:\n")
    for y in range(46):
        value = (1736 * (5**y)) % 2017
        print(f"{y}  {value}")
    print("\nMatching Values:\n")
    for y in range(46):
        t_value = (1736 * (5**y)) % 2017
        if t_value in s_values:
            print(f"{s_values[t_value]} {y}")
print_shanks_algorithm()