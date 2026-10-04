def fonk1(a2):
    a1 = 4
    b1 = [[0 for _ in range(a1)] for _ in range(a2 + 1)]
    for b2 in range(a2 + 1):
        for b3 in range(a1):
            if b2 = = 0:
                b1[b2][b3] = 0
            elif b2 = = 1:
                b1[b2][b3] = 1
            elif b2 = = 2:
                b1[b2][0] = 3
                b1[b2][1] = 2
                b1[b2][2] = 2
                b1[b2][3] = 3
            else:
                if b3 = = 0:
                    b1[b2][b3] = b1[b2-1][b3] + b1[b2-1][b3+2] + b1[b2-1][b3+3]
                elif b3 = = 1:
                    b1[b2][b3] = b1[b2-1][b3] + b1[b2-1][b3+2]
                elif b3 = = 2:
                    b1[b2][b3] = b1[b2-1][b3] + b1[b2-1][b3-2]
                elif b3 = = 3:
                    b1[b2][b3] = b1[b2-1][b3] + b1[b2-1][b3-2] + b1[b2-1][b3-3]
    return b1[a2]
if b4 = = "__main__":
    a2 = 6
    b5 = fonk1(a2)
    print(f"The values in the sequence at a2 = {a2} are: {b5}")