alphabet = "0123456789 ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
alphabet_chars = list(alphabet)
def clean(s):
    chars = [c.upper() for c in s if c.upper() in alphabet]
    return chars
def encrypt_char(m, k):
    m_int = alphabet.index(m)
    k_int = alphabet.index(k)
    c_int = (m_int + k_int) % len(alphabet)
    return alphabet_chars[c_int]
def encrypt(message, key):
    m_chars = clean(message)
    k_chars = clean(key)
    c_chars = [encrypt_char(m_chars[i], k_chars[i]) for i in range(len(m_chars))]
    return "".join(c_chars)
def decrypt_char(m, k):
    m_int = alphabet.index(m)
    k_int = alphabet.index(k)
    c_int = (m_int - k_int) % len(alphabet)
    return alphabet_chars[c_int]
def decrypt(message, key):
    m_chars = clean(message)
    k_chars = clean(key)
    c_chars = [decrypt_char(m_chars[i], k_chars[i]) for i in range(len(m_chars))]
    return "".join(c_chars)
message = "This is the Message!!!!! What time should we meeT? 12:30?"
key = "One thing that you will get to know about programming, is that programmers like to be lazy. If something has been done before, why should you do it again?"
encrypted_message = encrypt(message, key)
decrypted_message = decrypt(encrypted_message, key)
print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")
print(f"Decrypted Message: {decrypted_message}")