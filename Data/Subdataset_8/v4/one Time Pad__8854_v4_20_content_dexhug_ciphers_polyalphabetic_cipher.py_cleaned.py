
import string
def encrypt(message, shift):
    encryption = ""
    counter = 0
    for char in message:
        if char in string.ascii_uppercase:
            index = string.ascii_uppercase.find(char)
            shifted_index = (index + shift[counter]) % 26
            encryption += string.ascii_uppercase[shifted_index]
            counter = (counter + 1) % len(shift)
        elif char in string.digits:
            encryption += char
        elif char in string.whitespace:
            encryption += char
    return encryption
def decrypt(encryption, shift):
    decryption = ""
    dec_shift = [(26 - s) % 26 for s in shift]
    for char in encryption:
        if char in string.ascii_uppercase:
            index = string.ascii_uppercase.find(char)
            shifted_index = (index + dec_shift[0]) % 26
            decryption += string.ascii_uppercase[shifted_index]
            dec_shift.append(dec_shift.pop(0))
        else:
            decryption += char
    return decryption
def Main():
    print("Welcome to the Polyalphabetic Cipher.\n")
    shift_word = "encrypt"
    message = "Thanks for taking a look at my polyalphabetic cipher!"
    shift_word = shift_word.translate(str.maketrans('', '', string.punctuation + string.whitespace))
    shift = [(string.ascii_uppercase.find(char) + 1) for char in shift_word.upper()]
    message = message.translate(str.maketrans('', '', string.punctuation))
    print("Shifting the input by this list:", shift)
    print("Message to be encrypted:\n", message, sep="")
    encryption = encrypt(message.upper(), shift)
    print("\nYour encrypted message is:\n", encryption, sep="")
    decryption = decrypt(encryption, shift)
    print("Your decrypted message is:\n", decryption, sep="")
Main()