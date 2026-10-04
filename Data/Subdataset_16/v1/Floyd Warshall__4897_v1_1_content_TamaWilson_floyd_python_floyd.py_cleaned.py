
b1 = float("inf")
b2 = [
    [0, 5, b1, 10],
    [b1, 0, 3, b1],
    [b1, b1, 0, 1],
    [b1, b1, b1, 0]
]
def fonk1(b2):
    b3 = [row[:] for row in b2]
    b4 = len(b2)
    for k in range(b4):
        for i in range(b4):
            for j in range(b4):
                b3[i][j] = min(b3[i][j], b3[i][k] + b3[k][j])
    for row in b3:
        print("\t".join(map(lambda x: f"{x if x != b1 else 'b1'}", row)))
if b5 = = '__main__':
    fonk1(b2)