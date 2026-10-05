def get_encoding():
    encoding_dict = {}
    decoding_dict = {}
    encoding_dict.update({' ': 0, ',': 27, '.': 28, '?': 29, '!': 66})
    decoding_dict.update({0: ' ', 27: ',', 28: '.', 29: '?', 66: '!'})
    for i in range(65, 91):
        encoding_dict[chr(i)] = i - 64
        decoding_dict[i - 64] = chr(i)
    for i in range(48, 58):
        encoding_dict[chr(i)] = i - 18
        decoding_dict[i - 18] = chr(i)
    for i in range(97, 123):
        encoding_dict[chr(i)] = i - 57
        decoding_dict[i - 57] = chr(i)
    return encoding_dict, decoding_dict
def encrypt(string, key):
    encoding_dict, decoding_dict = get_encoding()
    encrypted_string = ""
    for char in string:
        encrypted_char = encoding_dict.get(char)
        if encrypted_char is None:
            return -1
        encrypted_char = (encrypted_char + key) % 67
        encrypted_string += decoding_dict.get(encrypted_char, char)
    return encrypted_string
def decrypt(string, key):
    encoding_dict, decoding_dict = get_encoding()
    decrypted_string = ""
    for char in string:
        decrypted_char = encoding_dict.get(char)
        if decrypted_char is None:
            return -1
        decrypted_char = (decrypted_char - key) % 67
        decrypted_string += decoding_dict.get(decrypted_char % 67, char)
    return decrypted_string