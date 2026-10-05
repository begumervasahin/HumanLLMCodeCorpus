import string
def encrypt(message, shift_word):
    encryption = ""
    shift_indices = [string.ascii_uppercase.find(char) + 1 for char in shift_word.upper()]
    counter = 0
    for char in message:
        if char in string.ascii_uppercase:
            index = string.ascii_uppercase.find(char)
            shifted_index = (index + shift_indices[counter]) % 26
            encryption += string.ascii_uppercase[shifted_index]
            counter = (counter + 1) % len(shift_indices)
        else:
            encryption += char
    return encryption
def decrypt(encryption, shift_word):
    decryption = ""
    shift_indices = [(26 - string.ascii_uppercase.find(char)) % 26 for char in shift_word.upper()]
    counter = 0
    for char in encryption:
        if char in string.ascii_uppercase:
            index = string.ascii_uppercase.find(char)
            shifted_index = (index + shift_indices[counter]) % 26
            decryption += string.ascii_uppercase[shifted_index]
            counter = (counter + 1) % len(shift_indices)
        else:
            decryption += char
    return decryption
def main():
    print("Welcome to the Polyalphabetic Cipher.\n")
    shift_word = "encrypt"
    message = "Thanks for taking a look at my polyalphabetic cipher!"
    shift_word = shift_word.translate(str.maketrans('', '', string.punctuation + string.whitespace))
    message = message.translate(str.maketrans('', '', string.punctuation))
    print("Shifting the input by this word:", shift_word)
    print("Message to be encrypted:\n", message, sep="")
    encryption = encrypt(message.upper(), shift_word)
    print("\nYour encrypted message is:\n", encryption, sep="")
    decryption = decrypt(encryption, shift_word)
    print("Your decrypted message is:\n", decryption, sep="")
if __name__ == "__main__":
    main()