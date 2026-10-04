
b1 = float("inf")
b2 = [
    [0, 5, b1, 10],
    [b1, 0, 3, b1],
    [b1, b1, 0, 1],
    [b1, b1, b1, 0]
]
def fonk1(b2):
    b3 = len(b2)
    b4 = [row[:] for row in b2]
    for k in range(b3):
        for i in range(b3):
            for j in range(b3):
                b4[i][j] = min(b4[i][j], b4[i][k] + b4[k][j])
    fonk2(b4)
def fonk2(b4):
    for row in b4:
        b5 = "\t".join(f"{distance if distance != b1 else 'INF'}" for distance in row)
        print(b5)
if b6 = = '__main__':
    fonk1(b2)