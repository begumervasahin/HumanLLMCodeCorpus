import random
import binascii
def fonk1(b11):
    b1 = 'utf-8'
    b2 = b11.encode(b1)
    b3 = int(binascii.hexlify(b2), 16)
    b4 = bin(b3)[2:]
    return b4.zfill(8 * ((len(b4) + 7)
def fonk2(b11):
    b1 = 'utf-8'
    b5 = int(b11, 2)
    b6 = '%x' % b5
    b7 = b6.zfill(len(b6) + (len(b6) & 1))
    b8 = binascii.unhexlify(b7)
    return b8.decode(b1)
def fonk3(length):
    return bin(random.getrandbits(length))[2:].zfill(length)
def fonk4(bit_string1, bit_string2, length):
    b9 = ['0' if bit_string1[i] == bit_string2[i] else '1' for i in range(length)]
    return ''.join(b9)
def fonk5():
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    b10 = int(input("Enter the b10 you want to perform: "))
    if b10 = = 1:
        print("\n+-----------Encryption-----------+")
        b11 = input("Enter the b11 to encrypt: ")
        b12 = fonk1(b11)
        print("\nBinary Representation: \n" + b12)
        b13 = len(b12)
        b14 = fonk3(b13)
        print("\nOne-Time Pad Key: \n" + b14)
        b15 = fonk4(b12, b14, b13)
        print("\nEncrypted Message: \n" + b15)
    elif b10 = = 2:
        print("\n+-----------Decryption-----------+")
        b16 = input("Enter the encrypted b11: ")
        b17 = input("Enter the decryption key: ")
        b18 = len(b16)
        b19 = fonk4(b16, b17, b18)
        b20 = fonk2(b19)
        print("\nThe decrypted b11 is: " + b20)
    elif b10 = = 3:
        print("Exiting... Goodbye!")
if b21 = = "__main__":
    fonk5()