def caesar_encrypt(plaintext, key):
    encrypted_text = ''
    for char in plaintext:
        char_value = ord(char)
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            char_value = ((char_value - offset + key) % 26) + offset
        encrypted_text += chr(char_value)
    return encrypted_text
def caesar_decrypt(ciphertext, key):
    decrypted_text = ''
    for char in ciphertext:
        char_value = ord(char)
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            char_value = ((char_value - offset - key) % 26) + offset
        decrypted_text += chr(char_value)
    return decrypted_text
def vigenere_encrypt(plaintext, key):
    key_length = len(key)
    ciphertext = ''
    for i, char in enumerate(plaintext):
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            shift = ord(key[i % key_length].lower()) - ord('a')
            char_value = ((ord(char) - offset + shift) % 26) + offset
            ciphertext += chr(char_value)
        else:
            ciphertext += char
    return ciphertext
def vigenere_decipher(ciphertext, key):
    key_length = len(key)
    plaintext = ''
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            shift = ord(key[i % key_length].lower()) - ord('a')
            char_value = ((ord(char) - offset - shift) % 26) + offset
            plaintext += chr(char_value)
        else:
            plaintext += char
    return plaintext