def encrypt(plain_text, key):
    result = ""
    for i in range(len(plain_text)):
        j = i % len(key)
        if plain_text[i].isupper():
            new_char = chr((ord(plain_text[i]) + ord(key[j]) - 2 * ord('A')) % 26 + ord('A'))
        elif plain_text[i].islower():
            new_char = chr((ord(plain_text[i]) + ord(key[j]) - ord('a') - ord('A')) % 26 + ord('a'))
        else:
            new_char = plain_text[i]
        result += new_char
    return result
if __name__ == "__main__":
    plain_text = "VINeeT"
    key = "WOW"
    encrypted_text = encrypt(plain_text, key)
    print("ENCRYPTED TEXT:", encrypted_text)