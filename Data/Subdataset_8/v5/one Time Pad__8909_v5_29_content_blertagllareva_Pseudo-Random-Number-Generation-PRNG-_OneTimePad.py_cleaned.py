def char_to_num(char):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet.index(char.lower()) + 1
def num_to_char(num):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet[num - 1]
def encode_char(plain_text_char, key_char):
    p_num = char_to_num(plain_text_char)
    k_num = char_to_num(key_char)
    c_num = (p_num + k_num - 1) % 26 + 1
    return num_to_char(c_num)
def decode_char(cipher_text_char, key_char):
    c_num = char_to_num(cipher_text_char)
    k_num = char_to_num(key_char)
    p_num = (c_num - k_num - 1) % 26 + 1
    return num_to_char(p_num)
def encode(plain_text, key):
    cipher_text = ""
    for p_char, k_char in zip(plain_text, key):
        cipher_text += encode_char(p_char, k_char)
    return cipher_text
def decode(cipher_text, key):
    plain_text = ""
    for c_char, k_char in zip(cipher_text, key):
        plain_text += decode_char(c_char, k_char)
    return plain_text
def main():
    print("One-Time Pad Program. The key must be smaller or equal in length to the plain text. The plain text should not contain numbers.")
    print("\nOptions:\n1: Encode\n2: Decode\n3: Exit")
    while True:
        choice = input(">>> ")
        if choice == "1":
            plain_text = input("Plain text: ")
            key = input("Key: ")
            print("Cipher text:", encode(plain_text, key))
        elif choice == "2":
            cipher_text = input("Cipher text: ")
            key = input("Key: ")
            print("Plain text:", decode(cipher_text, key))
        elif choice == "3":
            break
        else:
            print("Please choose 1, 2, or 3")
if __name__ == "__main__":
    main()