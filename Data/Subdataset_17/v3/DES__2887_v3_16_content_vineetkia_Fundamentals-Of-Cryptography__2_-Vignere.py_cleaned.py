def encrypt(plain_text, key):
    encrypted_text = []
    key_length = len(key)
    for i, char in enumerate(plain_text):
        key_char = key[i % key_length]
        if char.isupper():
            new_char = chr((ord(char) + ord(key_char) - 2 * ord('A')) % 26 + ord('A'))
        elif char.islower():
            new_char = chr((ord(char) + ord(key_char) - ord('a') - ord('A')) % 26 + ord('a'))
        else:
            new_char = char
        encrypted_text.append(new_char)
    return ''.join(encrypted_text)
if __name__ == "__main__":
    plain_text = "VINeeT"
    key = "WOW"
    encrypted_text = encrypt(plain_text, key)
    print("ENCRYPTED TEXT:", encrypted_text)