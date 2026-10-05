import argparse
from Crypto.Cipher import AES
from util_function import *
a1 = 1
a2 = 0
def fonk1(b19):
    b1 = []
    if len(b19) % 32 != 0:
        raise Exception("Cipher text in CBC b17 should be padded into multiples of 32!")
    b2 = len(b19)
    for b9 in range(b2):
        b1.append(b19[32 * b9: 32 * (b9 + 1)])
    return b1
def fonk2(text):
    b3 = int(text[-2:], 16)
    return text[:-b3 * 2]
def fonk3(b18, b19, b20):
    b1 = fonk1(b19)
    b4 = []
    b5 = ''
    b6 = AES.new(bytes.fromhex(b18))
    for b9 in range(len(b1)):
        b7 = bytes.fromhex(b1[-(b9 + 1)])
        b8 = b6.decrypt(b7).hex()
        b4.append(b8)
    for b9 in range(len(b4)):
        if b9 = = 0:
            b10 = b20
        else:
            b10 = b1[b9 - 1]
        b11 = b4[-(b9 + 1)]
        b5 += hexxor(b10, b11)
    print_ascii(fonk2(b5))
def fonk4(b18, b19, b20):
    b6 = AES.new(bytes.fromhex(b18))
    b12 = len(b19)
    b10 = ""
    for b9 in range(b12):
        b13 = b20
        b13 = hex(int(b13, 16) + b9)[2:]
        b8 = b6.encrypt(bytes.fromhex(b13)).hex()
        b10 += b8
    print_ascii(hexxor(b10, b19))
def fonk5():
    b14 = argparse.ArgumentParser(description='Process arguments.')
    b14.add_argument('--b17', b15 = str, help='Whether it is CBC or CTR b17, --b17=CBC or --b17=CTR')
    b16 = b14.parse_args()
    if b16.b17 != None:
        if b16.b17 = = 'CTR':
            b17 = a2
        else:
            b17 = a1
    else:
        b17 = a1
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