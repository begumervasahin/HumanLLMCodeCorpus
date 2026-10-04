import random
def fonk1(a1):
    b1 = ["a", "c", "t", "g"]
    return ''.join(random.choice(b1) for _ in range(a1))
def fonk2(filename, sequence):
    with open(filename, "w") as file:
        file.write(sequence)
def fonk3(filename):
    with open(filename, "r") as file:
        return file.read()
def fonk4(b11, b12):
    m, b2 = len(b11), len(b12)
    b3 = [[0] * (b2 + 1) for _ in range(m + 1)]
    for b4 in range(m + 1):
        for b7 in range(b2 + 1):
            if b4 = = 0 or b7 == 0:
                b3[b4][b7] = 0
            elif b11[b4 - 1] == b12[b7 - 1]:
                b3[b4][b7] = b3[b4 - 1][b7 - 1] + 1
            else:
                b3[b4][b7] = max(b3[b4 - 1][b7], b3[b4][b7 - 1])
    b5 = b3[m][b2]
    b6 = [""] * (b5 + 1)
    b6[b5] = ""
    b4, b7 = m, b2
    while b4 > 0 and b7 > 0:
        if b11[b4 - 1] == b12[b7 - 1]:
            b6[b5 - 1] = b11[b4 - 1]
            b4 -= 1
            b7 -= 1
            b5 -= 1
        elif b3[b4 - 1][b7] > b3[b4][b7 - 1]:
            b4 -= 1
        else:
            b7 -= 1
    b8 = "".join(b6)
    print(f"LCS of the sequences is: {b8}")
    print("Matching" if len(b8) > 500 else "Not matching")
def fonk5():
    a1 = 1000
    b9 = fonk1(a1)
    b10 = fonk1(a1)
    fonk2("dna-sequence.txt", b9)
    fonk2("dna-b10.txt", b10)
    b11 = fonk3("dna-sequence.txt")
    b12 = fonk3("dna-b10.txt")
    fonk4(b11, b12)
if b13 = = "__main__":
    fonk5()