def generate_substitution_alphabet(key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key_index = alphabet.index(key)
    substitution_alphabet = alphabet[key_index:] + alphabet[:key_index]
    return substitution_alphabet, key_index
def encode_message(message, substitution_alphabet):
    encoded_message = []
    for char in message:
        if char.isalpha():
            encoded_message.append(substitution_alphabet[ord(char.lower()) - ord('a')])
        else:
            encoded_message.append(char)
    return ''.join(encoded_message)
def decode_message(encoded_message, substitution_alphabet):
    decoded_message = []
    for char in encoded_message:
        if char.isalpha():
            decoded_message.append(chr(substitution_alphabet.index(char) + ord('a')))
        else:
            decoded_message.append(char)
    return ''.join(decoded_message)
def output_encoded_message(encoded_message):
    print("Encoded message:")
    for char in encoded_message:
        print(char, end=' ')
def empty_array(size):
    return [0] * size
def alpha_index(char):
    if len(char) != 1:
        print("Please input a single letter!")
    elif not char.isalpha():
        print("Please input a letter!")
    else:
        return ord(char.lower()) - ord('a')
if __name__ == "__main__":
    message = "Hello, World!"
    key = 'c'
    substitution_alphabet, key_index = generate_substitution_alphabet(key)
    encoded_message = encode_message(message.lower(), substitution_alphabet)
    print("Encoded message:", encoded_message)
    decoded_message = decode_message(encoded_message, substitution_alphabet)
    print("Decoded message:", decoded_message)