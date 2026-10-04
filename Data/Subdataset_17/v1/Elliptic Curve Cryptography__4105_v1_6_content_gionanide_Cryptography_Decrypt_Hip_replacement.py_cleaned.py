import string
def decrypt_caesar_cipher(text, shift):
    decrypted_text = []
    for char in text:
        if char in string.ascii_uppercase:
            new_char = chr((ord(char) - shift - 65) % 26 + 65)
            decrypted_text.append(new_char)
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)
def main():
    encrypted_text = 'YMJJDJXHFSRNXQJFIYMJXRNQJHFSQNJGZYYMJXMTJXYJQQYMJYWZYM'
    print('Encrypted message:', encrypted_text)
    for shift in range(1, 26):
        decrypted_message = decrypt_caesar_cipher(encrypted_text, shift)
        print(f'Shift {shift}: {decrypted_message}')
if __name__ == "__main__":
    main()