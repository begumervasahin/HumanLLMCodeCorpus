def fonk1():
    a1 = 2017
    a2 = 5
    a3 = 1736
    a4 = 46
    print("Shank's Algorithm!\n")
    print("S table:\n")
    b1 = {}
    for b5 in range(a4):
        b2 = (a2**(45 * b5)) % a1
        b1[b2] = b5
        print(f"{b5} {b2}")
    print("\nT table:\n")
    b3 = []
    for y in range(a4):
        b4 = (a3 * (a2**y)) % a1
        b3.append((y, b4))
        print(f"{y} {b4}")
    print("\nMatching Values:\n")
    for y, b4 in b3:
        if b4 in b1:
            b5 = b1[b4]
            print(f"{b5} {y}")
fonk1()