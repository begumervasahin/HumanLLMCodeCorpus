def fonk1(letter, b4):
    b1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    b2 = (b1.index(letter) + b4) % 26
    return b1[b2]
def fonk2(key, text):
    b3 = ''
    a1 = 0
    for letter in text:
        b4 = ord(key[a1]) - ord('A')
        b3 += fonk1(letter.upper(), b4)
        a1 = (a1 + 1) % len(key)
    return b3
def fonk3(key, numeric):
    b5 = []
    a1 = 0
    for digit in numeric:
        b4 = int(key[a1])
        b6 = (int(digit) + b4) % 10
        b5.append(str(b6))
        a1 = (a1 + 1) % len(key)
    return b5
print(fonk2("EVXLL", "MONTH"))
print(fonk3("6", "6"))