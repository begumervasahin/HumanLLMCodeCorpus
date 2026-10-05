def fonk1(b1 = "input.txt"):
    with open(b1, 'r') as file:
        b2 = file.readlines()
    b4, b5, b3 = map(int, b2[0].split())
    a1 = 1
    while a1 < b3:
        if a1 % b4 = = 0 and a1 % b5 == 0:
            print("FB")
        elif a1 % b4 = = 0:
            print("F")
        elif a1 % b5 = = 0:
            print("B")
        else:
            print(a1)
        a1 += 1
fonk1()