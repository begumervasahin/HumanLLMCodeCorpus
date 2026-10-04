def fonk1(n):
    def fonk2(b1, b2, n):
        if b1 = = -1 and b2 == 0:
            return -1
        if b2 = = (b1+1) and b1 < (n
            return fonk2(b1-1, b2-1, n-1) + 4*(n-b2)
        if b1 < (n-b2) and b2 <= b1:
            return fonk2(b2-1, b2, n) + (b1-b2) + 1
        if b1 >= (n-b2) and b2 <= b1:
            return fonk2(b1, b2-1, n) + 1
        if b1 >= (n-b2) and b2 > b1:
            return fonk2(b1+1, b2, n) + 1
        if b1 < (n-b2) and b2 > b1:
            return fonk2(b1, b2-1, n) - 1
    b3 = [[0] * n for j in xrange(n)]
    for b1 in xrange(n):
        for b2 in xrange(n):
            b3[b1][b2] = fonk2(b2, b1, n)
    return b3
for row in fonk1(6):
    print " ".join("%2s" % b1 for b1 in row)