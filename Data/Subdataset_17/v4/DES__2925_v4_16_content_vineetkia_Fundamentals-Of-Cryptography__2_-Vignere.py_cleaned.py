def encrypt(plain_text, key):
    result = []
    for i, char in enumerate(plain_text):
        key_char = key[i % len(key)]
        if char.isupper():
            encrypted_char = chr((ord(char) + ord(key_char) - 2 * ord('A')) % 26 + ord('A'))
        elif char.islower():
            encrypted_char = chr((ord(char) + ord(key_char) - ord('a') - ord('A')) % 26 + ord('a'))
        else:
            encrypted_char = char
        result.append(encrypted_char)
    return ''.join(result)
if __name__ == "__main__":
    plain_text = "VINeeT"
    key = "WOW"
    encrypted_text = encrypt(plain_text, key)
    print("ENCRYPTED TEXT:", encrypted_text)