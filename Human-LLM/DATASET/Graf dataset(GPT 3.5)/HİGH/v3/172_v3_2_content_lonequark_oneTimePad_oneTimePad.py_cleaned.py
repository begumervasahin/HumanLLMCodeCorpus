import random
def fonk1(string, b3):
    b1 = [ord(char) for char in string if ord(char) in b3]
    return b1
def fonk2(b1):
    b2 = ''.join(chr(num) for num in b1)
    return b2
def fonk3():
    b3 = list(range(32, 127))
    print('Write your message. Only ASCII characters in the range 32-126 are accepted.')
    b4 = input("> ")
    print('Name your b9 output file, excluding the .txt extension. For example: message1')
    print('The corresponding b7 will have "b7" appended to the filename. For example: message1key')
    b5 = input("> ")
    b6 = fonk1(b4, b3)
    b7 = [random.choice(b3) for _ in range(len(b6))]
    b8 = [(plain - b3[0] + k - b3[0]) % len(b3) + b3[0]
                        for plain, k in zip(b6, b7)]
    b9 = fonk2(b8)
    b7 = fonk2(b7)
    with open(b5 + ".txt", "w") as file:
        file.write(b9)
    with open(b5 + "b7.txt", "w") as file:
        file.write(b7)
def fonk4():
    b3 = list(range(32, 127))
    print('Enter the name of the b9 file, excluding the extension.')
    b10 = input('> ')
    print('Enter the name of the b7 file, excluding the extension.')
    b11 = input('> ')
    with open(b10 + ".txt", "r") as file:
        b9 = file.read()
    with open(b11 + ".txt", "r") as file:
        b7 = file.read()
    b8 = fonk1(b9, b3)
    b12 = fonk1(b7, b3)
    b6 = [(cipher - b3[0] - k + b3[0]) % len(b3) + b3[0]
                        for cipher, k in zip(b8, b12)]
    b4 = fonk2(b6)
    with open(b10 + "plain.txt", "w") as file:
        file.write(b4)
while True:
    print('Choose a b13:\n (1) Encrypt a message\n (2) Decrypt files\n (3) Quit')
    b13 = int(input('> '))
    if b13 = = 1:
        fonk3()
        print('Encryption successful.\n\n')
    elif b13 = = 2:
        fonk4()
        print('Decryption successful. Note: spaces may be removed!\n\n')
    else:
        print('Goodbye.')
        break