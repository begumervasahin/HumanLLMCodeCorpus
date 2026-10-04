import random
def fonk1(length):
    b1 = ["a", "c", "t", "g"]
    b2 = ''.join(random.choice(b1) for _ in range(length))
    b3 = ''.join(random.choice(b1) for _ in range(length))
    with open("dna-sequence.txt", "w") as file1:
        file1.write(b2)
    with open("dna-b3.txt", "w") as file2:
        file2.write(b3)
def fonk2(b11, b12):
    m, b4 = len(b11), len(b12)
    b5 = [[0] * (b4 + 1) for _ in range(m + 1)]
    for b6 in range(m + 1):
        for b9 in range(b4 + 1):
            if b6 = = 0 or b9 == 0:
                b5[b6][b9] = 0
            elif b11[b6 - 1] == b12[b9 - 1]:
                b5[b6][b9] = b5[b6 - 1][b9 - 1] + 1
            else:
                b5[b6][b9] = max(b5[b6 - 1][b9], b5[b6][b9 - 1])
    b7 = b5[m][b4]
    b8 = [""] * (b7 + 1)
    b8[b7] = ""
    b6, b9 = m, b4
    while b6 > 0 and b9 > 0:
        if b11[b6 - 1] == b12[b9 - 1]:
            b8[b7 - 1] = b11[b6 - 1]
            b6 -= 1
            b9 -= 1
            b7 -= 1
        elif b5[b6 - 1][b9] > b5[b6][b9 - 1]:
            b6 -= 1
        else:
            b9 -= 1
    b10 = "".join(b8)
    print(f"LCS of the sequences is: {b10}")
    print("Matching" if len(b10) > 500 else "Not matching")
fonk1(1000)
with open("dna-sequence.txt", "r") as file1:
    b11 = file1.read()
with open("dna-b3.txt", "r") as file2:
    b12 = file2.read()
fonk2(b11, b12)