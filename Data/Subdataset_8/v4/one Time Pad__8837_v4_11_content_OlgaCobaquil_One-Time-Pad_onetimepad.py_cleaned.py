import random
import binascii
def string_to_bits(message):
    encoding = 'utf-8'
    encoded_message = message.encode(encoding)
    hex_representation = int(binascii.hexlify(encoded_message), 16)
    binary_representation = bin(hex_representation)[2:]
    return binary_representation.zfill(8 * ((len(binary_representation) + 7)
def bits_to_string(message):
    encoding = 'utf-8'
    decimal_value = int(message, 2)
    hex_string = '%x' % decimal_value
    padded_hex_string = hex_string.zfill(len(hex_string) + (len(hex_string) & 1))
    decoded_message = binascii.unhexlify(padded_hex_string)
    return decoded_message.decode(encoding)
def one_time_pad(length):
    return bin(random.getrandbits(length))[2:].zfill(length)
def xor(bit_string1, bit_string2, length):
    result = ['0' if bit_string1[i] == bit_string2[i] else '1' for i in range(length)]
    return ''.join(result)
def main():
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    option = int(input("Enter the option you want to perform: "))
    if option == 1:
        print("\n+-----------Encryption-----------+")
        message = input("Enter the message to encrypt: ")
        binary_message = string_to_bits(message)
        print("\nBinary Representation: \n" + binary_message)
        binary_length = len(binary_message)
        one_time_pad_key = one_time_pad(binary_length)
        print("\nOne-Time Pad Key: \n" + one_time_pad_key)
        encrypted_result = xor(binary_message, one_time_pad_key, binary_length)
        print("\nEncrypted Message: \n" + encrypted_result)
    elif option == 2:
        print("\n+-----------Decryption-----------+")
        encrypted_message = input("Enter the encrypted message: ")
        decryption_key = input("Enter the decryption key: ")
        message_length = len(encrypted_message)
        decrypted_result = xor(encrypted_message, decryption_key, message_length)
        decrypted_message = bits_to_string(decrypted_result)
        print("\nThe decrypted message is: " + decrypted_message)
    elif option == 3:
        print("Exiting... Goodbye!")
if __name__ == "__main__":
    main()