def char_to_num(char):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    num = 1
    for letter in alphabet:
        if letter == char:
            break
        else:
            num += 1
    return num
def num_to_char(num):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet[num - 1]
def encode_char(plain_text_char, key_char):
    c_num = (char_to_num(plain_text_char) + char_to_num(key_char)) % 26
    c_text = num_to_char(c_num)
    return c_text
def decode_char(cipher_text_char, key_char):
    p_num = char_to_num(cipher_text_char) - char_to_num(key_char)
    p_text = num_to_char(p_num)
    return p_text
def encode(plain_text, key):
    cipher_text = ""
    for i in range(len(plain_text)):
        cipher_text += encode_char(plain_text[i], key[i])
    return cipher_text
def decode(cipher_text, key):
    plain_text = ""
    for i in range(len(cipher_text)):
        plain_text += decode_char(cipher_text[i], key[i])
    return plain_text
def main():
    cont = True
    print("One-Time Pad Program. The key must be smaller or equal in length to the plain text. The plain text should not contain numbers.")
    print("\nOptions:\n1: Encode\n2: Decode\n3: Exit")
    while cont:
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
            cont = False
        else:
            print("Please choose 1, 2, or 3")
if __name__ == "__main__":
    main()