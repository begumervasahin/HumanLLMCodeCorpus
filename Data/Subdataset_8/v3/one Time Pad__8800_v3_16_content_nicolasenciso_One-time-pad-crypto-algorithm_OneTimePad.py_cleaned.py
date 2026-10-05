def encrypt_letter(letter, shift):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypted_index = (alphabet.index(letter) + shift) % 26
    return alphabet[encrypted_index]
def encrypt_text(key, text):
    encrypted_text = ''
    key_index = 0
    for letter in text:
        shift = ord(key[key_index]) - ord('A')
        encrypted_text += encrypt_letter(letter.upper(), shift)
        key_index = (key_index + 1) % len(key)
    return encrypted_text
def encrypt_numeric(key, numeric):
    encrypted_numeric = []
    key_index = 0
    for digit in numeric:
        shift = int(key[key_index])
        encrypted_digit = (int(digit) + shift) % 10
        encrypted_numeric.append(str(encrypted_digit))
        key_index = (key_index + 1) % len(key)
    return encrypted_numeric
print(encrypt_text("EVXLL", "MONTH"))
print(encrypt_numeric("6", "6"))