import string
import secrets
def generate_random_shift(length):
    return [secrets.randbelow(26) for _ in range(length)]
def encrypt(message, shift):
    encryption = ""
    shift_index = 0
    for char in message:
        if char in string.ascii_uppercase:
            index = string.ascii_uppercase.index(char)
            new_index = (index + shift[shift_index]) % 26
            encryption += string.ascii_uppercase[new_index]
            shift_index += 1
    return encryption
def decrypt(encryption, shift):
    decryption_shift = [(26 - s) % 26 for s in shift]
    decryption = encrypt(encryption, decryption_shift)
    return decryption
def main():
    print("Welcome to the One-Time Pad Cipher.\n")
    message = "Thanks for taking a look at my one-time pad cipher!"
    non_letters = string.punctuation + string.whitespace + string.digits
    table = str.maketrans({key: None for key in non_letters})
    cleaned_message = message.translate(table)
    shift = generate_random_shift(len(cleaned_message))
    print("Shifting the input by this list:", shift)
    encryption = encrypt(cleaned_message.upper(), shift)
    print("\nYour encrypted message is:\n", encryption, sep="")
    decryption = decrypt(encryption, shift)
    print("Your decrypted message is:\n", decryption, sep="")
if __name__ == "__main__":
    main()