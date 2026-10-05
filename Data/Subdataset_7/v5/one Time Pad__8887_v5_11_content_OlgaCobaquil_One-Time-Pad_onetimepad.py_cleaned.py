import random
import binascii
def fonk1(b16):
    b1 = b16.encode('utf-8')
    b2 = int(binascii.hexlify(b1), 16)
    b3 = bin(b2)[2:]
    return b3.zfill(8 * ((len(b3) + 7)
def fonk2(b16):
    b4 = int(b16, 2)
    b5 = '%x' % b4
    b6 = b5.zfill(len(b5) + (len(b5) & 1))
    b7 = binascii.unhexlify(b6)
    return b7.decode('utf-8')
def fonk3(length):
    return bin(random.getrandbits(length))[2:].zfill(length)
def fonk4(bit_string1, bit_string2):
    b8 = ['0' if bit1 == bit2 else '1' for bit1, bit2 in zip(bit_string1, bit_string2)]
    return ''.join(b8)
def fonk5(b16):
    b9 = fonk1(b16)
    b10 = len(b9)
    b11 = fonk3(b10)
    b12 = fonk4(b9, b11)
    return b12, b11
def fonk6(b17, b18):
    b13 = fonk4(b17, b18)
    b14 = fonk2(b13)
    return b14
def fonk7():
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    b15 = int(input("Enter the b15 you want to perform: "))
    if b15 = = 1:
        print("\n+-----------Encryption-----------+")
        b16 = input("Enter the b16 to encrypt: ")
        b17, b11 = fonk5(b16)
        print("\nEncrypted Message: \n" + b17)
        print("\nOne-Time Pad Key: \n" + b11)
    elif b15 = = 2:
        print("\n+-----------Decryption-----------+")
        b17 = input("Enter the encrypted b16: ")
        b18 = input("Enter the decryption key: ")
        b14 = fonk6(b17, b18)
        print("\nThe decrypted b16 is: " + b14)
    elif b15 = = 3:
        print("Exiting... Goodbye!")
if b19 = = "__main__":
    fonk7()