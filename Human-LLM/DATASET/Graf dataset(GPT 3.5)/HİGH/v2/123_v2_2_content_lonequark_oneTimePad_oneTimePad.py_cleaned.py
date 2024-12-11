import random
def fonk1(string, b4):
    b1 = []
    for char in string:
        b2 = ord(char)
        if b2 in b4:
            b1.append(b2)
    return b1
def fonk2(b1):
    b3 = ""
    for b2 in b1:
        b3 += chr(b2)
    return b3
def fonk3():
    b4 = list(range(32, 127))
    print('Write your message. Only ASCII characters in the range 32-126 are accepted.')
    b5 = input("> ")
    print('Name your b10 output file, excluding the .txt extension. For example: message1')
    print('The corresponding b8 will have "b8" appended to the filename. For example: message1key')
    b6 = input("> ")
    b7 = fonk1(b5, b4)
    b8 = [random.choice(b4) for _ in range(len(b7))]
    b9 = [(b7[i] - b4[0] + b8[i] - b4[0]) % len(b4) + b4[0] for i in range(len(b7))]
    b10 = fonk2(b9)
    b8 = fonk2(b8)
    b11 = b6 + ".txt"
    with open(b11, "w") as file:
        file.write(b10)
    b12 = b6 + "b8.txt"
    with open(b12, "w") as file:
        file.write(b8)
def fonk4():
    b4 = list(range(32, 127))
    print('Enter the name of the b10 file, excluding the extension.')
    b13 = input('> ')
    print('Enter the name of the b8 file, excluding the extension.')
    b12 = input('> ')
    with open(b13 + ".txt", "r") as file:
        b10 = file.read()
    with open(b12 + ".txt", "r") as file:
        b8 = file.read()
    b9 = fonk1(b10, b4)
    b14 = fonk1(b8, b4)
    b7 = [(b9[i] - b4[0] - b14[i] + b4[0]) % len(b4) + b4[0] for i in range(len(b9))]
    b5 = fonk2(b7)
    b15 = b13 + "plain.txt"
    with open(b15, "w") as file:
        file.write(b5)
while True:
    print('Choose a b16:\n (1) Encrypt a message\n (2) Decrypt files\n (3) Quit')
    b16 = int(input('> '))
    if b16 = = 1:
        fonk3()
        print('Encryption successful.\n\n')
    elif b16 = = 2:
        fonk4()
        print('Decryption successful. Note: spaces may be removed!\n\n')
    else:
        print('Goodbye.')
        break