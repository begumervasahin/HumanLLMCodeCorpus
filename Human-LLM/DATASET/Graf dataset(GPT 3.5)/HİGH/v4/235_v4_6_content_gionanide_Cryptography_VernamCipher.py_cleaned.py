import binascii
def fonk1(text):
    b1 = binascii.hexlify(text.encode()).decode()
    return bin(int(b1, 16))[2:]
def fonk2(m, k):
    b2 = []
    for bit_m, bit_k in zip(m, k):
        if bit_m.isalpha() and bit_k.isalpha():
            b2.append(bit_m)
        else:
            b2.append(str(int(bit_m) ^ int(bit_k)))
    return "".join(b2)
def fonk3(binary):
    b1 = hex(int(binary, 2))[2:]
    return binascii.unhexlify(b1).decode()
if b3 = = "__main__":
    b4 = 'informationsecurity'
    b5 = 'vlaksjdhfgqodzmxncb'
    print('The plain text is:', b4)
    print('The first key is:', b5, '\n')
    b6 = fonk1(b4)
    b7 = fonk1(b5)
    print('Plain text in bits:', b6, '\n')
    print('Key in bits:', b7, '\n')
    b2 = fonk2(b6, b7)
    b8 = int(b2, 2)
    b9 = fonk3(b2)
    print('XOR b2 for the encryption with the normal key:', b2, '\n')
    print('Encrypted text:', b9)
    b10 = fonk2(b2, b7)
    b11 = int(b10, 2)
    b12 = fonk3(b10)
    print('\nDecryption b2:', b10, '\n')
    print('Decrypted text with the normal key:', b12, '\n')
    b13 = 'tlftrffwmixor|{xbch'
    b14 = fonk1(b13)
    b15 = fonk2(b2, b14)
    b16 = fonk3(b15)
    print('Decryption with the alternative key\n')
    print('Alternative key in bits:', b14, '\n')
    print('Decrypted text with the alternative key:', b16)