def fonk1(a2):
    a1 = 4
    b1 = [[0] * a1 for _ in range(a2 + 1)]
    for y in range(a1):
        if a2 >= 0:
            b1[0][y] = 0
        if a2 >= 1:
            b1[1][y] = 1
        if a2 >= 2:
            b1[2][0] = 3
            b1[2][1] = 2
            b1[2][2] = 2
            b1[2][3] = 3
    for x in range(3, a2 + 1):
        b1[x][0] = b1[x-1][0] + b1[x-1][2] + b1[x-1][3]
        b1[x][1] = b1[x-1][1] + b1[x-1][2]
        b1[x][2] = b1[x-1][2] + b1[x-1][0]
        b1[x][3] = b1[x-1][3] + b1[x-1][0] + b1[x-1][1]
    return b1[a2]
if b2 = = "__main__":
    a2 = 6
    b3 = fonk1(a2)
    print(f"The values in the sequence at a2 = {a2} are: {b3}")