import random
from util_function import strxor
def read_input():
    message_num = int(input("Enter the number of messages: "))
    message_set = [input("Enter message: ") for _ in range(message_num)]
    return message_set
def encrypt(key, message):
    return strxor(key, message)
def print_single_encrypted(cipher_text):
    cipher_text_hex = "".join(f"{ord(char):02x}" for char in cipher_text)
    print(cipher_text_hex)
def generate_random_key(length):
    random_ascii = [chr(random.randint(0, 255)) for _ in range(length)]
    return ''.join(random_ascii)
def main():
    message_set = read_input()
    message_num = len(message_set)
    max_size = len(max(message_set, key=len))
    key = generate_random_key(max_size)
    print("Number of messages:", message_num)
    for message in message_set:
        cipher_text = encrypt(key, message)
        print_single_encrypted(cipher_text)
if __name__ == "__main__":
    main()