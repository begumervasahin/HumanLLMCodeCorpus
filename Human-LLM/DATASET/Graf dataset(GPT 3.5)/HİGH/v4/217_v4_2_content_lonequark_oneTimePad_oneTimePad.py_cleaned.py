import random
b1 = range(32, 127)
def fonk1(string, accepted_range):
    b2 = []
    for char in string:
        b3 = ord(char)
        if b3 in accepted_range:
            b2.append(b3)
    return b2
def fonk2(b2):
    return ''.join(chr(num) for num in b2)
def fonk3():
    print('Write your message. ASCII characters 32-126 accepted.')
    b4 = raw_input("> ")
    print('Name your ciphertext output file, excluding .txt extension. For example: message1')
    print('The corresponding b7 will be the name with "b7" appended. For example: message1key')
    b5 = raw_input("> ")
    b6 = fonk1(b4, b1)
    b7 = [random.choice(b1) for _ in range(len(b6))]
    b8 = []
    for i in range(len(b6)):
        b9 = ((b6[i] - b1[0]) + (b7[i] - b1[0]) % len(b1)) + b1[0]
        b8.append(b9)
    b10 = fonk2(b8)
    b11 = fonk2(b7)
    b12 = b5 + ".txt"
    with open(b12, "w") as b14:
        b14.write(b10)
    b13 = b5 + "b7.txt"
    with open(b13, "w") as b15:
        b15.write(b11)
def fonk4():
    print('Enter the name of the ciphertext file, excluding the extension.')
    b14 = raw_input('> ')
    print('Enter the name of the b7 file, excluding the extension.')
    b15 = raw_input('> ')
    with open(b14 + ".txt", "r") as b14:
        b10 = b14.read()
    with open(b15 + ".txt", "r") as b15:
        b11 = b15.read()
    b8 = fonk1(b10, b1)
    b16 = fonk1(b11, b1)
    b6 = []
    for i in range(len(b8)):
        b17 = ((b8[i] - b1[0]) - (b16[i] - b1[0])) % len(b1) + b1[0]
        b6.append(b17)
    b4 = fonk2(b6)
    b18 = b14 + "plain.txt"
    with open(b18, "w") as plain_file:
        plain_file.write(b4)
while True:
    print('Choose a b19:\n (1) Encrypt a message\n (2) Decrypt files\n (3) Quit')
    b19 = int(raw_input('> '))
    if b19 = = 1:
        fonk3()
        print('Encryption successful.\n\n')
    elif b19 = = 2:
        fonk4()
        print('Decryption successful. Remember that the spaces are gone!\n\n')
    else:
        print('Goodbye.')
        break