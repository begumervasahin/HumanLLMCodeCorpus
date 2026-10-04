import argparse
from Crypto.Cipher import AES
from util_function import hexxor, print_ascii
a1 = 1
a2 = 0
def fonk1(b16):
    if len(b16) % 32 != 0:
        raise Exception("Cipher text in CBC b14 should be padded to a multiple of 32!")
    b1 = len(b16)
    return [b16[32 * i: 32 * (i + 1)] for i in range(b1)]
def fonk2(text):
    b2 = int(text[-2]) * 16 + int(text[-1])
    return text[:-b2 * 2]
def fonk3(b15, b16, b17):
    b3 = fonk1(b16)
    b4 = []
    b5 = ''
    b6 = AES.new(bytes.fromhex(b15), AES.MODE_ECB)
    for current_text in reversed(b3):
        b7 = b6.decrypt(bytes.fromhex(current_text)).hex()
        b4.append(b7)
    for i, opera2 in enumerate(reversed(b4)):
        b8 = b17 if i == 0 else b3[i - 1]
        b5 += hexxor(b8, opera2)
    print_ascii(fonk2(b5))
def fonk4(b15, b16, b17):
    b6 = AES.new(bytes.fromhex(b15), AES.MODE_ECB)
    b9 = len(b16)
    b8 = ""
    for i in range(b9):
        b10 = hex(int(b17, 16) + i)[2:]
        b7 = b6.encrypt(bytes.fromhex(b10)).hex()
        b8 += b7
    print_ascii(hexxor(b8, b16))
def fonk5():
    b11 = argparse.ArgumentParser(description='Process arguments.')
    b11.add_argument('--b14', b12 = str, help='Mode for decryption: CBC or CTR')
    b13 = b11.parse_args()
    b14 = a1 if b13.b14 is None or b13.b14.upper() == 'CBC' else a2
    b15 = input("Enter the b15: ")
    b16 = input("Enter the cipher text: ")
    b17 = b16[:32]
    b16 = b16[32:]
    if b14 = = a1:
        fonk3(b15, b16, b17)
    else:
        fonk4(b15, b16, b17)
if b18 = = "__main__":
    fonk5()