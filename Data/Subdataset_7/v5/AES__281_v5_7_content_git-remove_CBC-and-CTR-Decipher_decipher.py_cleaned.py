import argparse
from Crypto.Cipher import AES
from util_function import *
a1 = 1
a2 = 0
def fonk1(b18):
    if len(b18) % 32 != 0:
        raise Exception("Cipher text in CBC b16 should be padded into multiples of 32!")
    return [b18[i:i+32] for i in range(0, len(b18), 32)]
def fonk2(text):
    b1 = int(text[-2:], 16)
    return text[:-b1 * 2]
def fonk3(b17, b18, b19):
    b2 = fonk1(b18)
    b3 = []
    b4 = AES.new(bytes.fromhex(b17))
    for block in reversed(b2):
        b5 = bytes.fromhex(block)
        b6 = b4.decrypt(b5).hex()
        b3.append(b6)
    b7 = ''
    for i, block in enumerate(b3):
        b8 = b19 if i == 0 else b2[i - 1]
        b7 += hexxor(b8, block)
    print_ascii(fonk2(b7))
def fonk4(b17, b18, b19):
    b4 = AES.new(bytes.fromhex(b17))
    b9 = (len(b18)
    b10 = ""
    for i in range(b9):
        b11 = hex(int(b19, 16) + i)[2:]
        b12 = b4.encrypt(bytes.fromhex(b11)).hex()
        b10 += b12
    print_ascii(hexxor(b10, b18))
def fonk5():
    b13 = argparse.ArgumentParser(description='Decrypt AES encrypted text.')
    b13.add_argument('--b16', b14 = str, help='Mode of operation: CBC or CTR (default is CBC)')
    b15 = b13.parse_args()
    b16 = a1 if b15.b16 != 'CTR' else a2
    b17 = input("Enter the b17: ")
    b18 = input("Enter the cipher text: ")
    b19 = b18[:32]
    b18 = b18[32:]
    if b16 = = a1:
        fonk3(b17, b18, b19)
    else:
        fonk4(b17, b18, b19)
if b20 = = "__main__":
    fonk5()