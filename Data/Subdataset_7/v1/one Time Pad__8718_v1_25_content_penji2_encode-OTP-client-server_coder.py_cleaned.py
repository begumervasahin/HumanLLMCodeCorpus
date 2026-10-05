def fonk1(bitlist, b16):
    b1 = [[None for _ in range(8)] for _ in range(len(bitlist))]
    b2 = []
    for b6 in range(len(bitlist)):
        for b7 in range(8):
            if int(b16[b6][b7]) == 1 and int(bitlist[b6][b7]) == 1:
                b1[b6][b7] = "0"
            elif int(b16[b6][b7]) == 1 and int(bitlist[b6][b7]) == 0:
                b1[b6][b7] = "1"
            elif int(b16[b6][b7]) == 0 and int(bitlist[b6][b7]) == 1:
                b1[b6][b7] = "1"
            elif int(b16[b6][b7]) == 0 and int(bitlist[b6][b7]) == 0:
                b1[b6][b7] = "0"
    for b6 in range(len(bitlist)):
        b3 = ""
        for b7 in range(8):
            b3 += b1[b6][b7]
        b2.append(b3)
    return b2
def fonk2(bitlist, b16):
    b1 = [None] * len(bitlist)
    b2 = [[None for _ in range(8)] for _ in range(int(len(b1) / 8))]
    b4 = []
    b5 = ""
    a1 = 0
    for b6 in range(len(bitlist)):
        if int(b16[b6]) == 1 and int(bitlist[b6]) == 1:
            b1[b6] = "0"
        elif int(b16[b6]) == 1 and int(bitlist[b6]) == 0:
            b1[b6] = "1"
        elif int(b16[b6]) == 0 and int(bitlist[b6]) == 1:
            b1[b6] = "1"
        elif int(b16[b6]) == 0 and int(bitlist[b6]) == 0:
            b1[b6] = "0"
    for b8 in range(int(len(b1) / 8)):
        b3 = 0
        for b6, b7 in enumerate(b1):
            b2[b8][b3] = b1[b6 + a1]
            b3 += 1
            if b3 = = 8:
                a1 += 8
                break
    for b6 in range(int(len(b1) / 8)):
        b3 = ""
        for b7 in range(8):
            b3 += b2[b6][b7]
        b4.append(b3)
    for b6 in b4:
        b3 = int(b6, 2)
        b5 += chr(b3)
    return b5
def fonk3(mes, pas):
    b6 = mes
    b7 = pas
    b3 = list(b6)
    b8 = list(b7)
    b9 = []
    b10 = []
    for char in b3:
        b11 = ord(char)
        b7 = '{0:08b}'.format(b11)
        b9.append(b7)
    for char in b8:
        b11 = ord(char)
        b7 = '{0:08b}'.format(b11)
        b10.append(b7)
    b12 = fonk1(b9, b10)
    a1 = fonk1(b12, b10)
    b13 = ""
    for b6 in a1:
        a1 = int(b6, 2)
        b13 += chr(a1)
    return b13
if b14 = = "__main__":
    b15 = "Hello"
    b16 = "Password"
    b17 = fonk3(b15, b16)
    print("Encrypted b15:", b17)