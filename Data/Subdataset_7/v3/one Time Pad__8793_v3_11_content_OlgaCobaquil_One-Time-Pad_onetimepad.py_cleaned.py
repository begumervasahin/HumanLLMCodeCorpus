import random
import binascii
def fonk1(b10):
    b1 = b10.encode('utf8')
    b2 = int(binascii.hexlify(b1), 16)
    b3 = bin(b2)[2:]
    return b3.zfill(8 * ((len(b3) + 7)
def fonk2(b10):
    b4 = int(b10, 2)
    b5 = '%x' % b4
    b6 = len(b5)
    b7 = binascii.unhexlify(b5.zfill(b6 + (b6 & 1)))
    return b7.decode('utf8')
def fonk3(b17):
    return bin(random.getrandbits(b17))[2:].zfill(b17)
def fonk4(list1, list2, b17):
    b8 = ['0' if list1[i] == list2[i] else '1' for i in range(b17)]
    return ''.join(b8)
def fonk5():
    while True:
        print("\n1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        b9 = input("Enter the b9 you want to perform: ")
        if b9 = = '1':
            print("\b4+-----------Encrypt-----------+")
            b10 = input("Enter the b10 to encrypt: ")
            b11 = fonk1(b10)
            print("\nBinary String:\b4" + b11)
            b12 = len(b11)
            b13 = fonk3(b12)
            print("\nOne-time pad:\b4" + b13)
            b14 = fonk4(b11, b13, b12)
            print("\nEncrypted Message:\b4" + b14)
        elif b9 = = '2':
            print("\b4+-----------Decrypt-----------+")
            b15 = input("Enter the encrypted string: ")
            b16 = input("Key: ")
            b17 = len(b15)
            b18 = fonk4(b15, b16, b17)
            b19 = fonk2(b18)
            print("\nThe decrypted b10 is: " + b19)
        elif b9 = = '3':
            print("Exiting... Goodbye")
            break
        else:
            print("Invalid b9! Please enter a valid b9.")
if b20 = = "__main__":
    fonk5()