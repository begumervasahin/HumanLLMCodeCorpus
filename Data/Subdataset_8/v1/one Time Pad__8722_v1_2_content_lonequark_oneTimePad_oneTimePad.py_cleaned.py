import random
def stringToASCII(string, accept):
    listOut = []
    for char in string:
        num = ord(char)
        if num in accept:
            listOut.append(num)
    return listOut
def ASCIIToString(listIn):
    stringOut = ""
    for num in listIn:
        stringOut += chr(num)
    return stringOut
def encrypt():
    accept = list(range(32, 127))
    print('Write your message. ASCII characters 32-126 accepted.')
    plain = input("> ")
    print('Name your ciphertext output file, excluding .txt extension. For example: message1')
    print('The corresponding key will be the name with "key" appended. For example: message1key')
    fileName = input("> ")
    plainASCII = stringToASCII(plain, accept)
    key = [random.choice(accept) for _ in range(len(plainASCII))]
    cipherASCII = [(plainASCII[i] - accept[0] + key[i] - accept[0]) % len(accept) + accept[0] for i in range(len(plainASCII))]
    cipher = ASCIIToString(cipherASCII)
    key = ASCIIToString(key)
    newfileName = fileName + ".txt"
    with open(newfileName, "w") as file:
        file.write(cipher)
    keyFile = fileName + "key.txt"
    with open(keyFile, "w") as file:
        file.write(key)
def decrypt():
    accept = list(range(32, 127))
    print('Enter the name of the ciphertext file, excluding the extension.')
    cipherFile = input('> ')
    print('Enter the name of the key file, excluding the extension.')
    keyFile = input('> ')
    with open(cipherFile + ".txt", "r") as file:
        cipher = file.read()
    with open(keyFile + ".txt", "r") as file:
        key = file.read()
    cipherASCII = stringToASCII(cipher, accept)
    keyASCII = stringToASCII(key, accept)
    plainASCII = [(cipherASCII[i] - accept[0] - keyASCII[i] + accept[0]) % len(accept) + accept[0] for i in range(len(cipherASCII))]
    plain = ASCIIToString(plainASCII)
    plainFileName = cipherFile + "plain.txt"
    with open(plainFileName, "w") as file:
        file.write(plain)
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