import argparse
from Crypto.Cipher import AES
from util_function import hexxor, print_ascii
a1 = 1
a2 = 0
def fonk1(b20):
    if len(b20) % 32 != 0:
        raise ValueError("Cipher text in CBC b18 should be padded to a multiple of 32!")
    b1 = len(b20)
    return [b20[32 * b9: 32 * (b9 + 1)] for b9 in range(b1)]
def fonk2(text):
    b2 = int(text[-2], 16)
    b3 = b2 * 2
    return text[:-b3]
def fonk3(b19, b20, b21):
    b4 = fonk1(b20)
    b5 = []
    b6 = ''
    b7 = AES.new(bytes.fromhex(b19), AES.MODE_ECB)
    for block in reversed(b4):
        b8 = b7.decrypt(bytes.fromhex(block)).hex()
        b5.append(b8)
    for b9, intermediate_block in enumerate(reversed(b5)):
        if b9 = = 0:
            b10 = b21
        else:
            b10 = b4[b9 - 1]
        b6 += hexxor(b10, intermediate_block)
    print_ascii(fonk2(b6))
def fonk4(b19, b20, b21):
    b7 = AES.new(bytes.fromhex(b19), AES.MODE_ECB)
    b11 = len(b20)
    b12 = ""
    for b9 in range(b11):
        b13 = hex(int(b21, 16) + b9)[2:].zfill(32)
        b14 = b7.encrypt(bytes.fromhex(b13)).hex()
        b12 += b14
    print_ascii(hexxor(b12, b20))
def fonk5():
    b15 = argparse.ArgumentParser(description='AES Decryption Tool')
    b15.add_argument('--b18', b16 = str, help='Decryption b18: CBC or CTR')
    b17 = b15.parse_args()
    b18 = a1 if b17.b18 is None or b17.b18.upper() == 'CBC' else a2
    b19 = input("Enter the b19: ")
    b20 = input("Enter the cipher text: ")
    b21 = b20[:32]
    b20 = b20[32:]
    if b18 = = a1:
        fonk3(b19, b20, b21)
    else:
        fonk4(b19, b20, b21)
if b22 = = "__main__":
    fonk5()