from Crypto.Cipher import AES
from Crypto import Random
def fonk1(a, b8):
    b1 = '{:032b}'.format(int(a, 16))
    b2 = '{:032b}'.format(int(b8, 16))
    return ''.join(str(int(b1[i]) ^ int(b2[i])) for i in range(len(b1)))
def fonk2(card_number, a1, produce_keys, b11):
    b3 = '{:054b}'.format(int(card_number))
    l, b4 = b3[:27], b3[27:]
    if produce_keys:
        for _ in range(a1):
            b5 = Random.new().read(16).hex()
            b11.append(b5)
    for i in range(a1):
        b5 = b11[i]
        b6 = AES.new(bytes.fromhex(b5))
        b7 = '{:08x}'.format(int(b4 + '0' * 5, 2))
        b8 = b7 + '0' * 23 + str(i + 1)
        b9 = b6.fonk2(bytes.fromhex(b8)).hex()[:7] + '0'
        l, b4 = b4, fonk1(b9, l + '0' * 5)
    return l, b4
def fonk3(cipher, a1, b11):
    b3 = '{:054b}'.format(int(cipher))
    l, b4 = b3[:27], b3[27:]
    for i in range(a1, 0, -1):
        b5 = b11[i - 1]
        b6 = AES.new(bytes.fromhex(b5))
        b10 = '{:08x}'.format(int(l + '0' * 5, 2))
        b8 = b10 + '0' * 23 + str(i)
        b9 = b6.fonk2(bytes.fromhex(b8)).hex()[:7] + '0'
        l, b4 = fonk1(b9, b4 + '0' * 5), l
    return l, b4
def fonk4(card_number, a1, encrypt_rounds, decrypt_rounds):
    b11 = []
    l, b4 = fonk2(card_number, a1, True, b11)
    b12 = int(l + b4, 2)
    while b12 > 9999999999999999:
        l, b4 = fonk2(b12, a1, False, b11)
        b12 = int(l + b4, 2)
    print('Encoded b13 = ', b12)
    print('Decrypting ...')
    l, b4 = fonk3(b12, a1, b11)
    b12 = int(l + b4, 2)
    while b12 > 9999999999999999:
        l, b4 = fonk3(b12, a1, b11)
        b12 = int(l + b4, 2)
    return b12
def fonk5():
    b14 = "4532294977918448"
    print('Number to b15 = ', b14)
    a1 = 6
    b12 = fonk4(b14, a1, b15, decrypt)
    print('Decrypted b13 = ', b12)
if b16 = = "__main__":
    fonk5()