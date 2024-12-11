def fonk1(b4, b5):
    b1 = [[None for _ in range(8)] for _ in range(len(b4))]
    b2 = []
    for b8 in range(0, len(b4)):
        for b9 in range(0, 8):
            if int(b5[b8][b9]) == 1 and int(b4[b8][b9]) == 1:
                b1[b8][b9] = "0"
            if int(b5[b8][b9]) == 1 and int(b4[b8][b9]) == 0:
                b1[b8][b9] = "1"
            if int(b5[b8][b9]) == 0 and int(b4[b8][b9]) == 1:
                b1[b8][b9] = "1"
            if int(b5[b8][b9]) == 0 and int(b4[b8][b9]) == 0:
                b1[b8][b9] = "0"
    for b8 in range(0, len(b4)):
        b3 = ""
        for b9 in range(0, 8):
            b3 = b3 + b1[b8][b9]
        b2.append(b3)
    return b2
def fonk2(b4,b5):
    b4 = list(b4)
    b5 = list(b5)
    b1 = [None]*len(b4)
    b2 = [[None for _ in range(8)] for _ in range(int(len(b1)/8))]
    b6 = []
    b7 = ""
    a1 = 0
    for b8 in range(0, len(b4)):
        if int(b5[b8]) == 1 and int(b4[b8]) == 1:
            b1[b8]="0"
        if int(b5[b8]) == 1 and int(b4[b8]) == 0:
            b1[b8]="1"
        if int(b5[b8]) == 0 and int(b4[b8]) == 1:
            b1[b8]="1"
        if int(b5[b8]) == 0 and int(b4[b8]) == 0:
            b1[b8]="0"
    for b10 in range(0,int(len(b1)/8)):
        b3 = 0
        for b8,b9 in enumerate(b1):
            b2[b10][b3]=b1[b8+a1]
            b3+=1
            if b3 = =8:
                a1+=8
                break
    for b8 in range(0, int(len(b1)/8)):
        b3 = ""
        for b9 in range(0, 8):
            b3 = b3 + b2[b8][b9]
        b6.append(b3)
    for b8 in b6:
        b3 = (int(b8, 2))
        b7 = b7 + chr(b3)
    return b7
def fonk3(mes,pas):
    b8 = mes
    b9 = pas
    b3 = list(b8)
    b10 = list(b9)
    b11 = []
    b12 = []
    for char in b3:
        b13 = ord(char)
        b9 = '{0:08b}'.format(b13)
        b11.append(b9)
    for char in b10:
        b13 = ord(char)
        b9 = '{0:08b}'.format(b13)
        b12.append(b9)
    b14 = fonk1(b11, b12)
    a1 = fonk1(b14, b12)
    b15 = []
    b16 = ''
    for b8 in b14:
        b16+=b8
    for b8 in a1:
        a1 = (int(b8, 2))
    for b8 in b14:
        b14 = (int(b8, 2))
        b15.append(chr(b14))
    return b16