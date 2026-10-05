import string
import secrets
def encrypt(message, shift):
    encryption = ""
    for char, s in zip(message, shift):
        if char.isalpha():
            char_index = string.ascii_uppercase.index(char.upper())
            encrypted_index = (char_index + s) % 26
            encrypted_char = string.ascii_uppercase[encrypted_index]
            encryption += encrypted_char
    return encryption
def decrypt(encryption, shift):
    decryption_shift = [26 - s for s in shift]
    decryption = encrypt(encryption, decryption_shift)
    return decryption
def main():
    print("Welcome to the One-Time Pad Cipher.\n")
    message = "Thanks for taking a look at my one-time pad cipher!"
    message = message.upper().translate(str.maketrans("", "", string.punctuation + string.whitespace + string.digits))
    shifts = [secrets.randbelow(26) for _ in range(len(message))]
    print("Shift values:", shifts)
    encrypted_message = encrypt(message, shifts)
    print("\nEncrypted message:\n", encrypted_message, sep="")
    decrypted_message = decrypt(encrypted_message, shifts)
    print("\nDecrypted message:\n", decrypted_message, sep="")
if __name__ == "__main__":
    main()