import random
def fonk1(length, filename):
    b1 = ["A", "C", "T", "G"]
    b2 = ''.join(random.choice(b1) for _ in range(length))
    with open(filename, "w") as file_txt:
        file_txt.write(b2)
def fonk2(b10, b11):
    b3 = len(b10)
    b4 = len(b11)
    b5 = [[0] * (b4 + 1) for _ in range(b3 + 1)]
    for b8 in range(1, b3 + 1):
        for b9 in range(1, b4 + 1):
            if b10[b8 - 1] == b11[b9 - 1]:
                b5[b8][b9] = b5[b8 - 1][b9 - 1] + 1
            else:
                b5[b8][b9] = max(b5[b8 - 1][b9], b5[b8][b9 - 1])
    b6 = b5[b3][b4]
    b7 = [""] * (b6 + 1)
    b7[b6] = ""
    b8 = b3
    b9 = b4
    while b8 > 0 and b9 > 0:
        if b10[b8 - 1] == b11[b9 - 1]:
            b7[b6 - 1] = b10[b8 - 1]
            b8 -= 1
            b9 -= 1
            b6 -= 1
        elif b5[b8 - 1][b9] > b5[b8][b9 - 1]:
            b8 -= 1
        else:
            b9 -= 1
    print("LCS of b10 and b11 is:", "".join(b7))
    if len(b7) > 500:
        print("Matching")
    else:
        print("Not matching")
fonk1(1000, "dna-b2.txt")
fonk1(1000, "dna-sequence2.txt")
b10 = open("dna-b2.txt", "r").read()
b11 = open("dna-sequence2.txt", "r").read()
fonk2(b10, b11)