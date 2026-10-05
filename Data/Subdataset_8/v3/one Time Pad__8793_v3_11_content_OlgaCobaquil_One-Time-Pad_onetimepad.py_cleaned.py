import random
import binascii
def string_to_bits(message):
    enc_message = message.encode('utf8')
    int_hex = int(binascii.hexlify(enc_message), 16)
    binary_string = bin(int_hex)[2:]
    return binary_string.zfill(8 * ((len(binary_string) + 7)
def bits_to_string(message):
    n = int(message, 2)
    hex_string = '%x' % n
    k = len(hex_string)
    sol = binascii.unhexlify(hex_string.zfill(k + (k & 1)))
    return sol.decode('utf8')
def generate_one_time_pad(length):
    return bin(random.getrandbits(length))[2:].zfill(length)
def xor(list1, list2, length):
    result = ['0' if list1[i] == list2[i] else '1' for i in range(length)]
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
            binary_message = string_to_bits(message)
            print("\nBinary String:\n" + binary_message)
            binary_length = len(binary_message)
            one_time_pad = generate_one_time_pad(binary_length)
            print("\nOne-time pad:\n" + one_time_pad)
            encrypted_message = xor(binary_message, one_time_pad, binary_length)
            print("\nEncrypted Message:\n" + encrypted_message)
        elif option == '2':
            print("\n+-----------Decrypt-----------+")
            ciphertext = input("Enter the encrypted string: ")
            key = input("Key: ")
            length = len(ciphertext)
            decrypted_message = xor(ciphertext, key, length)
            original_message = bits_to_string(decrypted_message)
            print("\nThe decrypted message is: " + original_message)
        elif option == '3':
            print("Exiting... Goodbye")
            break
        else:
            print("Invalid option! Please enter a valid option.")
if __name__ == "__main__":
    main()