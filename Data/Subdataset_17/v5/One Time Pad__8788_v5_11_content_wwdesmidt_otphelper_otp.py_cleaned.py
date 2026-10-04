alphabet = "0123456789 ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
alphabet_chars = list(alphabet)
message = "This is the Message!!!!! What time should we meeT? 12:30?"
key = ("One thing that you will get to know about programming, is that programmers like to be lazy. "
       "If something has been done before, why should you do it again?")
def clean(s):
    return [c.upper() for c in s if c.upper() in alphabet]
def encrypt_char(message_char, key_char):
    message_index = alphabet.index(message_char)
    key_index = alphabet.index(key_char)
    encrypted_index = (message_index + key_index) % len(alphabet)
    return alphabet_chars[encrypted_index]
def encrypt(message, key):
    message_chars = clean(message)
    key_chars = clean(key)
    encrypted_chars = [encrypt_char(message_chars[i], key_chars[i]) for i in range(len(message_chars))]
    return "".join(encrypted_chars)
def decrypt_char(encrypted_char, key_char):
    encrypted_index = alphabet.index(encrypted_char)
    key_index = alphabet.index(key_char)
    decrypted_index = (encrypted_index - key_index) % len(alphabet)
    return alphabet_chars[decrypted_index]
def decrypt(encrypted_message, key):
    encrypted_chars = clean(encrypted_message)
    key_chars = clean(key)
    decrypted_chars = [decrypt_char(encrypted_chars[i], key_chars[i]) for i in range(len(encrypted_chars))]
    return "".join(decrypted_chars)
encrypted_message = encrypt(message, key)
decrypted_message = decrypt(encrypted_message, key)
print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")
print(f"Decrypted Message: {decrypted_message}")