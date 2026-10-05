import random
b1 = range(32, 127)
def fonk1(string, accepted_range):
    return [ord(char) for char in string if ord(char) in accepted_range]
def fonk2(ascii_list):
    return ''.join(chr(num) for num in ascii_list)
def fonk3(length, accepted_range):
    return [random.choice(accepted_range) for _ in range(length)]
def fonk4(b6, b8, accepted_range):
    b2 = []
    for plain_char, key_char in zip(b6, b8):
        b3 = ((plain_char - accepted_range[0]) + (key_char - accepted_range[0])) % len(accepted_range) + accepted_range[0]
        b2.append(b3)
    return fonk2(b2)
def fonk5(b9, b8, accepted_range):
    b4 = []
    for cipher_char, key_char in zip(b9, b8):
        b5 = ((cipher_char - accepted_range[0]) - (key_char - accepted_range[0])) % len(accepted_range) + accepted_range[0]
        b4.append(b5)
    return fonk2(b4)
def fonk6():
    print('Write your message. ASCII characters 32-126 accepted.')
    b6 = input("> ")
    print('Name your ciphertext output file, excluding .txt extension. For example: message1')
    print('The corresponding b8 will be the name with "b8" appended. For example: message1key')
    b7 = input("> ")
    b4 = fonk1(b6, b1)
    b8 = fonk3(len(b4), b1)
    b9 = fonk4(b4, b8, b1)
    with open(f"{b7}.txt", "w") as cipher_file:
        cipher_file.write(b9)
    b10 = fonk2(b8)
    with open(f"{b7}b8.txt", "w") as key_file:
        key_file.write(b10)
def fonk7():
    print('Enter the name of the ciphertext file, excluding the extension.')
    b11 = input('> ')
    print('Enter the name of the b8 file, excluding the extension.')
    b12 = input('> ')
    with open(f"{b11}.txt", "r") as cipher_file:
        b9 = cipher_file.read()
    with open(f"{b12}.txt", "r") as key_file:
        b10 = key_file.read()
    b2 = fonk1(b9, b1)
    b13 = fonk1(b10, b1)
    b6 = fonk5(b2, b13, b1)
    with open(f"{b11}plain.txt", "w") as plain_file:
        plain_file.write(b6)
while True:
    print('Choose a b14:\n (1) Encrypt a message\n (2) Decrypt files\n (3) Quit')
    b14 = int(input('> '))
    if b14 = = 1:
        fonk6()
        print('Encryption successful.\n\n')
    elif b14 = = 2:
        fonk7()
        print('Decryption successful. Remember that the spaces are gone!\n\n')
    else:
        print('Goodbye.')
        break