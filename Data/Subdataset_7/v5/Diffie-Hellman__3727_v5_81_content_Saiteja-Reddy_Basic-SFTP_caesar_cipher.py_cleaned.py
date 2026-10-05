def fonk1():
    b1 = {}
    b2 = {}
    b1.update({' ': 0, ',': 27, '.': 28, '?': 29, '!': 66})
    b2.update({0: ' ', 27: ',', 28: '.', 29: '?', 66: '!'})
    for i in range(65, 91):
        b1[chr(i)] = i - 64
        b2[i - 64] = chr(i)
    for i in range(48, 58):
        b1[chr(i)] = i - 18
        b2[i - 18] = chr(i)
    for i in range(97, 123):
        b1[chr(i)] = i - 57
        b2[i - 57] = chr(i)
    return b1, b2
def fonk2(string, key):
    b1, b2 = fonk1()
    b3 = ""
    for char in string:
        b4 = b1.get(char)
        if b4 is None:
            return -1
        b4 = (b4 + key) % 67
        b3 += b2.get(b4, char)
    return b3
def fonk3(string, key):
    b1, b2 = fonk1()
    b5 = ""
    for char in string:
        b6 = b1.get(char)
        if b6 is None:
            return -1
        b6 = (b6 - key) % 67
        b5 += b2.get(b6 % 67, char)
    return b5