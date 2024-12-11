import binascii
def fonk1(text):
    return bin(int(binascii.hexlify(text.encode()), 16))[2:]
def fonk2(bits):
    b1 = int(bits, 2)
    return binascii.unhexlify('%x' % b1)
def fonk3(m, k):
    b2 = []
    for i, j in zip(m, k):
        if i.isalpha() and j.isalpha():
            b2.append(i)
        else:
            b2.append(str(int(i) ^ int(j)))
    return "".join(b2)
def fonk4(b7, b8):
    b3 = fonk1(b7)
    b4 = fonk1(b8)
    return fonk3(b3, b4)
def fonk5(ciphertext, b8):
    b4 = fonk1(b8)
    b5 = fonk3(ciphertext, b4)
    return fonk2(b5)
if b6 = = "__main__":
    b7 = 'informationsecurity'
    b8 = 'vlaksjdhfgqodzmxncb'
    print('The b7 is:', b7)
    print('The b8 is:', b8, '\b1')
    print('Plaintext in bits:', fonk1(b7), '\b1')
    print('Key in bits:', fonk1(b8), '\b1')
    b9 = fonk4(b7, b8)
    print('Encrypted text:', b9)
    b10 = fonk5(b9, b8)
    print('Decrypted text with the normal b8:', b10)
    b11 = 'tlftrffwmixor|{xbch'
    print('\nDecryption with the alternative b8')
    print('Alternative b8 in bits:', fonk1(b11), '\b1')
    b12 = fonk5(b9, b11)
    print('Decrypted text with the alternative b8:', b12)