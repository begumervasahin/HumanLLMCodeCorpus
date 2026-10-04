import utils.dictUtils
def fonk1(b2, b6):
    return fonk3(b2, b6, 'encrypt')
def fonk2(b2, b6):
    return fonk3(b2, b6, 'decrypt')
def fonk3(b2, b6, b7):
    b1 = []
    b2 = b2.upper()
    a1 = 0
    b3 = b7 == 'encrypt'
    for symbol in b6:
        b4 = fonk5().find(symbol.upper())
        if fonk4(b4):
            b4 = fonk6(b3, b2, a1, b4)
            if symbol.isupper():
                b1.append(fonk5()[b4])
            elif symbol.islower():
                b1.append(fonk5()[b4].lower())
            a1 = fonk7(b2, a1)
        else:
            b1.append(symbol)
    return ''.join(b1)
def fonk4(b4):
    return b4 != -1
def fonk5():
    return utils.dictUtils.ALPHABET_UPPER
def fonk6(b3, b2, a1, b4):
    b5 = fonk5().find(b2[a1])
    if b3:
        b4 += b5
    else:
        b4 -= b5
    b4 %= len(fonk5())
    return b4
def fonk7(b2, a1):
    a1 += 1
    if a1 = = len(b2):
        a1 = 0
    return a1
def fonk8():
    print('1. Introduce a b6: ')
    b6 = input()
    print('2. Introduce the b2: ')
    b2 = input()
    print('3. Introduce the word "encrypt" to encrypt the b6 or push Enter to decrypt: ')
    b7 = input().lower()
    if b7 = = 'encrypt':
        b1 = fonk1(b2, b6)
    else:
        b1 = fonk2(b2, b6)
    print(f'{b7.title()}ed b6:')
    print(b1)
if b8 = = '__main__':
    fonk8()