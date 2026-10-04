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
def print_single_encrypted(cipher_text):
    cipher_text_hex = "".join(f"{ord(char):02x}" for char in cipher_text)
    print(cipher_text_hex)
def generate_random_key(length):
    random_ascii = [random.choice("0123456789abcdef") for _ in range(length)]
    return ''.join(random_ascii)
def main():
    message_set = read_input()
    max_size = 2 * len(max(message_set, key=len))
    key = generate_random_key(max_size)
    print(f"Number of messages: {len(message_set)}")
    for message in message_set:
        cipher_text = encrypt(key, message)
        print_single_encrypted(cipher_text)
if __name__ == "__main__":
    main()