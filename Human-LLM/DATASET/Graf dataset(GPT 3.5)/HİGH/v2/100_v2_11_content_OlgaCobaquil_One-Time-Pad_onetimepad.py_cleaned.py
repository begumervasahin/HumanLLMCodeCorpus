import random
import binascii
def fonk1(b11):
    b1 = 'utf8'
    b2 = b11.encode(b1)
    b3 = int(binascii.hexlify(b2), 16)
    b4 = bin(b3)[2:]
    return b4.zfill(8 * ((len(b4) + 7)
def fonk2(b11):
    b1 = 'utf8'
    b5 = int(b11, 2)
    b6 = '%x' % b5
    b7 = len(b6)
    b8 = binascii.unhexlify(b6.zfill(b7 + (b7 & 1)))
    return b8.decode(b1)
def fonk3(b16):
    return bin(random.getrandbits(b16))[2:].zfill(b16)
def fonk4(list1, list2, b16):
    b9 = []
    for i in range(b16):
        if list1[i] == list2[i]:
            b9.append('0')
        else:
            b9.append('1')
    return ''.join(b9)
def fonk5():
    while True:
        print("\n1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        b10 = input("Enter the b10 you want to perform: ")
        if b10 = = '1':
            print("\b5+-----------Encrypt-----------+")
            b11 = input("Enter the b11 to encrypt: ")
            b4 = fonk1(b11)
            print("\nBinary String:\b5" + b4)
            b12 = len(b4)
            b13 = fonk3(b12)
            print("\nOne-time pad:\b5" + str(b13))
            b9 = fonk4(b4, b13, b12)
            print("\nEncrypted Message:\b5" + str(b9))
        elif b10 = = '2':
            print("\b5+-----------Decrypt-----------+")
            b14 = input("Enter the encrypted string: ")
            b15 = input("Key: ")
            b16 = len(b14)
            b9 = fonk4(b14, b15, b16)
            b17 = fonk2(b9)
            print("\nThe decrypted b11 is: " + b17)
        elif b10 = = '3':
            print("Exiting... Goodbye")
            break
        else:
            print("Invalid b10! Please enter a valid b10.")
if b18 = = "__main__":
    fonk5()