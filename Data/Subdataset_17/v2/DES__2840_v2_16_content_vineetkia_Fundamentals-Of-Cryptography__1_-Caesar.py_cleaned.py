def encrypt(plain_text, shift):
    encrypted_text = []
    for char in plain_text:
        if char.isupper():
            new_char = chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
        elif char.islower():
            new_char = chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
        else:
            new_char = char
        encrypted_text.append(new_char)
    return ''.join(encrypted_text)
if __name__ == "__main__":
    plain_text = "Vineet"
    shift = 4
    encrypted_text = encrypt(plain_text, shift)
    print("ENCRYPTED TEXT:", encrypted_text)