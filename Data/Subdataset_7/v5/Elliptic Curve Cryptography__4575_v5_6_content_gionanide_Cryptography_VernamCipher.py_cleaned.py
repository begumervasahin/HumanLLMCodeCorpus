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
    b6 = 'tlftrffwmixor|{xbch'
    print('The plain text is:', b4)
    print('The first key is:', b5, '\n')
    b7 = fonk1(b4)
    b8 = fonk1(b5)
    b9 = fonk1(b6)
    print('Plain text in bits:', b7, '\n')
    print('Key in bits:', b8, '\n')
    b10 = fonk2(b7, b8)
    b11 = fonk3(b10)
    print('XOR b2 for the encryption with the normal key:', b10, '\n')
    print('Encrypted text:', b11)
    b12 = fonk2(b10, b8)
    b13 = fonk3(b12)
    print('\nDecryption b2:', b12, '\n')
    print('Decrypted text with the normal key:', b13, '\n')
    b14 = fonk2(b10, b9)
    b15 = fonk3(b14)
    print('Decryption with the alternative key\n')
    print('Alternative key in bits:', b9, '\n')
    print('Decrypted text with the alternative key:', b15)