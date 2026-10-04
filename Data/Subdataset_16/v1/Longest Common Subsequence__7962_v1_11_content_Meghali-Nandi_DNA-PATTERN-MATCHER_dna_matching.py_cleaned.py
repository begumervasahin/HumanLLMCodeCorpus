import random
def fonk1(length):
    b1 = ["a", "c", "t", "g"]
    b2 = ''.join(random.choice(b1) for _ in range(length))
    with open("dna-sequence.txt", "w") as file_txt:
        file_txt.write(b2)
    with open("dna-sequence2.txt", "w") as file_txt:
        file_txt.write(''.join(random.choice(b1) for _ in range(length)))
def fonk2(b9, b10, b11, b12):
    b3 = [[0 for _ in range(b12+1)] for _ in range(b11+1)]
    for b4 in range(b11+1):
        for b7 in range(b12+1):
            if b4 = = 0 or b7 == 0:
                b3[b4][b7] = 0
            elif b9[b4-1] == b10[b7-1]:
                b3[b4][b7] = b3[b4-1][b7-1] + 1
            else:
                b3[b4][b7] = max(b3[b4-1][b7], b3[b4][b7-1])
    b5 = b3[b11][b12]
    b6 = [""] * (b5+1)
    b6[b5] = ""
    b4 = b11
    b7 = b12
    while b4 > 0 and b7 > 0:
        if b9[b4-1] == b10[b7-1]:
            b6[b5-1] = b9[b4-1]
            b4 -= 1
            b7 -= 1
            b5 -= 1
        elif b3[b4-1][b7] > b3[b4][b7-1]:
            b4 -= 1
        else:
            b7 -= 1
    b8 = "".join(b6)
    print("LCS of " + b9 + " and " + b10 + " is " + b8)
    if len(b8) > 500:
        print("Matching")
    else:
        print("Not matching")
fonk1(1000)
b9 = open("dna-sequence.txt", "r").read()
b10 = open("dna-sequence2.txt", "r").read()
b11 = len(b9)
b12 = len(b10)
fonk2(b9, b10, b11, b12)