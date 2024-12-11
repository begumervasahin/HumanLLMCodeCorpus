def fonk1(H,b4,i):
    b1 = i
    b2 = 2 * i + 1
    b3 = 2 * i + 2
    if b2 < b4 and H[i] > H[b2]:
        b1 = b2
    if b3 < b4 and H[b1] > H[b3]:
        b1 = b3
    if b1 != i:
        H[i], H[b1] = H[b1], H[i]
        fonk1(H, b4, b1)
def fonk2(H):
    b4 = len(H)
    for i in range(b4, -1, -1):
        fonk1(H, b4, i)
    for i in range(b4 - 1, 0, -1):
        H[i], H[0] = H[0], H[i]
        fonk1(H, i, 0)