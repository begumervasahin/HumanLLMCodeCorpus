def create_substitution_alphabet(key_letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key_index = alphabet.index(key_letter)
    return alphabet[key_index:] + alphabet[:key_index]
def cipher_sub(text, key_letter):
    print(f"\nOriginal Text: {text}")
    substitution_alphabet = create_substitution_alphabet(key_letter)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encoded_message = ''.join(
        substitution_alphabet[alphabet.index(char)] if char.isalpha() else char for char in text
    )
    print(f"\nKey Letter: {key_letter}")
    print(f"Substitution Alphabet: < {' '.join(substitution_alphabet)} >")
    return encoded_message
def decode_sub(encoded_text, key_letter):
    print(f"\nEncoded Text: {encoded_text}")
    substitution_alphabet = create_substitution_alphabet(key_letter)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decoded_message = ''.join(
        alphabet[substitution_alphabet.index(char)] if char.isalpha() else char for char in encoded_text
    )
    print(f"\nKey Letter: {key_letter}")
    print(f"Substitution Alphabet: < {' '.join(substitution_alphabet)} >")
    return decoded_message
def output_encoded(text):
    print(" ".join(text))
def empty_array(size):
    return [0] * size
def alpha_index(letter):
    if len(letter) != 1 or not letter.isalpha():
        print("That's not a letter!")
        return None
    return ord(letter.lower()) - ord('a')
if __name__ == "__main__":
    original_text = "hello world"
    key_letter = 'd'
    encoded_message = cipher_sub(original_text, key_letter)
    print(f"\nEncoded Message: {encoded_message}")
    decoded_message = decode_sub(encoded_message, key_letter)
    print(f"\nDecoded Message: {decoded_message}")
    print("\nOutput Encoded Message:")
    output_encoded(encoded_message)
    print(f"\nEmpty Array Example: {empty_array(5)}")
    print(f"Index of '{key_letter}' in Alphabet: {alpha_index(key_letter)}")