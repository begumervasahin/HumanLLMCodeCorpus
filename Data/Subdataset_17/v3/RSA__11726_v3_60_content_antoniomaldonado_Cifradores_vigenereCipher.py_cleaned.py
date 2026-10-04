import string
ALPHABET = string.ascii_uppercase
def encrypt_message(key, message):
    return translate_message(key, message, 'encrypt')
def decrypt_message(key, message):
    return translate_message(key, message, 'decrypt')
def translate_message(key, message, mode):
    translated = []
    key = key.upper()
    key_index = 0
    is_encrypt = (mode == 'encrypt')
    for symbol in message:
        symbol_index = ALPHABET.find(symbol.upper())
        if symbol_index != -1:
            new_index = calculate_new_index(is_encrypt, key, key_index, symbol_index)
            translated_symbol = ALPHABET[new_index]
            if symbol.islower():
                translated.append(translated_symbol.lower())
            else:
                translated.append(translated_symbol)
            key_index = update_key_index(key, key_index)
        else:
            translated.append(symbol)
    return ''.join(translated)
def calculate_new_index(is_encrypt, key, key_index, symbol_index):
    key_offset = ALPHABET.find(key[key_index])
    if is_encrypt:
        new_index = (symbol_index + key_offset) % len(ALPHABET)
    else:
        new_index = (symbol_index - key_offset) % len(ALPHABET)
    return new_index
def update_key_index(key, current_index):
    new_index = (current_index + 1) % len(key)
    return new_index
def main():
    message = input('1. Introduce a message: ')
    key = input('2. Introduce the key: ')
    mode = input('3. Introduce the word "encrypt" to encrypt the message or press Enter to decrypt: ').lower()
    if mode == 'encrypt':
        translated = encrypt_message(key, message)
    else:
        translated = decrypt_message(key, message)
    action = mode.title() if mode else "Decrypt"
    print(f'{action}ed message:')
    print(translated)
if __name__ == '__main__':
    main()