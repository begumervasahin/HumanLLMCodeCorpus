def fonk1():
    print("Shank's Algorithm!\n")
    print("S table:\n")
    b1 = {}
    for x in range(46):
        b2 = (5**(45 * x)) % 2017
        b1[b2] = x
        print(f"{x} {b2}")
    print("\nT table:\n")
    for y in range(46):
        b2 = (1736 * (5**y)) % 2017
        print(f"{y}  {b2}")
    print("\nMatching Values:\n")
    for y in range(46):
        b3 = (1736 * (5**y)) % 2017
        if b3 in b1:
            print(f"{b1[b3]} {y}")
fonk1()