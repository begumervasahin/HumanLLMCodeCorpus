
import random
import binascii
def string_to_bits(message):
    """ ord -> unicode
        format -> binario
    return "".join(seven_bits(format(ord(x), 'b')) for x in message)
    return ''.join(chr(int(message[i*8:i*8+8],2)) for i in range(len(message)
def one_time_pad(ln):
    return bin(random.getrandbits(ln))[2:].zfill(ln)
def xor(lista1, lista2,ln):
    result = []
    for i in range(ln):
        if (lista1[i] == lista2[i]):
            result.append('0')
        else:
            result.append('1')
    cadena = ''.join(result)
    return cadena
def main():
    print(" 1. Cifrar ")
    print(" 2. Descifrar")
    print(" 3. Salir")
    op = input("Ingrese la opcion que desea realizar: ")
    if (op == 1):
        print("\n+-----------Cifrar-----------+")
        msj = raw_input("Ingrese el mensaje a cifrar: ")
        cadena_binario = string_to_bits(msj)
        print("\nCadena Binaria: \n" + cadena_binario)
        len_binario = len(cadena_binario)
        cadena_random = one_time_pad(len_binario)
        print("\nOne time pad: \n" + str(cadena_random))
        result = xor(cadena_binario, cadena_random, len_binario)
        print("\nCifrado: \n" + str(result))
    elif (op == 2):
        print("\n+-----------Descifrar-----------+")
        cfr = raw_input("Ingresar la cadena cifrada: ")
        in_key = raw_input("Key: ")
        tm = len(cfr)
        result = xor(cfr, in_key,tm)
        final_msj = bits_to_string(result)
        print("\nEl mensaje es: "+ final_msj)
    elif (op == 3):
        print("Salir... adios")
main()