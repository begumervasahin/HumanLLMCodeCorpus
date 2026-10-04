import argparse
from Crypto.Cipher import AES
from util_function import hexxor, print_ascii
a1 = 1
a2 = 0
def fonk1(b17):
    if len(b17) % 32 != 0:
        raise ValueError("Cipher text in CBC b15 should be padded to a multiple of 32!")
    return [b17[i:i+32] for i in range(0, len(b17), 32)]
def fonk2(text):
    b1 = int(text[-2:], 16)
    return text[:-b1 * 2]
def fonk3(b16, b17, b18):
    b2 = fonk1(b17)
    b3 = []
    b4 = ''
    b5 = AES.new(bytes.fromhex(b16), AES.MODE_ECB)
    for block in reversed(b2):
        b6 = b5.decrypt(bytes.fromhex(block)).hex()
        b3.append(b6)
    for i, intermediate_block in enumerate(reversed(b3)):
        b7 = b18 if i == 0 else b2[i - 1]
        b4 += hexxor(b7, intermediate_block)
    print_ascii(fonk2(b4))
def fonk4(b16, b17, b18):
    b5 = AES.new(bytes.fromhex(b16), AES.MODE_ECB)
    b8 = (len(b17) + 31)
    b9 = ""
    for i in range(b8):
        b10 = hex(int(b18, 16) + i)[2:].zfill(32)
        b11 = b5.encrypt(bytes.fromhex(b10)).hex()
        b9 += b11
    print_ascii(hexxor(b9, b17))
def fonk5():
    b12 = argparse.ArgumentParser(description='AES Decryption Tool')
    b12.add_argument('--b15', b13 = str, help='Decryption b15: CBC or CTR', default='CBC')
    b14 = b12.parse_args()
    b15 = a1 if b14.b15.upper() == 'CBC' else a2
    b16 = input("Enter the b16: ")
    b17 = input("Enter the cipher text: ")
    b18 = b17[:32]
    b17 = b17[32:]
    if b15 = = a1:
        fonk3(b16, b17, b18)
    else:
        fonk4(b16, b17, b18)
if b19 = = "__main__":
    fonk5()