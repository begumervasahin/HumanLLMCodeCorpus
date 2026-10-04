import utils.dictUtils
def fonk1(b2, b5):
    return fonk3(b2, b5, 'encrypt')
def fonk2(b2, b5):
    return fonk3(b2, b5, '')
def fonk3(b2, b5, b6):
    b1 = []
    b2 = b2.upper()
    a1 = 0
    b3 = b6 == 'encrypt'
    for symbol in b5:
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
def fonk6(is_encript, b2, a1, b4):
    if is_encript:
        b4 += fonk5().find(b2[a1])
    else:
        b4 -= fonk5().find(b2[a1])
    b4 %= len(fonk5())
    return b4
def fonk7(b2, a1):
    a1 += 1
    if a1 = = len(b2):
        a1 = 0
    return a1
def fonk8():
    print('1. Introduce a b5: ')
    b5 = input()
    print('2. Introduce the b2: ')
    b2 = input()
    print('3. Introduce the word "encrypt" to encrypt the b5 or push '
          'Enter to decrypt: ')
    b6 = input().lower()
    if b6 = = 'encrypt':
        b1 = fonk1(b2, b5)
    else:
        b1 = fonk2(b2, b5)
    print('%sed b5:' % (b6.title()))
    print(b1)
if b7 = = '__main__':
    fonk8()