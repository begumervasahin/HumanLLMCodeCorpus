b1 = float("inf")
b2 = [  [0, 5, b1, 10],
            [b1, 0, 3, b1],
            [b1, b1, 0,   1],
            [b1, b1, b1, 0]
        ]
def fonk1(b2):
    b3 = b2
    b4 = len(b2)
    for k in range(b4):
        for i in range(b4):
            for j in range(b4):
                b3[i][j] = min(b3[i][j], b3[i][k] + b3[k][j])
    for itens in b3:
        print("")
        for item in itens:
            print("%s\t" % item, b5 = "")