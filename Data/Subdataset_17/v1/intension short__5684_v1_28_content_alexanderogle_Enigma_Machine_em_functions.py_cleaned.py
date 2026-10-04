def create_substitution_alphabet(n):
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    key_index = alpha.index(n)
    return alpha[key_index:] + alpha[:key_index]
def cipher_sub(text, n):
    print("\nOriginal Text:", text)
    substitution_alphabet = create_substitution_alphabet(n)
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    encoded_message = ''.join(substitution_alphabet[alpha.index(char)] if char.isalpha() else char for char in text)
    print("\nKey Letter:", n)
    print("Substitution Alphabet: <", ' '.join(substitution_alphabet), ">")
    return encoded_message
def decode_sub(text, n):
    print("\nEncoded Text:", text)
    substitution_alphabet = create_substitution_alphabet(n)
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    decoded_message = ''.join(alpha[substitution_alphabet.index(char)] if char.isalpha() else char for char in text)
    print("\nKey Letter:", n)
    print("Substitution Alphabet: <", ' '.join(substitution_alphabet), ">")
    return decoded_message
def output_encoded(text):
    for char in text:
        print(char, end=" ")
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
    encoded = cipher_sub(original_text, key_letter)
    print("\nEncoded Message:", encoded)
    decoded = decode_sub(encoded, key_letter)
    print("\nDecoded Message:", decoded)
    output_encoded(encoded)
    print("\n")
    print("Empty Array:", empty_array(5))
    print("Index of 'd' in Alphabet:", alpha_index('d'))