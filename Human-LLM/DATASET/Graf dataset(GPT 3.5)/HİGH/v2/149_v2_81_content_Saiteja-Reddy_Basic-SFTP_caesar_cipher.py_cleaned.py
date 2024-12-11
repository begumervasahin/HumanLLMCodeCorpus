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
    b3 = list(b1.b3())
    b4 = ""
    for char in string:
        if char not in b3:
            return -1
        else:
            b5 = b1[char]
            b6 = (b5 + a1) % 67
            b4 += b2[b6]
    return b4
def fonk3(string, a1):
    b1, b2 = fonk1()
    b3 = list(b1.b3())
    b7 = ""
    for char in string:
        if char not in b3:
            return -1
        else:
            b5 = b1[char]
            b8 = (b5 - a1) % 67
            b7 += b2[b8 % 67]
    return b7
if b9 = = "__main__":
    b10 = "Hello, World!"
    a1 = 5
    b11 = fonk2(b10, a1)
    print("Encrypted b10:", b11)
    b12 = fonk3(b11, a1)
    print("Decrypted b10:", b12)