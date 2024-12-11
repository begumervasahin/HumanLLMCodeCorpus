def fonk1():
    b1 = {}
    b2 = {}
    b1[' '] = 0
    b2[0] = ' '
    for i in range(65, 91):
        b1[chr(i)] = i - 64
        b2[i - 64] = chr(i)
    b1[','] = 27
    b1['.'] = 28
    b1['?'] = 29
    b2[27] = ','
    b2[28] = '.'
    b2[29] = '?'
    for i in range(48, 58):
        b1[chr(i)] = i - 18
        b2[i - 18] = chr(i)
    for i in range(97, 123):
        b1[chr(i)] = i - 57
        b2[i - 57] = chr(i)
    b1['!'] = 66
    b2[66] = '!'
    return b1, b2
def fonk2(string, a1):
    b1, b2 = fonk1()
    b3 = ""
    for char in string:
        b4 = b1.get(char)
        if b4 is None:
            return -1
        else:
            b5 = (b4 + a1) % 67
            b3 += b2[b5]
    return b3
def fonk3(string, a1):
    b1, b2 = fonk1()
    b6 = ""
    for char in string:
        b4 = b1.get(char)
        if b4 is None:
            return -1
        else:
            b7 = (b4 - a1) % 67
            b6 += b2[b7 % 67]
    return b6
if b8 = = "__main__":
    b9 = "Hello, World!"
    a1 = 5
    b10 = fonk2(b9, a1)
    print("Encrypted b9:", b10)
    b11 = fonk3(b10, a1)
    print("Decrypted b9:", b11)