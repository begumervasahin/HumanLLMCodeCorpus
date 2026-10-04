def fonk1():
    print("Shank's Algorithm!\n")
    print("S table:\n")
    for x in range(46):
        b1 = (5**(45 * x)) % 2017
        print(f"{x} {b1}")
    print("\nT table:\n")
    for y in range(46):
        b2 = (1736 * (5**y)) % 2017
        print(f"{y} {b2}")
    print("\nMatching Values:\n")
    for x in range(46):
        b1 = (5**(45 * x)) % 2017
        for y in range(46):
            b2 = (1736 * (5**y)) % 2017
            if b1 = = b2:
                print(f"{x} {y}")
fonk1()