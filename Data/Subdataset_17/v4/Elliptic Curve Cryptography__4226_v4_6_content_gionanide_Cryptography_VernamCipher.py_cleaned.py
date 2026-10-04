import binascii
def to_binary_string(data):
    hex_data = bin(int(binascii.hexlify(data.encode()), 16))[2:]
    return hex_data.zfill(len(data) * 8)
def xor(binary_message, binary_key):
    return ''.join(str(int(bm) ^ int(bk)) for bm, bk in zip(binary_message, binary_key))
def binary_to_text(binary_data):
    number = int(binary_data, 2)
    hex_data = f'{number:x}'
    return binascii.unhexlify(hex_data).decode()
plain_text = 'informationsecurity'
key1 = 'vlaksjdhfgqodzmxncb'
alternative_key = 'tlftrffwmixor|{xbch'
print('The plain text is:', plain_text)
print('The first key is:', key1, '\n')
plain_text_bin = to_binary_string(plain_text)
key1_bin = to_binary_string(key1)
print('Plain text in bits:', plain_text_bin)
print('Key in bits:', key1_bin, '\n')
xor_result = xor(plain_text_bin, key1_bin)
encrypted_number = int(xor_result, 2)
encrypted_text = binary_to_text(xor_result)
print('XOR result for the encryption with the normal key:', xor_result)
print('Encrypted text:', encrypted_text)
decrypted_xor_result = xor(xor_result, key1_bin)
decrypted_text = binary_to_text(decrypted_xor_result)
print('\nDecryption result:', decrypted_xor_result)
print('Decrypted text with the normal key:', decrypted_text, '\n')
alternative_key_bin = to_binary_string(alternative_key)
print('Alternative key in bits:', alternative_key_bin, '\n')
alternative_decryption_result = xor(xor_result, alternative_key_bin)
alternative_decrypted_text = binary_to_text(alternative_decryption_result)
print('Decrypted text with the alternative key:', alternative_decrypted_text)