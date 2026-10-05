import random
accepted_ascii_range = range(32, 127)
def string_to_ascii(string, accepted_range):
    ascii_list = []
    for char in string:
        ascii_val = ord(char)
        if ascii_val in accepted_range:
            ascii_list.append(ascii_val)
    return ascii_list
def ascii_to_string(ascii_list):
    return ''.join(chr(num) for num in ascii_list)
def encrypt():
    print('Write your message. ASCII characters 32-126 accepted.')
    plain_text = raw_input("> ")
    print('Name your ciphertext output file, excluding .txt extension. For example: message1')
    print('The corresponding key will be the name with "key" appended. For example: message1key')
    file_name = raw_input("> ")
    plain_text_ascii = string_to_ascii(plain_text, accepted_ascii_range)
    key = [random.choice(accepted_ascii_range) for _ in range(len(plain_text_ascii))]
    cipher_text_ascii = []
    for i in range(len(plain_text_ascii)):
        encrypted = ((plain_text_ascii[i] - accepted_ascii_range[0]) + (key[i] - accepted_ascii_range[0]) % len(accepted_ascii_range)) + accepted_ascii_range[0]
        cipher_text_ascii.append(encrypted)
    cipher_text = ascii_to_string(cipher_text_ascii)
    key_text = ascii_to_string(key)
    cipher_file_name = file_name + ".txt"
    with open(cipher_file_name, "w") as cipher_file:
        cipher_file.write(cipher_text)
    key_file_name = file_name + "key.txt"
    with open(key_file_name, "w") as key_file:
        key_file.write(key_text)
def decrypt():
    print('Enter the name of the ciphertext file, excluding the extension.')
    cipher_file = raw_input('> ')
    print('Enter the name of the key file, excluding the extension.')
    key_file = raw_input('> ')
    with open(cipher_file + ".txt", "r") as cipher_file:
        cipher_text = cipher_file.read()
    with open(key_file + ".txt", "r") as key_file:
        key_text = key_file.read()
    cipher_text_ascii = string_to_ascii(cipher_text, accepted_ascii_range)
    key_ascii = string_to_ascii(key_text, accepted_ascii_range)
    plain_text_ascii = []
    for i in range(len(cipher_text_ascii)):
        decrypted = ((cipher_text_ascii[i] - accepted_ascii_range[0]) - (key_ascii[i] - accepted_ascii_range[0])) % len(accepted_ascii_range) + accepted_ascii_range[0]
        plain_text_ascii.append(decrypted)
    plain_text = ascii_to_string(plain_text_ascii)
    plain_file_name = cipher_file + "plain.txt"
    with open(plain_file_name, "w") as plain_file:
        plain_file.write(plain_text)
while True:
    print('Choose a mode:\n (1) Encrypt a message\n (2) Decrypt files\n (3) Quit')
    mode = int(raw_input('> '))
    if mode == 1:
        encrypt()
        print('Encryption successful.\n\n')
    elif mode == 2:
        decrypt()
        print('Decryption successful. Remember that the spaces are gone!\n\n')
    else:
        print('Goodbye.')
        break