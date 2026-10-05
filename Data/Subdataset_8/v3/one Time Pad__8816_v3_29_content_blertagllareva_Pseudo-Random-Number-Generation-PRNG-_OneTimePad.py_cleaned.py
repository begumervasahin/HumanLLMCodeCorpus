def char_to_num(char):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet.index(char) + 1
def num_to_char(num):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet[num - 1]
def encode_char(plain_char, key_char):
    plain_num = char_to_num(plain_char)
    key_num = char_to_num(key_char)
    cipher_num = (plain_num + key_num - 1) % 26 + 1
    return num_to_char(cipher_num)
def decode_char(cipher_char, key_char):
    cipher_num = char_to_num(cipher_char)
    key_num = char_to_num(key_char)
    plain_num = (cipher_num - key_num - 1) % 26 + 1
    return num_to_char(plain_num)
def encode(plain_text, key):
    cipher_text = ""
    for plain_char, key_char in zip(plain_text, key):
        cipher_text += encode_char(plain_char, key_char)
    return cipher_text
def decode(cipher_text, key):
    plain_text = ""
    for cipher_char, key_char in zip(cipher_text, key):
        plain_text += decode_char(cipher_char, key_char)
    return plain_text
def main():
    print("OneTimePad Program. The key must be shorter or equal to the plain text. The plain text should not contain numbers.")
    print("\nOptions:\n1: Encoding\n2: Decoding\n3: Quit")
    while True:
        choice = input(">>> ")
        if choice == "1":
            plain_text = input("Plain text: ")
            key = input("Key: ")
            if len(key) < len(plain_text):
                print("The key must be at least as long as the plain text.")
            else:
                print("Cipher text:", encode(plain_text, key))
        elif choice == "2":
            cipher_text = input("Cipher text: ")
            key = input("Key: ")
            if len(key) < len(cipher_text):
                print("The key must be at least as long as the cipher text.")
            else:
                print("Plain text:", decode(cipher_text, key))
        elif choice == "3":
            break
        else:
            print("Please choose 1, 2, or 3.")
if __name__ == "__main__":
    main()