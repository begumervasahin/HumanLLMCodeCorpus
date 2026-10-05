import random
import binascii
def fonk1(message):
    b1 = 'utf8'
    b2 = message.encode(b1)
    b3 = int(binascii.hexlify(b2), 16)
    b4 = bin(b3)[2:]
    return b4.zfill(8 * ((len(b4) + 7)
def fonk2(message):
    b1 = 'utf8'
    b5 = int(message, 2)
    b6 = '%x' % b5
    b7 = len(b6)
    b8 = binascii.unhexlify(b6.zfill(b7 + (b7 & 1)))
    return b8.decode(b1)
def fonk3(ln):
    return bin(random.getrandbits(ln))[2:].zfill(ln)
def fonk4(lista1, lista2, ln):
    b9 = []
    for i in range(ln):
        if lista1[i] == lista2[i]:
            b9.append('0')
        else:
            b9.append('1')
    return ''.join(b9)
def fonk5():
    while True:
        print("\n1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        b10 = input("Enter the option you want to perform: ")
        if b10 = = '1':
            print("\b5+-----------Encrypt-----------+")
            b11 = input("Enter the message to encrypt: ")
            b12 = fonk1(b11)
            print("\nBinary String: \b5" + b12)
            b13 = len(b12)
            b14 = fonk3(b13)
            print("\nOne-time pad: \b5" + str(b14))
            b9 = fonk4(b12, b14, b13)
            print("\nEncrypted Message: \b5" + str(b9))
        elif b10 = = '2':
            print("\b5+-----------Decrypt-----------+")
            b15 = input("Enter the encrypted string: ")
            b16 = input("Key: ")
            b17 = len(b15)
            b9 = fonk4(b15, b16, b17)
            b18 = fonk2(b9)
            print("\nThe decrypted message is: " + b18)
        elif b10 = = '3':
            print("Exiting... Goodbye")
            break
        else:
            print("Invalid option! Please enter a valid option.")
if b19 = = "__main__":
    fonk5()