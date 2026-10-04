import binascii
def fonk1(data, length):
    return bin(int(binascii.hexlify(data.encode()), 16))[2:].zfill(length)
def fonk2(binary_message, binary_key):
    return ''.join(str(int(m) ^ int(k)) for m, k in zip(binary_message, binary_key))
def fonk3(binary_data):
    b1 = int(binary_data, 2)
    b2 = f'{b1:x}'
    return binascii.unhexlify(b2).decode()
b3 = 'informationsecurity'
b4 = 'vlaksjdhfgqodzmxncb'
print('The plain text is:', b3)
print('The first key is:', b4, '\n')
b5 = len(b4) * 8
b6 = fonk1(b3, b5)
b7 = fonk1(b4, b5)
print('Plain text in bits:', b6)
print('Key in bits:', b7, '\n')
b8 = fonk2(b6, b7)
b9 = fonk3(b8)
print('XOR result for the encryption with the normal key:', b8)
print('Encrypted text:', b9)
b10 = fonk2(b8, b7)
b11 = fonk3(b10)
print('\nDecryption result:', b10)
print('Decrypted text with the normal key:', b11, '\n')
b12 = fonk1('tlftrffwmixor|{xbch', b5)
print('Alternative key in bits:', b12, '\n')
b13 = fonk2(b8, b12)
b14 = fonk3(b13)
print('Decrypted text with the alternative key:', b14)