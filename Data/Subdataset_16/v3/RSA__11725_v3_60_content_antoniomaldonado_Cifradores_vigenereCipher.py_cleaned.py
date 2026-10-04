import string
b1 = string.ascii_uppercase
def fonk1(b3, b9):
    return fonk3(b3, b9, 'encrypt')
def fonk2(b3, b9):
    return fonk3(b3, b9, 'decrypt')
def fonk3(b3, b9, b10):
    b2 = []
    b3 = b3.upper()
    a1 = 0
    b4 = (b10 == 'encrypt')
    for symbol in b9:
        b5 = b1.find(symbol.upper())
        if b5 != -1:
            b6 = fonk4(b4, b3, a1, b5)
            b7 = b1[b6]
            if symbol.islower():
                b2.append(b7.lower())
            else:
                b2.append(b7)
            a1 = fonk5(b3, a1)
        else:
            b2.append(symbol)
    return ''.join(b2)
def fonk4(b4, b3, a1, b5):
    b8 = b1.find(b3[a1])
    if b4:
        b6 = (b5 + b8) % len(b1)
    else:
        b6 = (b5 - b8) % len(b1)
    return b6
def fonk5(b3, current_index):
    b6 = (current_index + 1) % len(b3)
    return b6
def fonk6():
    b9 = input('1. Introduce a b9: ')
    b3 = input('2. Introduce the b3: ')
    b10 = input('3. Introduce the word "encrypt" to encrypt the b9 or press Enter to decrypt: ').lower()
    if b10 = = 'encrypt':
        b2 = fonk1(b3, b9)
    else:
        b2 = fonk2(b3, b9)
    b11 = b10.title() if b10 else "Decrypt"
    print(f'{b11}ed b9:')
    print(b2)
if b12 = = '__main__':
    fonk6()