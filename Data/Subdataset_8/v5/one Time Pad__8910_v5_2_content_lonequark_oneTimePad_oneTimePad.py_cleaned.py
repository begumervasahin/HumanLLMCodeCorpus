import random
accepted_ascii_range = range(32, 127)
def string_to_ascii(string, accepted_range):
    return [ord(char) for char in string if ord(char) in accepted_range]
def ascii_to_string(ascii_list):
    return ''.join(chr(num) for num in ascii_list)
def generate_key(length, accepted_range):
    return [random.choice(accepted_range) for _ in range(length)]
def encrypt_message(plain_text, key, accepted_range):
    cipher_text_ascii = []
    for plain_char, key_char in zip(plain_text, key):
        encrypted = ((plain_char - accepted_range[0]) + (key_char - accepted_range[0])) % len(accepted_range) + accepted_range[0]
        cipher_text_ascii.append(encrypted)
    return ascii_to_string(cipher_text_ascii)
def decrypt_message(cipher_text, key, accepted_range):
    plain_text_ascii = []
    for cipher_char, key_char in zip(cipher_text, key):
        decrypted = ((cipher_char - accepted_range[0]) - (key_char - accepted_range[0])) % len(accepted_range) + accepted_range[0]
        plain_text_ascii.append(decrypted)
    return ascii_to_string(plain_text_ascii)
def encrypt():
    print('Write your message. ASCII characters 32-126 accepted.')
    plain_text = input("> ")
    print('Name your ciphertext output file, excluding .txt extension. For example: message1')
    print('The corresponding key will be the name with "key" appended. For example: message1key')
    file_name = input("> ")
    plain_text_ascii = string_to_ascii(plain_text, accepted_ascii_range)
    key = generate_key(len(plain_text_ascii), accepted_ascii_range)
    cipher_text = encrypt_message(plain_text_ascii, key, accepted_ascii_range)
    with open(f"{file_name}.txt", "w") as cipher_file:
        cipher_file.write(cipher_text)
    key_text = ascii_to_string(key)
    with open(f"{file_name}key.txt", "w") as key_file:
        key_file.write(key_text)
def decrypt():
    print('Enter the name of the ciphertext file, excluding the extension.')
    cipher_file_name = input('> ')
    print('Enter the name of the key file, excluding the extension.')
    key_file_name = input('> ')
    with open(f"{cipher_file_name}.txt", "r") as cipher_file:
        cipher_text = cipher_file.read()
    with open(f"{key_file_name}.txt", "r") as key_file:
        key_text = key_file.read()
    cipher_text_ascii = string_to_ascii(cipher_text, accepted_ascii_range)
    key_ascii = string_to_ascii(key_text, accepted_ascii_range)
    plain_text = decrypt_message(cipher_text_ascii, key_ascii, accepted_ascii_range)
    with open(f"{cipher_file_name}plain.txt", "w") as plain_file:
        plain_file.write(plain_text)
while True:
    print('Choose a mode:\n (1) Encrypt a message\n (2) Decrypt files\n (3) Quit')
    mode = int(input('> '))
    if mode == 1:
        encrypt()
        print('Encryption successful.\n\n')
    elif mode == 2:
        decrypt()
        print('Decryption successful. Remember that the spaces are gone!\n\n')
    else:
        print('Goodbye.')
        break