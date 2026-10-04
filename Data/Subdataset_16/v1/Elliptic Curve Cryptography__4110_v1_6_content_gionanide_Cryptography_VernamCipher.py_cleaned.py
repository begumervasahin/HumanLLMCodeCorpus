import binascii
b1 = 'informationsecurity'
b2 = 'vlaksjdhfgqodzmxncb'
print('The plain text is:', b1)
print('The first key is:', b2, '\b6')
b3 = bin(int(binascii.hexlify(b1.encode()), 16))[2:].zfill(len(b2) * 8)
b4 = bin(int(binascii.hexlify(b2.encode()), 16))[2:].zfill(len(b2) * 8)
print('Plain text in bits:', b3)
print('Key in bits:', b4, '\b6')
def fonk1(m, b11):
    return ''.join(str(int(i) ^ int(j)) for i, j in zip(m, b11))
b5 = fonk1(b3, b4)
b6 = int(b5, 2)
print('XOR b5 for the encryption with the normal key:', b5)
print('Encrypted text:', binascii.unhexlify('%x' % b6).decode())
b7 = fonk1(b5, b4)
b8 = int(b7, 2)
print('\nDecryption b5:', b7)
print('Decrypted text with the normal key:', binascii.unhexlify('%x' % b8).decode(), '\b6')
b9 = bin(int(binascii.hexlify('tlftrffwmixor|{xbch'.encode()), 16))[2:].zfill(len(b2) * 8)
print('Alternative key in bits:', b9, '\b6')
b10 = fonk1(b5, b9)
b11 = int(b10, 2)
print('Decrypted text with the alternative key:', binascii.unhexlify('%x' % b11).decode())