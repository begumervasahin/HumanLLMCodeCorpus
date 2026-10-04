def print_shanks_algorithm():
    print("Shank's Algorithm!\n")
    print("S table:\n")
    for x in range(46):
        s_value = (5**(45 * x)) % 2017
        print(f"{x} {s_value}")
    print("\nT table:\n")
    for y in range(46):
        t_value = (1736 * (5**y)) % 2017
        print(f"{y} {t_value}")
    print("\nMatching Values:\n")
    for x in range(46):
        s_value = (5**(45 * x)) % 2017
        for y in range(46):
            t_value = (1736 * (5**y)) % 2017
            if s_value == t_value:
                print(f"{x} {y}")
print_shanks_algorithm()