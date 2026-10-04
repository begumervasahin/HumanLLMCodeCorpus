import argparse
from Crypto.Cipher import AES
from util_function import hexxor, print_ascii
a1 = 1
a2 = 0
def fonk1(b19):
    if len(b19) % 32 != 0:
        raise ValueError("Cipher text in CBC b17 should be padded to a multiple of 32!")
    b1 = len(b19)
    return [b19[32 * i: 32 * (i + 1)] for i in range(b1)]
def fonk2(text):
    b2 = int(text[-2], 16)
    b3 = b2 * 2
    return text[:-b3]
def fonk3(b18, b19, b20):
    b4 = fonk1(b19)
    b5 = []
    b6 = ''
    b7 = AES.new(bytes.fromhex(b18), AES.MODE_ECB)
    for block in reversed(b4):
        b8 = b7.decrypt(bytes.fromhex(block)).hex()
        b5.append(b8)
    for i, intermediate_block in enumerate(reversed(b5)):
        b9 = b20 if i == 0 else b4[i - 1]
        b6 += hexxor(b9, intermediate_block)
    print_ascii(fonk2(b6))
def fonk4(b18, b19, b20):
    b7 = AES.new(bytes.fromhex(b18), AES.MODE_ECB)
    b10 = len(b19)
    b11 = ""
    for i in range(b10):
        b12 = hex(int(b20, 16) + i)[2:].zfill(32)
        b13 = b7.encrypt(bytes.fromhex(b12)).hex()
        b11 += b13
    print_ascii(hexxor(b11, b19))
def fonk5():
    b14 = argparse.ArgumentParser(description='AES Decryption Tool')
    b14.add_argument('--b17', b15 = str, help='Decryption b17: CBC or CTR')
    b16 = b14.parse_args()
    b17 = a1 if b16.b17 is None or b16.b17.upper() == 'CBC' else a2
    b18 = input("Enter the b18: ")
    b19 = input("Enter the cipher text: ")
    b20 = b19[:32]
    b19 = b19[32:]
    if b17 = = a1:
        fonk3(b18, b19, b20)
    else:
        fonk4(b18, b19, b20)
if b21 = = "__main__":
    fonk5()