def get_encoding():
    encoding_dict = {}
    decoding_dict = {}
    encoding_dict[' '] = 0
    decoding_dict[0] = ' '
    for i in range(65, 91):
        encoding_dict[chr(i)] = i - 64
        decoding_dict[i - 64] = chr(i)
    encoding_dict[','] = 27
    encoding_dict['.'] = 28
    encoding_dict['?'] = 29
    decoding_dict[27] = ','
    decoding_dict[28] = '.'
    decoding_dict[29] = '?'
    for i in range(48, 58):
        encoding_dict[chr(i)] = i - 18
        decoding_dict[i - 18] = chr(i)
    for i in range(97, 123):
        encoding_dict[chr(i)] = i - 57
        decoding_dict[i - 57] = chr(i)
    encoding_dict['!'] = 66
    decoding_dict[66] = '!'
    return encoding_dict, decoding_dict
def encrypt(text, key):
    encoding_dict, decoding_dict = get_encoding()
    valid_chars = set(encoding_dict.keys())
    encrypted_text = []
    for char in text:
        if char not in valid_chars:
            return -1
        encoded_value = encoding_dict[char]
        encrypted_value = (encoded_value + key) % 67
        encrypted_text.append(decoding_dict[encrypted_value])
    return ''.join(encrypted_text)
def decrypt(text, key):
    encoding_dict, decoding_dict = get_encoding()
    valid_chars = set(encoding_dict.keys())
    decrypted_text = []
    for char in text:
        if char not in valid_chars:
            return -1
        encoded_value = encoding_dict[char]
        decrypted_value = (encoded_value - key) % 67
        decrypted_text.append(decoding_dict[decrypted_value])
    return ''.join(decrypted_text)