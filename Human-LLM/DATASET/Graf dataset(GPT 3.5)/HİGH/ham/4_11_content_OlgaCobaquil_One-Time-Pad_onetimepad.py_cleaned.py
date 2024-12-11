
import random
import binascii
def fonk1(message):
    """ ord -> unicode
        format -> binario
    return "".join(seven_bits(format(ord(x), 'b')) for x in message)
    return ''.join(chr(int(message[i*8:i*8+8],2)) for i in range(len(message)
def fonk2(ln):
    return bin(random.getrandbits(ln))[2:].zfill(ln)
def fonk3(lista1, lista2,ln):
    b1 = []
    for i in range(ln):
        if (lista1[i] == lista2[i]):
            b1.append('0')
        else:
            b1.append('1')
    b2 = ''.join(b1)
    return b2
def fonk4():
    print(" 1. Cifrar ")
    print(" 2. Descifrar")
    print(" 3. Salir")
    b3 = input("Ingrese la opcion que desea realizar: ")
    if (b3 = = 1):
        print("\n+-----------Cifrar-----------+")
        b4 = raw_input("Ingrese el mensaje a cifrar: ")
        b5 = fonk1(b4)
        print("\nCadena Binaria: \n" + b5)
        b6 = len(b5)
        b7 = fonk2(b6)
        print("\nOne time pad: \n" + str(b7))
        b1 = fonk3(b5, b7, b6)
        print("\nCifrado: \n" + str(b1))
    elif (b3 = = 2):
        print("\n+-----------Descifrar-----------+")
        b8 = raw_input("Ingresar la b2 cifrada: ")
        b9 = raw_input("Key: ")
        b10 = len(b8)
        b1 = fonk3(b8, b9,b10)
        b11 = bits_to_string(b1)
        print("\nEl mensaje es: "+ b11)
    elif (b3 = = 3):
        print("Salir... adios")
fonk4()