def fonk1():
    print("Shank's Algorithm!\n")
    print("\n\nS table\n")
    for x in range(0, 46):
        b1 = (5**(45 * x)) % 2017
        print(f"{x} {b1}\n")
    print("\n\nT table\n")
    for y in range(0, 46):
        b1 = (1736 * (5**y)) % 2017
        print(f"{y}  {b1}\n")
    print("\n\nMatching Values\n")
    b2 = {}
    for x in range(0, 46):
        b3 = (5**(45 * x)) % 2017
        b2[b3] = x
    for y in range(0, 46):
        b4 = (1736 * (5**y)) % 2017
        if b4 in b2:
            print(f"{b2[b4]} {y}\n")
fonk1()