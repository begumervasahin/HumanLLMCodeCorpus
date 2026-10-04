import random
from util_function import strxor
def read_input():
    message_num = int(input("Enter the number of messages: "))
    message_set = []
    for _ in range(message_num):
        message_set.append(input("Enter message: "))
    return message_set
def encrypt(key, message):
    return strxor(key, message)
def print_single_encrypted(cipher_text):
    cipher_text_hex = "".join("{:02x}".format(ord(char)) for char in cipher_text)
    print(cipher_text_hex)
def main():
    message_set = read_input()
    message_num = len(message_set)
    max_size = 2 * len(max(message_set, key=len))
    random_ascii = [hex(random.randint(0, 15)).split('x')[-1] for _ in range(max_size)]
    key = ''.join(random_ascii)
    print("Number of messages:", message_num)
    for message in message_set:
        cipher_text = encrypt(key, message)
        print_single_encrypted(cipher_text)
if __name__ == "__main__":
    main()