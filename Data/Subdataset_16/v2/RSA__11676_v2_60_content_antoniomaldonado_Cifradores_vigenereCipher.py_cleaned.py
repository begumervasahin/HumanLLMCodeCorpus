
import string
b1 = string.ascii_uppercase
def fonk1(b3, b7):
    return fonk3(b3, b7, 'encrypt')
def fonk2(b3, b7):
    return fonk3(b3, b7, 'decrypt')
def fonk3(b3, b7, b8):
    b2 = []
    b3 = b3.upper()
    a1 = 0
    b4 = b8 == 'encrypt'
    for symbol in b7:
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
    b6 = b1.find(b3[a1])
    if b4:
        b5 += b6
    else:
        b5 -= b6
    return b5 % len(b1)
def fonk6(b3, a1):
    a1 += 1
    if a1 = = len(b3):
        a1 = 0
    return a1
def fonk7():
    print('1. Introduce a b7: ')
    b7 = input()
    print('2. Introduce the b3: ')
    b3 = input()
    print('3. Introduce the word "encrypt" to encrypt the b7 or press Enter to decrypt: ')
    b8 = input().lower()
    if b8 = = 'encrypt':
        b2 = fonk1(b3, b7)
    else:
        b2 = fonk2(b3, b7)
    print(f'{b8.title() if b8 else "Decrypt"}ed b7:')
    print(b2)
if b9 = = '__main__':
    fonk7()