def fonk1(b12):
    if len(b12) < 2:
        return b12
    b1 = [None for _ in range(len(b12))]
    b2 = [None for _ in range(len(b12))]
    a1 = 1
    b1[0] = 0
    b3 = []
    for i in range(1, len(b12)):
        if b12[i] > b12[b1[a1-1]]:
            b4 = a1
        else:
            a2 = 0
            b5 = a1 - 1
            while a2 + 1 < b5:
                b6 = (a2 + b5)
                if b12[i] > b12[b1[b6]]:
                    a2 = b6 + 1
                else:
                    b5 = b6
            b4 = a2
        b2[i] = b1[b4-1]
        b1[b4] = i
        a1 = max(a1, b4 + 1)
    b7 = b1[a1-1]
    for _ in range(a1):
        b3.append(b12[b7])
        b7 = b2[b7]
    return b3[::-1]
def fonk2(b12):
    b8 = [[] for _ in range(len(b12))]
    b9 = []
    for i in range(len(b12)):
        b10 = False
        for b4 in range(i):
            if b12[i] > b8[b4][-1]:
                b10 = True
                b8[i] = b8[b4] + [b12[i]]
                b9 = max(b8[i], b9, key=len)
        if b10 is False:
            b8[i].append(b12[i])
    return b9
if b11 = = "__main__":
    b12 = [30, 10, 20, 50, 40, 60]
    print("Longest increasing subsequence using O(n log n) approach:")
    print(fonk1(b12))
    print("\nLongest increasing subsequence using O(n^2) approach:")
    print(fonk2([80, 90, 91, 81, 82, 83, 74, 85]))