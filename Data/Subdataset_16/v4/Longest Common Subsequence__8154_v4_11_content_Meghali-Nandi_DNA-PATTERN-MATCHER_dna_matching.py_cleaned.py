import random
def fonk1(a1, filename):
    b1 = ["a", "c", "t", "g"]
    b2 = ''.join(random.choice(b1) for _ in range(a1))
    with open(filename, "a") as file:
        file.write(b2)
def fonk2(b10, b11):
    b3 = len(b10)
    b4 = len(b11)
    b5 = [[0 for _ in range(b4+1)] for _ in range(b3+1)]
    for b6 in range(b3+1):
        for b9 in range(b4+1):
            if b6 = = 0 or b9 == 0:
                b5[b6][b9] = 0
            elif b10[b6-1] == b11[b9-1]:
                b5[b6][b9] = b5[b6-1][b9-1] + 1
            else:
                b5[b6][b9] = max(b5[b6-1][b9], b5[b6][b9-1])
    b7 = b5[b3][b4]
    b8 = [""] * (b7+1)
    b8[b7] = ""
    b6 = b3
    b9 = b4
    while b6 > 0 and b9 > 0:
        if b10[b6-1] == b11[b9-1]:
            b8[b7-1] = b10[b6-1]
            b6 -= 1
            b9 -= 1
            b7 -= 1
        elif b5[b6-1][b9] > b5[b6][b9-1]:
            b6 -= 1
        else:
            b9 -= 1
    return "".join(b8)
def fonk3():
    a1 = 1000
    fonk1(a1, "dna-b2.txt")
    fonk1(a1, "dna-sequence2.txt")
    b10 = open("dna-b2.txt", "r").read()
    b11 = open("dna-sequence2.txt", "r").read()
    b12 = fonk2(b10, b11)
    print(f"LCS of the DNA sequences is {b12}")
    if len(b12) > 500:
        print("Matching")
    else:
        print("Not matching")
if b13 = = "__main__":
    fonk3()