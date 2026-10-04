def encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isupper():
            new_char = chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
        else:
            new_char = chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
        encrypted_text += new_char
    return encrypted_text
if __name__ == "__main__":
    plain_text = "Vineet"
    shift = 4
    encrypted_text = encrypt(plain_text, shift)
    print("ENCRYPTED TEXT:", encrypted_text)