import string
def decrypt_caesar_cipher(text, shift):
    decrypted_text = []
    for char in text:
        if char in string.ascii_uppercase:
            shifted = (ord(char) - shift - 65) % 26 + 65
            decrypted_text.append(chr(shifted))
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)
def main():
    encrypted_message = 'YMJJDJXHFSRNXQJFIYMJXRNQJHFSQNJGZYYMJXMTJXYJQQYMJYWZYM'
    print('Encrypted message:', encrypted_message)
    for shift in range(1, 26):
        decrypted_message = decrypt_caesar_cipher(encrypted_message, shift)
        print(f'Shift {shift}: {decrypted_message}')
if __name__ == "__main__":
    main()