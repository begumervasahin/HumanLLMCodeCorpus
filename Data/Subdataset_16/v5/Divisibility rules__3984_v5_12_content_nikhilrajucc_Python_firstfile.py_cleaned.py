def fonk1(b1 = "input.txt"):
    with open(b1, 'r') as file:
        b2 = file.read().split()
    b3 = int(b2[0])
    b4 = int(b2[1])
    b5 = int(b2[2])
    for i in range(1, b5 + 1):
        if i % b3 = = 0 and i % b4 == 0:
            print("FB")
        elif i % b3 = = 0:
            print("F")
        elif i % b4 = = 0:
            print("B")
        else:
            print(i)
fonk1("input.txt")