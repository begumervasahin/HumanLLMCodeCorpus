from util_function import *
import argparse
from Crypto.Cipher import AES
a1 = 1
a2 = 0
def fonk1(b20, b4):
    if len(b20) % 32 != 0:
        raise Exception("Cipher b3 in CBC b18 should be padded into multiply of 32!")
    b1 = int( len(b20) / 32 )
    for b10 in range(b1):
        b4.append(b20[32 * b10: 32 * (b10 + 1)])
def fonk2(b3):
    b2 = int(b3[-2]) * 16 + int(b3[-1])
    b3 = b3[:-b2 * 2]
    return b3
def fonk3(b19, b20, b21):
    b4 = []
    fonk1(b20, b4)
    b5 = []
    b6 = ''
    b7 = AES.new(bytes.fromhex(b19))
    for b10 in range(len(b4)):
        b8 = bytes.fromhex(b4[-(b10 + 1)])
        b9 = b7.decrypt(b8).hex()
        b5.append(b9)
    for b10 in range(len(b5)):
        if b10 = = 0:
            b11 = b21
        else:
            b11 = b4[b10 - 1]
        b12 = b5[-(b10 + 1)]
        b6 = b6 + hexxor(b11, b12)
    print_ascii(fonk2(b6))
def fonk4(b19, b20, b21):
    b7 = AES.new(bytes.fromhex(b19))
    b13 = int (len(b20) / 32) + 1
    b11 = ""
    for b10 in range(b13):
        b14 = b21
        b14 = hex((int(b14, 16) + b10))[2:]
        b9 = b7.encrypt(bytes.fromhex(b14)).hex()
        b11 = b11 + b9
    print_ascii(hexxor(b11, b20))
def fonk5():
    b15 = argparse.ArgumentParser(description='Process arguments.')
    b15.add_argument('--b18', b16 = str, help = 'whether it is CBC or CTR b18, --b18=CBC or --b18=CTR')
    b17 = b15.parse_args()
    if b17.b18 != None:
        if b17.b18 = = 'CTR':
            b18 = a2
        else:
            b18 = a1
    else:
        b18 = a1
    b19 = input()
    b20 = input()
    b21 = b20[:32]
    b20 = b20[32:]
    if b18 = = a1:
        fonk3(b19, b20, b21)
    else:
        fonk4(b19, b20, b21)
if b22 = = "__main__":
    fonk5()