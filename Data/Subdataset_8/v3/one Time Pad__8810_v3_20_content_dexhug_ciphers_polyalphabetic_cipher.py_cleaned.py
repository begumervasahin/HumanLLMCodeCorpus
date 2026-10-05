import string
def clean_input(text):
    return ''.join(char.upper() for char in text if char.isalpha())
def calculate_shift(shift_word):
    return [(ord(char) - ord('A') + 1) for char in shift_word]
def shift_character(char, shift):
    if char.isalpha():
        shifted_index = (string.ascii_uppercase.index(char) + shift) % 26
        return string.ascii_uppercase[shifted_index]
    return char
def apply_shift(message, shift_list):
    encryption = ""
    counter = 0
    for char in message:
        shift = shift_list[counter % len(shift_list)]
        encryption += shift_character(char, shift)
        if char.isalpha():
            counter += 1
    return encryption
def encrypt(message, shift_word):
    cleaned_message = clean_input(message)
    cleaned_shift_word = clean_input(shift_word)
    shift_list = calculate_shift(cleaned_shift_word)
    return apply_shift(cleaned_message, shift_list)
def decrypt(encryption, shift_word):
    cleaned_encryption = clean_input(encryption)
    cleaned_shift_word = clean_input(shift_word)
    shift_list = calculate_shift(cleaned_shift_word)
    dec_shift = [(26 - s) % 26 for s in shift_list]
    return apply_shift(cleaned_encryption, dec_shift)
def main():
    print("Welcome to the Polyalphabetic Cipher.\n")
    shift_word = "encrypt"
    message = "Thanks for taking a look at my polyalphabetic cipher!"
    print("Shifting the input by this list:", calculate_shift(shift_word))
    print("Message to be encrypted:\n", message)
    encryption = encrypt(message, shift_word)
    print("\nYour encrypted message is:\n", encryption)
    decryption = decrypt(encryption, shift_word)
    print("Your decrypted message is:\n", decryption)
if __name__ == "__main__":
    main()