def fonk1(bitlist, b6):
    b1 = []
    for i in range(len(bitlist)):
        b2 = ''
        for j in range(8):
            if int(b6[i][j]) == 1 and int(bitlist[i][j]) == 1:
                b2 += '0'
            elif int(b6[i][j]) == 1 and int(bitlist[i][j]) == 0:
                b2 += '1'
            elif int(b6[i][j]) == 0 and int(bitlist[i][j]) == 1:
                b2 += '1'
            else:
                b2 += '0'
        b1.append(b2)
    return b1
def fonk2(bitlist, b6):
    b1 = []
    for i in range(len(bitlist)):
        if int(b6[i]) == 1 and int(bitlist[i]) == 1:
            b1.append("0")
        elif int(b6[i]) == 1 and int(bitlist[i]) == 0:
            b1.append("1")
        elif int(b6[i]) == 0 and int(bitlist[i]) == 1:
            b1.append("1")
        else:
            b1.append("0")
    b3 = []
    for i in range(0, len(b1), 8):
        b3.append(b1[i:i+8])
    b4 = ''
    for byte in b3:
        b4 += chr(int(''.join(byte), 2))
    return b4
def fonk3(mes, pas):
    b5 = mes
    b6 = pas
    b7 = [format(ord(char), '08b') for char in b5]
    b8 = [format(ord(char), '08b') for char in b6]
    b9 = fonk1(b7, b8)
    b10 = fonk1(b9, b8)
    return ''.join(b10)