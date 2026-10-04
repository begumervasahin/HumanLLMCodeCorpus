import utils.dictUtils
def encrypt_msg(key, message):
    return translate_msg(key, message, 'encrypt')
def decrypt_msg(key, message):
    return translate_msg(key, message, 'decrypt')
def translate_msg(key, message, mode):
    translated = []
    key = key.upper()
    key_index = 0
    is_encrypt = (mode == 'encrypt')
    for symbol in message:
        symbol_offset = get_alphabet().find(symbol.upper())
        if symbol_exists(symbol_offset):
            offset = calculate_alphabet_offset(is_encrypt, key, key_index, symbol_offset)
            if symbol.isupper():
                translated.append(get_alphabet()[offset])
            elif symbol.islower():
                translated.append(get_alphabet()[offset].lower())
            key_index = increment_key_index(key, key_index)
        else:
            translated.append(symbol)
    return ''.join(translated)
def symbol_exists(offset):
    return offset != -1
def get_alphabet():
    return utils.dictUtils.ALPHABET_UPPER
def calculate_alphabet_offset(is_encrypt, key, key_index, offset):
    key_char_offset = get_alphabet().find(key[key_index])
    if is_encrypt:
        offset += key_char_offset
    else:
        offset -= key_char_offset
    return offset % len(get_alphabet())
def increment_key_index(key, key_index):
    key_index += 1
    if key_index == len(key):
        key_index = 0
    return key_index
def main():
    print('1. Introduce a message: ')
    message = input()
    print('2. Introduce the key: ')
    key = input()
    print('3. Introduce the word "encrypt" to encrypt the message or push Enter to decrypt: ')
    mode = input().lower()
    if mode == 'encrypt':
        translated_message = encrypt_msg(key, message)
    else:
        translated_message = decrypt_msg(key, message)
    print(f'{mode.title()}ed message:')
    print(translated_message)
if __name__ == '__main__':
    main()