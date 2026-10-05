import random
import binascii
def string_to_bits(message):
    encoding = 'utf8'
    enc_msj = message.encode(encoding)
    int_hex = int(binascii.hexlify(enc_msj), 16)
    str_bin = bin(int_hex)[2:]
    return str_bin.zfill(8 * ((len(str_bin) + 7)
def bits_to_string(message):
    encoding = 'utf8'
    n = int(message, 2)
    hex_string = '%x' % n
    k = len(hex_string)
    sol = binascii.unhexlify(hex_string.zfill(k + (k & 1)))
    return sol.decode(encoding)
def one_time_pad(ln):
    return bin(random.getrandbits(ln))[2:].zfill(ln)
def xor(lista1, lista2, ln):
    result = []
    for i in range(ln):
        if lista1[i] == lista2[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)
def main():
    while True:
        print("\n1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        op = input("Enter the option you want to perform: ")
        if op == '1':
            print("\n+-----------Encrypt-----------+")
            msj = input("Enter the message to encrypt: ")
            cadena_binario = string_to_bits(msj)
            print("\nBinary String: \n" + cadena_binario)
            len_binario = len(cadena_binario)
            cadena_random = one_time_pad(len_binario)
            print("\nOne-time pad: \n" + str(cadena_random))
            result = xor(cadena_binario, cadena_random, len_binario)
            print("\nEncrypted Message: \n" + str(result))
        elif op == '2':
            print("\n+-----------Decrypt-----------+")
            cfr = input("Enter the encrypted string: ")
            in_key = input("Key: ")
            tm = len(cfr)
            result = xor(cfr, in_key, tm)
            final_msj = bits_to_string(result)
            print("\nThe decrypted message is: " + final_msj)
        elif op == '3':
            print("Exiting... Goodbye")
            break
        else:
            print("Invalid option! Please enter a valid option.")
if __name__ == "__main__":
    main()