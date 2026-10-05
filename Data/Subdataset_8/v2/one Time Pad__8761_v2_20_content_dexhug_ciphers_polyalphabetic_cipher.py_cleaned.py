import string
def encrypt(message, shift):
    encryption = ""
    counter = 0
    for char in message:
        if char.isalpha():
            shifted_index = (string.ascii_uppercase.index(char) + shift[counter]) % 26
            encrypted_char = string.ascii_uppercase[shifted_index]
            encryption += encrypted_char
            counter = (counter + 1) % len(shift)
        else:
            encryption += char
    return encryption
def decrypt(encryption, shift):
    dec_shift = [(26 - s) % 26 for s in shift]
    return encrypt(encryption, dec_shift)
def main():
    print("Welcome to the Polyalphabetic Cipher.\n")
    shift_word = "encrypt"
    message = "Thanks for taking a look at my polyalphabetic cipher!"
    shift_word = ''.join(char.upper() for char in shift_word if char.isalpha())
    message = ''.join(char.upper() for char in message if char.isalpha())
    shift = [(ord(char) - ord('A') + 1) for char in shift_word]
    print("Shifting the input by this list:", shift)
    print("Message to be encrypted:\n", message)
    encryption = encrypt(message, shift)
    print("\nYour encrypted message is:\n", encryption)
    decryption = decrypt(encryption, shift)
    print("Your decrypted message is:\n", decryption)
if __name__ == "__main__":
    main()