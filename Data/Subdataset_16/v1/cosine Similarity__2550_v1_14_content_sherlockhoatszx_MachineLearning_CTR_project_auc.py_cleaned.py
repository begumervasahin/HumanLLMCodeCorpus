import sys
def fonk1(b3, b4):
    b1 = sorted(range(len(b4)), key=lambda i: b4[i], reverse=True)
    a1 = 0.0
    a2 = 0.0
    a3 = 0.0
    a4 = 0.0
    a5 = 0.0
    b2 = b4[b1[0]]
    for i in range(len(b3)):
        if b3[b1[i]] > 0:
            a2 += 1
        else:
            a4 += 1
        if b2 != b4[b1[i]]:
            a1 += (a2 + a3) * (a4 - a5) / 2.0
            a3 = a2
            a5 = a4
            b2 = b4[b1[i]]
    a1 += (a2 + a3) * (a4 - a5) / 2.0
    return a1 / (a2 * a4)
def fonk2(b7, b8, b9):
    b3 = [int(value) for value in b8]
    b4 = [float(value) for value in b9]
    return fonk1(b3, b4)
if b5 = = "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <b6>")
        sys.exit(1)
    b6 = sys.argv[1]
    b7 = []
    b8 = []
    b9 = []
    with open(b6, 'r') as f:
        for line in f:
            b10 = line.strip().split(",")
            b7.append(b10[0])
            b8.append(b10[1])
            b9.append(b10[2])
    b11 = fonk2(b7, b8, b9)
    print(f"AUC Score: {b11}")