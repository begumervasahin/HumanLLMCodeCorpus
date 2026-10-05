def decrypt_message(ciphertext):
    for shift in range(1, 26):
        decrypted_text = ""
        for char in ciphertext:
            if 'A' <= char <= 'Z':
                decrypted_char = chr(((ord(char) - shift - ord('A')) % 26) + ord('A'))
            else:
                decrypted_char = char
            decrypted_text += decrypted_char
        print(f"Decryption {shift}: {decrypted_text}")
def main():
    ciphertext = 'YMJJDJXHFSRNXQJFIYMJXRNQJHFSQNJGZYYMJXMTJXYJQQYMJYWZYM'
    print('Ciphertext:', ciphertext)
    decrypt_message(ciphertext)
if __name__ == "__main__":
    main()