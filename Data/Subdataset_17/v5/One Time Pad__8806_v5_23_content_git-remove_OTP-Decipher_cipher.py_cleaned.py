import random
from util_function import strxor
def read_input():
    message_set = []
    message_num = int(input("Enter the number of messages: "))
    for _ in range(message_num):
        message_set.append(input("Enter message: "))
    return message_set
def encrypt(key, message):
    return strxor(key, message)
def print_encrypted_hex(cipher_text):
    cipher_text_hex = "".join(f"{ord(char):02x}" for char in cipher_text)
    print(cipher_text_hex)
def generate_random_key(length):
    return ''.join(random.choice("0123456789abcdef") for _ in range(length))
def main():
    message_set = read_input()
    max_message_length = max(len(message) for message in message_set)
    key_length = 2 * max_message_length
    key = generate_random_key(key_length)
    print(f"Number of messages: {len(message_set)}")
    for message in message_set:
        cipher_text = encrypt(key, message)
        print_encrypted_hex(cipher_text)
if __name__ == "__main__":
    main()