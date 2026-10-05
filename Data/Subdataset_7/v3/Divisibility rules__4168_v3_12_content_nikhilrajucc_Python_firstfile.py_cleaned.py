def fonk1(b1 = "input.txt"):
    with open(b1, 'r') as file:
        b3, b4, b2 = map(int, file.readline().split())
    for i in range(1, b2 + 1):
        if i % b3 = = 0 and i % b4 == 0:
            print("FB")
        elif i % b3 = = 0:
            print("F")
        elif i % b4 = = 0:
            print("B")
        else:
            print(i)
fonk1()