from Crypto.Cipher import AES
from Crypto import Random
b1 = "4532294977918448"
print('Number to b2 = ', b1)
b3 = []
def fonk1(a, b11):
    b4 = '{:032b}'.format(int(a, 16))
    b5 = '{:032b}'.format(int(b11, 16))
    return ''.join(str(int(b4[i]) ^ int(b5[i])) for i in range(len(b4) - 5))
def fonk2(card_number, a1, generate_keys):
    b6 = '{:054b}'.format(int(card_number))
    l, b7 = b6[:27], b6[27:]
    if generate_keys:
        for _ in range(a1):
            b8 = Random.new().read(16).hex()
            b3.append(b8)
    for i in range(a1):
        b8 = b3[i]
        b9 = AES.new(bytes.fromhex(b8))
        b10 = '{:08x}'.format(int(b7 + '0' * 5, 2))
        b11 = b10 + '0' * 23 + str(i + 1)
        b12 = b9.fonk2(bytes.fromhex(b11)).hex()[:7] + '0'
        l, b7 = b7, fonk1(b12, l + '0' * 5)
    return l, b7
def fonk3(cipher, a1):
    b6 = '{:054b}'.format(int(cipher))
    l, b7 = b6[:27], b6[27:]
    for i in range(a1, 0, -1):
        b8 = b3[i - 1]
        b9 = AES.new(bytes.fromhex(b8))
        b13 = '{:08x}'.format(int(l + '0' * 5, 2))
        b11 = b13 + '0' * 23 + str(i)
        b12 = b9.fonk2(bytes.fromhex(b11)).hex()[:7] + '0'
        l, b7 = fonk1(b12, b7 + '0' * 5), l
    return l, b7
def fonk4():
    a1 = 6
    l, b7 = fonk2(b1, a1, True)
    b14 = int(l + b7, 2)
    while b14 > 9999999999999999:
        print('Not valid encoded b15 = ', b14)
        l, b7 = fonk2(b14, a1, False)
        b14 = int(l + b7, 2)
    print('Encoded b15 = ', b14)
    print('Decrypting ...')
    print('Cipher to b16 = ', b14)
    l, b7 = fonk3(b14, a1)
    b14 = int(l + b7, 2)
    while b14 > 9999999999999999:
        print('Not valid encoded b15 = ', b14)
        l, b7 = fonk3(b14, a1)
        b14 = int(l + b7, 2)
    print('Decrypted b15 = ', b14)
if b17 = = "__main__":
    fonk4()