import binascii
def fonk1(data):
    b1 = bin(int(binascii.hexlify(data.encode()), 16))[2:]
    return b1.zfill(len(data) * 8)
def fonk2(binary_message, binary_key):
    return ''.join(str(int(bm) ^ int(bk)) for bm, bk in zip(binary_message, binary_key))
def fonk3(binary_data):
    b2 = int(binary_data, 2)
    b1 = f'{b2:x}'
    return binascii.unhexlify(b1).decode()
b3 = 'informationsecurity'
b4 = 'vlaksjdhfgqodzmxncb'
b5 = 'tlftrffwmixor|{xbch'
print('The plain text is:', b3)
print('The first key is:', b4, '\n')
b6 = fonk1(b3)
b7 = fonk1(b4)
print('Plain text in bits:', b6)
print('Key in bits:', b7, '\n')
b8 = fonk2(b6, b7)
b9 = int(b8, 2)
b10 = fonk3(b8)
print('XOR result for the encryption with the normal key:', b8)
print('Encrypted text:', b10)
b11 = fonk2(b8, b7)
b12 = fonk3(b11)
print('\nDecryption result:', b11)
print('Decrypted text with the normal key:', b12, '\n')
b13 = fonk1(b5)
print('Alternative key in bits:', b13, '\n')
b14 = fonk2(b8, b13)
b15 = fonk3(b14)
print('Decrypted text with the alternative key:', b15)