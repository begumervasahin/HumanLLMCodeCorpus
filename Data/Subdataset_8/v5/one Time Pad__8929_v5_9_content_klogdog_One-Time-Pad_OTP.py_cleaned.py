import random
def generate_random_key(message_length):
    return [random.randint(0, 27) for _ in range(message_length)]
def encrypt_message(message, key):
    ciphertext = [(alphabet_to_number[char] + key[i]) % 28 for i, char in enumerate(message)]
    return ciphertext
def decrypt_message(ciphertext, key):
    decrypted_message = [(ciphertext[i] - key[i]) % 28 for i in range(len(ciphertext))]
    return decrypted_message
def convert_to_text(numbers):
    return ''.join(number_to_alphabet[num] for num in numbers)
message = "this is an ultra secret message:"
alphabet_to_number = {" ": 0, "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,
                      "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20,
                      "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, ":": 27}
number_to_alphabet = {0: " ", 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
                      11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',
                      21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 27: ':'}
key = generate_random_key(len(message))
ciphertext = encrypt_message(message, key)
decrypted_message = decrypt_message(ciphertext, key)
decrypted_text = convert_to_text(decrypted_message)
print("One-time pad:")
print("Key:", key)
print("Message to number:", ciphertext)
print("Decrypted message:", decrypted_text)