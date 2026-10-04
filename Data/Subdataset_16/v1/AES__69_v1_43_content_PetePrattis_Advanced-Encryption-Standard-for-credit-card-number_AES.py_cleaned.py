from Crypto.Cipher import AES
from Crypto import Random
def fonk1(a, b8):
    b1 = '{:032b}'.format(int(a, 16))
    b2 = '{:032b}'.format(int(b8, 16))
    return ''.join(str(int(b1[i]) ^ int(b2[i])) for i in range(len(b1)))
def fonk2(card_number, a1, produce_keys, b15):
    b3 = '{:054b}'.format(int(card_number))
    b11, b4 = b3[:27], b3[27:]
    if produce_keys:
        for _ in range(a1):
            b5 = Random.new().read(16).hex()
            b15.append(b5)
    for i in range(a1):
        b5 = b15[i]
        b6 = AES.new(bytes.fromhex(b5))
        b7 = '{:08x}'.format(int(b4 + '0' * 5, 2))
        b8 = b7 + '0' * 23 + str(i + 1)
        b9 = b6.b14(bytes.fromhex(b8)).hex()[:7] + '0'
        b10 = b4
        b4 = fonk1(b9, b11 + '0' * 5)
        b11 = b10
    return b11, b4
def fonk3(cipher, a1, b15):
    b3 = '{:054b}'.format(int(cipher))
    b11, b4 = b3[:27], b3[27:]
    for i in range(a1, 0, -1):
        b5 = b15[i - 1]
        b6 = AES.new(bytes.fromhex(b5))
        b12 = '{:08x}'.format(int(b11 + '0' * 5, 2))
        b8 = b12 + '0' * 23 + str(i)
        b9 = b6.b14(bytes.fromhex(b8)).hex()[:7] + '0'
        b10 = b11
        b11 = fonk1(b9, b4 + '0' * 5)
        b4 = b10
    return b11, b4
def fonk4():
    b13 = "4532294977918448"
    print('Number to b14 = ', b13)
    b15 = []
    a1 = 6
    b11, b4 = fonk2(b13, a1, True, b15)
    b16 = int(b11 + b4, 2)
    while b16 > 9999999999999999:
        print('Not valid encoded b17 = ', b16)
        b11, b4 = fonk2(b16, a1, False, b15)
        b16 = int(b11 + b4, 2)
    print('Encoded b17 = ', b16)
    print('Decrypting ...')
    print('Cipher to b18 = ', b16)
    b11, b4 = fonk3(b16, a1, b15)
    b16 = int(b11 + b4, 2)
    while b16 > 9999999999999999:
        print('Not valid encoded b17 = ', b16)
        b11, b4 = fonk3(b16, a1, b15)
        b16 = int(b11 + b4, 2)
    print('Decrypted b17 = ', b16)
if b19 = = "__main__":
    fonk4()