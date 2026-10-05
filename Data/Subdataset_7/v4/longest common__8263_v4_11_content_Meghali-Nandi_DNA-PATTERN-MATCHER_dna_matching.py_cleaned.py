import random
def fonk1(length):
    b1 = ["a", "c", "t", "g"]
    return ''.join(random.choice(b1) for _ in range(length))
def fonk2(sequence, filename):
    with open(filename, "a") as file_txt:
        file_txt.write(sequence)
def fonk3(b9, b10):
    m, b2 = len(b9), len(b10)
    b3 = [[0 for _ in range(b2 + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for b6 in range(1, b2 + 1):
            if b9[i - 1] == b10[b6 - 1]:
                b3[i][b6] = b3[i - 1][b6 - 1] + 1
            else:
                b3[i][b6] = max(b3[i - 1][b6], b3[i][b6 - 1])
    b4 = b3[m][b2]
    b5 = [""] * (b4 + 1)
    i, b6 = m, b2
    while i > 0 and b6 > 0:
        if b9[i - 1] == b10[b6 - 1]:
            b5[b4 - 1] = b9[i - 1]
            i -= 1
            b6 -= 1
            b4 -= 1
        elif b3[i - 1][b6] > b3[i][b6 - 1]:
            i -= 1
        else:
            b6 -= 1
    print("Longest Common Subsequence of b9 and b10 is:", "".join(b5))
    if len(b5) > 500:
        print("Matching")
    else:
        print("Not matching")
b7 = fonk1(1000)
b8 = fonk1(1000)
fonk2(b7, "dna-sequence.txt")
fonk2(b8, "dna-b8.txt")
b9 = open("dna-sequence.txt", "r").read()
b10 = open("dna-b8.txt", "r").read()
fonk3(b9, b10)