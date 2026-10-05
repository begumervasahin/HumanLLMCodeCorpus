import random
import binascii
def string_to_bits(message):
    encoding = 'utf8'
    enc_message = message.encode(encoding)
    int_hex = int(binascii.hexlify(enc_message), 16)
    binary_string = bin(int_hex)[2:]
    return binary_string.zfill(8 * ((len(binary_string) + 7)
def bits_to_string(message):
    encoding = 'utf8'
    n = int(message, 2)
    hex_string = '%x' % n
    k = len(hex_string)
    sol = binascii.unhexlify(hex_string.zfill(k + (k & 1)))
    return sol.decode(encoding)
def one_time_pad(length):
    return bin(random.getrandbits(length))[2:].zfill(length)
def xor(list1, list2, length):
    result = []
    for i in range(length):
        if list1[i] == list2[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)
def main():
    while True:
        print("\n1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        option = input("Enter the option you want to perform: ")
        if option == '1':
            print("\n+-----------Encrypt-----------+")
            message = input("Enter the message to encrypt: ")
            binary_string = string_to_bits(message)
            print("\nBinary String:\n" + binary_string)
            binary_length = len(binary_string)
            random_pad = one_time_pad(binary_length)
            print("\nOne-time pad:\n" + str(random_pad))
            result = xor(binary_string, random_pad, binary_length)
            print("\nEncrypted Message:\n" + str(result))
        elif option == '2':
            print("\n+-----------Decrypt-----------+")
            ciphertext = input("Enter the encrypted string: ")
            input_key = input("Key: ")
            length = len(ciphertext)
            result = xor(ciphertext, input_key, length)
            final_message = bits_to_string(result)
            print("\nThe decrypted message is: " + final_message)
        elif option == '3':
            print("Exiting... Goodbye")
            break
        else:
            print("Invalid option! Please enter a valid option.")
if __name__ == "__main__":
    main()