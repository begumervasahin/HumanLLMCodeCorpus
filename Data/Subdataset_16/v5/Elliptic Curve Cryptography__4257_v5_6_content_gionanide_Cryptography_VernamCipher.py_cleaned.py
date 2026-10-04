import binascii
def fonk1(data):
    b1 = bin(int(binascii.hexlify(data.encode()), 16))[2:]
    return b1.zfill(len(data) * 8)
def fonk2(binary_message, binary_key):
    return ''.join(str(int(bm) ^ int(bk)) for bm, bk in zip(binary_message, binary_key))
def fonk3(b2):
    b1 = f'{int(b2, 2):x}'
    return binascii.unhexlify(b1).decode()
def fonk4(data, label):
    b2 = fonk1(data)
    print(f'{label} in bits: {b2}')
def fonk5(encrypted_result, decrypted_result, b8, b10):
    print(f'XOR result for the encryption: {encrypted_result}')
    print(f'Encrypted text: {b8}\n')
    print(f'Decryption result: {decrypted_result}')
    print(f'Decrypted text: {b10}\n')
b3 = 'informationsecurity'
b4 = 'vlaksjdhfgqodzmxncb'
b5 = 'tlftrffwmixor|{xbch'
print(f'The plain text is: {b3}')
print(f'The first key is: {b4}\n')
fonk4(b3, 'Plain text')
fonk4(b4, 'Key')
b6 = fonk2(fonk1(b3), fonk1(b4))
b7 = int(b6, 2)
b8 = fonk3(b6)
b9 = fonk2(b6, fonk1(b4))
b10 = fonk3(b9)
fonk5(
    b6,
    b9,
    b8,
    b10
)
b11 = fonk1(b5)
print(f'Alternative key in bits: {b11}\n')
b12 = fonk2(b6, b11)
b13 = fonk3(b12)
print(f'Decrypted text with the alternative key: {b13}')