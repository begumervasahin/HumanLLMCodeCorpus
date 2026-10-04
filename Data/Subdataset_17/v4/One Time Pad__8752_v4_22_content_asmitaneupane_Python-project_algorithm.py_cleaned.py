def vernam_cipher(key, text):
    answer = []
    key_length = len(key)
    for i, char in enumerate(text):
        answer.append(chr(ord(char) ^ ord(key[i % key_length])))
    return ''.join(answer)
key = "mysecretkey"
text = "Hello, World!"
cipher_text = vernam_cipher(key, text)
print("Cipher Text:", cipher_text)
decrypted_text = vernam_cipher(key, cipher_text)
print("Decrypted Text:", decrypted_text)