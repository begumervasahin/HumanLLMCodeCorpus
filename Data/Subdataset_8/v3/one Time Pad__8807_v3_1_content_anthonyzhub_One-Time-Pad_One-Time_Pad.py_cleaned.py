from random import randint
characters = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ,./\\;:"[]{}()_-!@'
def generate_one_time_pads(sheets, length):
    for sheet in range(sheets):
        with open(f"otp{sheet}.txt", "w") as f:
            for _ in range(length):
                f.write(str(randint(0, len(characters) - 1)) + "\n")
def load_sheet(filename):
    with open(filename, "r") as f:
        contents = f.read().splitlines()
    return contents
def get_plaintext():
    plain_text = input('Enter your message: ')
    return plain_text
def load_file(filename):
    with open(filename, 'r') as f:
        contents = f.read()
    return contents
def save_file(filename, data):
    with open(filename, 'w') as f:
        f.write(data)
def encrypt(plaintext, sheet):
    ciphertext = ''
    for position, character in enumerate(plaintext):
        if character not in characters:
            ciphertext += character
        else:
            encrypted = (characters.index(character) + int(sheet[position])) % len(characters)
            ciphertext += characters[encrypted]
    return ciphertext
def decrypt(ciphertext, sheet):
    plaintext = ''
    for position, character in enumerate(ciphertext):
        if character not in characters:
            plaintext += character
        else:
            decrypted = (characters.index(character) - int(sheet[position])) % len(characters)
            plaintext += characters[decrypted]
    return plaintext
def menu():
    while True:
        print('1. Generate one-time pads')
        print('2. Encrypt a message')
        print('3. Decrypt a message')
        print('4. Quit program')
        choice = input('Enter number: ')
        if choice == '1':
            sheets = int(input('How many OTPs should be generated? '))
            length = int(input('What will be the maximum message length? '))
            generate_one_time_pads(sheets, length)
        elif choice == '2':
            filename = input('Enter filename of the OTP you want to use: ')
            sheet = load_sheet(filename)
            plaintext = get_plaintext()
            ciphertext = encrypt(plaintext, sheet)
            filename = input('Enter name of encrypted file: ')
            save_file(filename, ciphertext)
        elif choice == '3':
            filename = input('Enter filename of the OTP you want to use: ')
            sheet = load_sheet(filename)
            filename = input('Type the name of the file to be decrypted: ')
            ciphertext = load_file(filename)
            plaintext = decrypt(ciphertext, sheet)
            print('Decrypted Message: \n' + plaintext)
        elif choice == '4':
            break
menu()