import binascii
def to_binary_string(data):
    hex_data = bin(int(binascii.hexlify(data.encode()), 16))[2:]
    return hex_data.zfill(len(data) * 8)
def xor(binary_message, binary_key):
    return ''.join(str(int(bm) ^ int(bk)) for bm, bk in zip(binary_message, binary_key))
def binary_to_text(binary_data):
    hex_data = f'{int(binary_data, 2):x}'
    return binascii.unhexlify(hex_data).decode()
def print_binary_conversion(data, label):
    binary_data = to_binary_string(data)
    print(f'{label} in bits: {binary_data}')
def print_encryption_decryption_results(encrypted_result, decrypted_result, encrypted_text, decrypted_text):
    print(f'XOR result for the encryption: {encrypted_result}')
    print(f'Encrypted text: {encrypted_text}\n')
    print(f'Decryption result: {decrypted_result}')
    print(f'Decrypted text: {decrypted_text}\n')
plain_text = 'informationsecurity'
key1 = 'vlaksjdhfgqodzmxncb'
alternative_key = 'tlftrffwmixor|{xbch'
print(f'The plain text is: {plain_text}')
print(f'The first key is: {key1}\n')
print_binary_conversion(plain_text, 'Plain text')
print_binary_conversion(key1, 'Key')
xor_result = xor(to_binary_string(plain_text), to_binary_string(key1))
encrypted_number = int(xor_result, 2)
encrypted_text = binary_to_text(xor_result)
decrypted_xor_result = xor(xor_result, to_binary_string(key1))
decrypted_text = binary_to_text(decrypted_xor_result)
print_encryption_decryption_results(
    xor_result,
    decrypted_xor_result,
    encrypted_text,
    decrypted_text
)
alternative_key_bin = to_binary_string(alternative_key)
print(f'Alternative key in bits: {alternative_key_bin}\n')
alternative_decryption_result = xor(xor_result, alternative_key_bin)
alternative_decrypted_text = binary_to_text(alternative_decryption_result)
print(f'Decrypted text with the alternative key: {alternative_decrypted_text}')