def fonk1(bitlist, b12):
    b1 = []
    for i in range(len(bitlist)):
        b2 = ""
        for j in range(8):
            if int(b12[i][j]) == 1 and int(bitlist[i][j]) == 1:
                b2 += "0"
            elif int(b12[i][j]) == 1 and int(bitlist[i][j]) == 0:
                b2 += "1"
            elif int(b12[i][j]) == 0 and int(bitlist[i][j]) == 1:
                b2 += "1"
            elif int(b12[i][j]) == 0 and int(bitlist[i][j]) == 0:
                b2 += "0"
        b1.append(b2)
    return b1
def fonk2(bitlist, b12):
    b3 = []
    for i in range(len(bitlist)):
        if int(b12[i]) == 1 and int(bitlist[i]) == 1:
            b3.append("0")
        elif int(b12[i]) == 1 and int(bitlist[i]) == 0:
            b3.append("1")
        elif int(b12[i]) == 0 and int(bitlist[i]) == 1:
            b3.append("1")
        elif int(b12[i]) == 0 and int(bitlist[i]) == 0:
            b3.append("0")
    return b3
def fonk3(bitlist):
    b4 = []
    for i in range(int(len(bitlist) / 8)):
        b5 = ""
        for j in range(8):
            b5 += bitlist[i * 8 + j]
        b4.append(b5)
    return b4
def fonk4(b11, b12):
    b6 = [format(ord(char), '08b') for char in b11]
    b7 = [format(ord(char), '08b') for char in b12]
    b1 = fonk1(b6, b7)
    b1 = fonk1(b1, b7)
    b8 = ""
    for b2 in b1:
        b9 = int(b2, 2)
        b8 += chr(b9)
    return b8
if b10 = = "__main__":
    b11 = "Hello"
    b12 = "Password"
    b8 = fonk4(b11, b12)
    print("Encrypted b11:", b8)