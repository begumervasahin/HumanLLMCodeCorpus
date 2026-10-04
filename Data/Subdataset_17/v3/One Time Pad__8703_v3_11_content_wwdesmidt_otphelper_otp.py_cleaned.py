ALPHABET = "0123456789 ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
ALPHABET_CHARS = list(ALPHABET)
def clean(s):
    return [c.upper() for c in s if c.upper() in ALPHABET]
def encrypt_char(m, k):
    m_int = ALPHABET.index(m)
    k_int = ALPHABET.index(k)
    c_int = (m_int + k_int) % len(ALPHABET)
    return ALPHABET_CHARS[c_int]
def decrypt_char(c, k):
    c_int = ALPHABET.index(c)
    k_int = ALPHABET.index(k)
    m_int = (c_int - k_int) % len(ALPHABET)
    return ALPHABET_CHARS[m_int]
def encrypt(message, key):
    m_chars = clean(message)
    k_chars = clean(key)
    encrypted_chars = [encrypt_char(m_chars[i], k_chars[i % len(k_chars)]) for i in range(len(m_chars))]
    return "".join(encrypted_chars)
def decrypt(encrypted_message, key):
    c_chars = clean(encrypted_message)
    k_chars = clean(key)
    decrypted_chars = [decrypt_char(c_chars[i], k_chars[i % len(k_chars)]) for i in range(len(c_chars))]
    return "".join(decrypted_chars)
if __name__ == "__main__":
    message = "This is the Message!!!!! What time should we meeT? 12:30?"
    key = ("One thing that you will get to know about programming, is that programmers "
           "like to be lazy. If something has been done before, why should you do it again?")
    encrypted_message = encrypt(message, key)
    decrypted_message = decrypt(encrypted_message, key)
    print(f"Original Message: {message}")
    print(f"Encrypted Message: {encrypted_message}")
    print(f"Decrypted Message: {decrypted_message}")