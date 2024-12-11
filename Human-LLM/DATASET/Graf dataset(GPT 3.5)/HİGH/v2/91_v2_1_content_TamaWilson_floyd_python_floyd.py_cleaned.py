b1 = float("inf")
b2 = [
    [0, 5, b1, 10],
    [b1, 0, 3, b1],
    [b1, b1, 0, 1],
    [b1, b1, b1, 0]
]
def fonk1(b2):
    b3 = b2
    b4 = len(b2)
    for k in range(b4):
        for i in range(b4):
            for j in range(b4):
                b3[i][j] = min(b3[i][j], b3[i][k] + b3[k][j])
    for row in b3:
        print("")
        for item in row:
            print("%s\t" % item, b5 = "")
if b6 = = "__main__":
    print("Shortest paths in the b2:")
    fonk1(b2)