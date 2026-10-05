import binascii
def text_to_bits(text):
    hex_representation = binascii.hexlify(text.encode()).decode()
    return bin(int(hex_representation, 16))[2:]
def bits_to_text(bits):
    hex_representation = hex(int(bits, 2))[2:]
    return binascii.unhexlify(hex_representation).decode()
def xor(m, k):
    result = []
    for i, j in zip(m, k):
        if i.isalpha() and j.isalpha():
            result.append(i)
        else:
            result.append(str(int(i) ^ int(j)))
    return "".join(result)
def encrypt(plaintext, key):
    plaintext_bits = text_to_bits(plaintext)
    key_bits = text_to_bits(key)
    return xor(plaintext_bits, key_bits)
def decrypt(ciphertext, key):
    key_bits = text_to_bits(key)
    decrypted_bits = xor(ciphertext, key_bits)
    return bits_to_text(decrypted_bits)
if __name__ == "__main__":
    plaintext = 'informationsecurity'
    key = 'vlaksjdhfgqodzmxncb'
    print('The plaintext is:', plaintext)
    print('The key is:', key, '\n')
    print('Plaintext in bits:', text_to_bits(plaintext), '\n')
    print('Key in bits:', text_to_bits(key), '\n')
    encrypted_text = encrypt(plaintext, key)
    print('Encrypted text:', encrypted_text)
    decrypted_text = decrypt(encrypted_text, key)
    print('Decrypted text with the normal key:', decrypted_text)
    alternative_key = 'tlftrffwmixor|{xbch'
    print('\nDecryption with the alternative key')
    print('Alternative key in bits:', text_to_bits(alternative_key), '\n')
    decrypted_text_alternative = decrypt(encrypted_text, alternative_key)
    print('Decrypted text with the alternative key:', decrypted_text_alternative)