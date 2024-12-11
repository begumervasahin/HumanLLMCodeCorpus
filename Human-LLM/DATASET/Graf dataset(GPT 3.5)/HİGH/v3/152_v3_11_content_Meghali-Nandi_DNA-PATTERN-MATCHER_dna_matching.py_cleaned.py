import random
def fonk1(length, filename):
    b1 = ["A", "C", "T", "G"]
    b2 = ''.join(random.choice(b1) for _ in range(length))
    with open(filename, "w") as file_txt:
        file_txt.write(b2)
def fonk2(b7, b8):
    m, b3 = len(b7), len(b8)
    b4 = [[0] * (b3 + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for b6 in range(1, b3 + 1):
            if b7[i - 1] == b8[b6 - 1]:
                b4[i][b6] = b4[i - 1][b6 - 1] + 1
            else:
                b4[i][b6] = max(b4[i - 1][b6], b4[i][b6 - 1])
    b5 = []
    i, b6 = m, b3
    while i > 0 and b6 > 0:
        if b7[i - 1] == b8[b6 - 1]:
            b5.append(b7[i - 1])
            i -= 1
            b6 -= 1
        elif b4[i - 1][b6] > b4[i][b6 - 1]:
            i -= 1
        else:
            b6 -= 1
    print("Longest Common Subsequence of b7 and b8 is:", "".join(reversed(b5)))
    if len(b5) > 500:
        print("Matching")
    else:
        print("Not matching")
fonk1(1000, "dna-b2.txt")
fonk1(1000, "dna-sequence2.txt")
b7 = open("dna-b2.txt", "r").read()
b8 = open("dna-sequence2.txt", "r").read()
fonk2(b7, b8)