def generate_substitution_alphabet(key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key_index = alphabet.index(key)
    substitution_alphabet = alphabet[key_index:] + alphabet[:key_index]
    return substitution_alphabet, key_index
def encode_message(message, substitution_alphabet):
    encoded_message = []
    for char in message:
        if char.isalpha():
            encoded_char = substitution_alphabet[ord(char.lower()) - ord('a')]
            encoded_message.append(encoded_char)
        else:
            encoded_message.append(char)
    return ''.join(encoded_message)
def decode_message(encoded_message, substitution_alphabet):
    decoded_message = []
    for char in encoded_message:
        if char.isalpha():
            decoded_char = chr(substitution_alphabet.index(char) + ord('a'))
            decoded_message.append(decoded_char)
        else:
            decoded_message.append(char)
    return ''.join(decoded_message)
def output_encoded_message(encoded_message):
    print(' '.join(encoded_message))
if __name__ == "__main__":
    message = "Hello, World!"
    key = 'c'
    substitution_alphabet, key_index = generate_substitution_alphabet(key)
    encoded_message = encode_message(message.lower(), substitution_alphabet)
    print("Encoded message:", encoded_message)
    print("Key Index:", key_index)
    print("Substitution Alphabet:", substitution_alphabet)
    decoded_message = decode_message(encoded_message, substitution_alphabet)
    print("\nDecoded message:", decoded_message)
    print("Key Index:", key_index)
    print("Substitution Alphabet:", substitution_alphabet)