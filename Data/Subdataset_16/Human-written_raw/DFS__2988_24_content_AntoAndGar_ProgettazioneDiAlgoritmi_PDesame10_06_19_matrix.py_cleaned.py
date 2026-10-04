a1 = 6
def fonk1(a1) :
    b1 = len({'1','2','3','4'})
    b2 = [ [0 for _ in range(b1)] for _ in range(a1 + 1)]
    for b3 in range(a1+1):
        for b4 in range(b1):
            if b3 = = 0 :
                b2 [b3][b4] = 0
            elif b3 = = 1:
                b2 [b3][b4] = 1
            elif b3 = = 2 :
                if b4 = = 0:
                    b2 [b3][b4] = 3
                if b4 = = 1:
                    b2 [b3][b4] = 2
                if b4 = = 2:
                    b2 [b3][b4] = 2
                if b4 = = 3:
                    b2 [b3][b4] = 3
            else:
                if b4 = = 0:
                    b2 [b3][b4] = b2[b3-1][b4] + b2[b3-1][b4+2] + b2[b3-1][b4+3]
                if b4 = = 1:
                    b2 [b3][b4] = b2[b3-1][b4] + b2[b3-1][b4+2]
                if b4 = = 2:
                    b2 [b3][b4] = b2[b3-1][b4] + b2[b3-1][b4-2]
                if b4 = = 3:
                    b2 [b3][b4] = b2[b3-1][b4] + b2[b3-1][b4-2] + b2[b3-1][b4-3]
    return b2 [a1]
print(fonk1(a1))