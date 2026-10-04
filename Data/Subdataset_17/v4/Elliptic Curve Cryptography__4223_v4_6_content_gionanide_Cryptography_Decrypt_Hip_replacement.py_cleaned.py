import timeit
def decrypt_caesar_cipher(text, shift):
    decrypted_chars = []
    for char in text:
        if 'A' <= char <= 'Z':
            shifted_char_code = (ord(char) - ord('A') + shift) % 26 + ord('A')
            decrypted_chars.append(chr(shifted_char_code))
        else:
            decrypted_chars.append(char)
    return ''.join(decrypted_chars)
def main():
    encrypted_text = 'YMJJDJXHFSRNXQJFIYMJXRNQJHFSQNJGZYYMJXMTJXYJQQYMJYWZYM'
    print('Encrypted message:', encrypted_text)
    for shift in range(1, 26):
        decrypted_message = decrypt_caesar_cipher(encrypted_text, shift)
        print(f'Shift {shift}: {decrypted_message}')
if __name__ == "__main__":
    main()