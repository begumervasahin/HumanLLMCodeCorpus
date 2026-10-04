import random
from util_function import strxor
def read_input():
    message_num = int(input("Enter the number of messages: "))
    return [input("Enter message: ") for _ in range(message_num)]
def encrypt(key, message):
    return strxor(key, message)
def print_single_encrypted(cipher_text):
    cipher_text_hex = "".join(f"{ord(char):02x}" for char in cipher_text)
    print(cipher_text_hex)
def generate_random_key(length):
    return ''.join(chr(random.randint(0, 255)) for _ in range(length))
def main():
    message_set = read_input()
    max_size = max(len(message) for message in message_set)
    key = generate_random_key(max_size)
    print("Number of messages:", len(message_set))
    for message in message_set:
        cipher_text = encrypt(key, message)
        print_single_encrypted(cipher_text)
if __name__ == "__main__":
    main()