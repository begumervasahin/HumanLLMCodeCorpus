import string
def decrypt_caesar_cipher(encrypted_text, shift_amount):
    decrypted_chars = []
    for char in encrypted_text:
        if char in string.ascii_uppercase:
            shifted_char_code = (ord(char) - shift_amount - ord('A')) % 26 + ord('A')
            decrypted_chars.append(chr(shifted_char_code))
        else:
            decrypted_chars.append(char)
    return ''.join(decrypted_chars)
def main():
    encrypted_message = 'YMJJDJXHFSRNXQJFIYMJXRNQJHFSQNJGZYYMJXMTJXYJQQYMJYWZYM'
    print(f'Encrypted message: {encrypted_message}')
    for shift in range(1, 26):
        decrypted_message = decrypt_caesar_cipher(encrypted_message, shift)
        print(f'Shift {shift}: {decrypted_message}')
if __name__ == "__main__":
    main()