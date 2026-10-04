import string
def decrypt_caesar_cipher(text, shift):
    decrypted_text = []
    for char in text:
        if char in string.ascii_uppercase:
            new_char_code = (ord(char) - ord('A') + shift) % 26 + ord('A')
            decrypted_text.append(chr(new_char_code))
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)
def main():
    encrypted_text = 'YMJJDJXHFSRNXQJFIYMJXRNQJHFSQNJGZYYMJXMTJXYJQQYMJYWZYM'
    print('Encrypted message:', encrypted_text)
    print('Attempting to decrypt with various shifts:')
    for shift in range(1, 26):
        decrypted_message = decrypt_caesar_cipher(encrypted_text, shift)
        print(f'Shift {shift}: {decrypted_message}')
if __name__ == "__main__":
    main()