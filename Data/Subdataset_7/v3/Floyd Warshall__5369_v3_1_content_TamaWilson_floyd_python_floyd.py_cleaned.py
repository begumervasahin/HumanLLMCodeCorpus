b1 = float("inf")
b2 = [
    [0, 5, b1, 10],
    [b1, 0, 3, b1],
    [b1, b1, 0, 1],
    [b1, b1, b1, 0]
]
def fonk1(b2):
    b3 = len(b2)
    for k in range(b3):
        for i in range(b3):
            for j in range(b3):
                b2[i][j] = min(b2[i][j], b2[i][k] + b2[k][j])
    print("Shortest paths in the b2:")
    for row in b2:
        print("\t".join(str(item) for item in row))
if b4 = = "__main__":
    fonk1(b2)