def fonk1(b1 = "input.txt"):
    with open(b1, 'r') as file:
        b2 = file.readlines()
    b4, b5, b3 = map(int, b2[0].split())
    for i in range(1, b3 + 1):
        if i % b4 = = 0 and i % b5 == 0:
            print("FB")
        elif i % b4 = = 0:
            print("F")
        elif i % b5 = = 0:
            print("B")
        else:
            print(i)
fonk1()