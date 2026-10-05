
def fonk1(b12, key):
    b1 = ''
    for char in b12:
        b2 = ord(char) + int(key)
        if b2 - int(key) == 32:
            b2 = 32
        elif b2 > ord('z'):
            b2 -= 26
        elif b2 < ord('a'):
            b2 += 26
        b3 = chr(b2)
        b1 += b3
    print(b1)
    return b1
def fonk2(b9, key):
    b4 = ''
    for char in b9:
        b2 = ord(char) - int(key)
        if b2 + int(key) == 32:
            b2 = 32
        elif b2 > ord('z'):
            b2 -= 26
        elif b2 < ord('a'):
            b2 += 26
        b5 = chr(b2)
        b4 += b5
    return b4
def fonk3(b12, key):
    b6 = len(key)
    b7 = [ord(char) for char in key]
    b8 = [ord(char) for char in b12]
    b9 = ''
    for i in range(len(b8)):
        b10 = (b8[i] + b7[i % b6]) % 26
        b9 += chr(b10 + 65)
    return b9
def fonk4(b9, key):
    b6 = len(key)
    b7 = [ord(char) for char in key]
    b11 = [ord(char) for char in b9]
    b12 = ''
    for i in range(len(b11)):
        b10 = (b11[i] - b7[i % b6]) % 26
        b12 += chr(b10 + 65)
    return b12