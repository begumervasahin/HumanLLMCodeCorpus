import binascii
def text_to_binary(text):
    hex_representation = binascii.hexlify(text.encode()).decode()
    return bin(int(hex_representation, 16))[2:]
def xor(m, k):
    result = []
    for bit_m, bit_k in zip(m, k):
        if bit_m.isalpha() and bit_k.isalpha():
            result.append(bit_m)
        else:
            result.append(str(int(bit_m) ^ int(bit_k)))
    return "".join(result)
def binary_to_text(binary):
    hex_representation = hex(int(binary, 2))[2:]
    return binascii.unhexlify(hex_representation).decode()
if __name__ == "__main__":
    plain_text = 'informationsecurity'
    key1 = 'vlaksjdhfgqodzmxncb'
    alternative_key = 'tlftrffwmixor|{xbch'
    print('The plain text is:', plain_text)
    print('The first key is:', key1, '\n')
    plain_text_binary = text_to_binary(plain_text)
    key_binary = text_to_binary(key1)
    alternative_key_binary = text_to_binary(alternative_key)
    print('Plain text in bits:', plain_text_binary, '\n')
    print('Key in bits:', key_binary, '\n')
    encrypted_text_binary = xor(plain_text_binary, key_binary)
    encrypted_text = binary_to_text(encrypted_text_binary)
    print('XOR result for the encryption with the normal key:', encrypted_text_binary, '\n')
    print('Encrypted text:', encrypted_text)
    decrypted_text_binary = xor(encrypted_text_binary, key_binary)
    decrypted_text = binary_to_text(decrypted_text_binary)
    print('\nDecryption result:', decrypted_text_binary, '\n')
    print('Decrypted text with the normal key:', decrypted_text, '\n')
    decrypted_text_alternative_binary = xor(encrypted_text_binary, alternative_key_binary)
    decrypted_text_alternative = binary_to_text(decrypted_text_alternative_binary)
    print('Decryption with the alternative key\n')
    print('Alternative key in bits:', alternative_key_binary, '\n')
    print('Decrypted text with the alternative key:', decrypted_text_alternative)