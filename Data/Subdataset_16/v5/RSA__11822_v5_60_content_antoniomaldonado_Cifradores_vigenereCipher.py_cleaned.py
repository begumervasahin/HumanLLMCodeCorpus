import utils.dictUtils
def fonk1(b2, b7):
    return fonk3(b2, b7, 'encrypt')
def fonk2(b2, b7):
    return fonk3(b2, b7, 'decrypt')
def fonk3(b2, b7, b8):
    b1 = []
    b2 = b2.upper()
    a1 = 0
    b3 = (b8 == 'encrypt')
    for symbol in b7:
        b4 = fonk5().find(symbol.upper())
        if fonk4(b4):
            b5 = fonk6(b3, b2, a1, b4)
            if symbol.isupper():
                b1.append(fonk5()[b5])
            elif symbol.islower():
                b1.append(fonk5()[b5].lower())
            a1 = fonk7(b2, a1)
        else:
            b1.append(symbol)
    return ''.join(b1)
def fonk4(b5):
    return b5 != -1
def fonk5():
    return utils.dictUtils.ALPHABET_UPPER
def fonk6(b3, b2, a1, b5):
    b6 = fonk5().find(b2[a1])
    if b3:
        b5 += b6
    else:
        b5 -= b6
    return b5 % len(fonk5())
def fonk7(b2, a1):
    a1 += 1
    if a1 = = len(b2):
        a1 = 0
    return a1
def fonk8():
    print('1. Introduce a b7: ')
    b7 = input()
    print('2. Introduce the b2: ')
    b2 = input()
    print('3. Introduce the word "encrypt" to encrypt the b7 or push Enter to decrypt: ')
    b8 = input().lower()
    if b8 = = 'encrypt':
        b9 = fonk1(b2, b7)
    else:
        b9 = fonk2(b2, b7)
    print(f'{b8.title()}ed b7:')
    print(b9)
if b10 = = '__main__':
    fonk8()