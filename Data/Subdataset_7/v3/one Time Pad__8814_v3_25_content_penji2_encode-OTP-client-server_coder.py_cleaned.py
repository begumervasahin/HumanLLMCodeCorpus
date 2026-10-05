def fonk1(bitlist, b15):
    b1 = []
    for i in range(len(bitlist)):
        b2 = ""
        for j in range(8):
            b3 = int(b15[i][j])
            b4 = int(bitlist[i][j])
            b5 = b3 ^ b4
            b2 += str(b5)
        b1.append(b2)
    return b1
def fonk2(bitlist, b15):
    b6 = []
    for i in range(len(bitlist)):
        b3 = int(b15[i])
        b4 = int(bitlist[i])
        b7 = b3 ^ b4
        b6.append(str(b7))
    return b6
def fonk3(bitlist):
    b8 = []
    for i in range(int(len(bitlist) / 8)):
        b9 = "".join(bitlist[i * 8: i * 8 + 8])
        b8.append(b9)
    return b8
def fonk4(b14, b15):
    b10 = [format(ord(char), '08b') for char in b14]
    b11 = [format(ord(char), '08b') for char in b15]
    b1 = fonk1(b10, b11)
    b1 = fonk1(b1, b11)
    b12 = "".join([chr(int(char, 2)) for char in b1])
    return b12
if b13 = = "__main__":
    b14 = "Hello"
    b15 = "Password"
    b12 = fonk4(b14, b15)
    print("Encrypted b14:", b12)