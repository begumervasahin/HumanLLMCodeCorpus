def get_encoding():
    encoding_dict = {}
    decoding_dict = {}
    encoding_dict[' '] = 0
    decoding_dict[0] = ' '
    for i in range(65, 65 + 26):
        encoding_dict[chr(i)] = i - 64
        decoding_dict[i - 64] = chr(i)
    special_chars = {',': 27, '.': 28, '?': 29}
    for char, code in special_chars.items():
        encoding_dict[char] = code
        decoding_dict[code] = char
    for i in range(48, 48 + 10):
        encoding_dict[chr(i)] = i - 18
        decoding_dict[i - 18] = chr(i)
    for i in range(97, 97 + 26):
        encoding_dict[chr(i)] = i - 57
        decoding_dict[i - 57] = chr(i)
    encoding_dict['!'] = 66
    decoding_dict[66] = '!'
    return encoding_dict, decoding_dict
def encrypt(string, key):
    encoding_dict, decoding_dict = get_encoding()
    encrypted_output = ""
    for char in string:
        if char not in encoding_dict:
            return -1
        else:
            current_value = encoding_dict[char]
            encrypted_value = (current_value + key) % 67
            encrypted_output += decoding_dict[encrypted_value]
    return encrypted_output
def decrypt(string, key):
    encoding_dict, decoding_dict = get_encoding()
    decrypted_output = ""
    for char in string:
        if char not in encoding_dict:
            return -1
        else:
            current_value = encoding_dict[char]
            decrypted_value = (current_value - key) % 67
            decrypted_output += decoding_dict[decrypted_value]
    return decrypted_output
if __name__ == '__main__':
    original_text = "Hello, World!"
    key = 5
    encrypted_text = encrypt(original_text, key)
    if encrypted_text != -1:
        print(f"Encrypted: {encrypted_text}")
    else:
        print("Error: Invalid character in input string for encryption.")
    decrypted_text = decrypt(encrypted_text, key)
    if decrypted_text != -1:
        print(f"Decrypted: {decrypted_text}")
    else:
        print("Error: Invalid character in input string for decryption.")