import string
b1 = string.ascii_uppercase
def fonk1(b3, b6):
    return fonk3(b3, b6, 'encrypt')
def fonk2(b3, b6):
    return fonk3(b3, b6, 'decrypt')
def fonk3(b3, b6, b7):
    b2 = []
    b3 = b3.upper()
    a1 = 0
    b4 = b7 == 'encrypt'
    for symbol in b6:
        b5 = b1.find(symbol.upper())
        if fonk4(b5):
            b5 = fonk5(b4, b3, a1, b5)
            if symbol.isupper():
                b2.append(b1[b5])
            elif symbol.islower():
                b2.append(b1[b5].lower())
            a1 = fonk6(b3, a1)
        else:
            b2.append(symbol)
    return ''.join(b2)
def fonk4(b5):
    return b5 != -1
def fonk5(b4, b3, a1, b5):
    if b4:
        b5 += b1.find(b3[a1])
    else:
        b5 -= b1.find(b3[a1])
    b5 %= len(b1)
    return b5
def fonk6(b3, a1):
    a1 += 1
    if a1 = = len(b3):
        a1 = 0
    return a1
def fonk7():
    print('1. Introduce a b6: ')
    b6 = input()
    print('2. Introduce the b3: ')
    b3 = input()
    print('3. Introduce the word "encrypt" to encrypt the b6 or press Enter to decrypt: ')
    b7 = input().lower()
    if b7 = = 'encrypt':
        b2 = fonk1(b3, b6)
    else:
        b2 = fonk2(b3, b6)
    print('%sed b6:' % (b7.title() if b7 else "Decrypt"))
    print(b2)
if b8 = = '__main__':
    fonk7()