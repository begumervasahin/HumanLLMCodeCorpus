def read_private_key(pub_key_file):
    with open(pub_key_file, 'r') as file:
        lines = file.readlines()
    prime = int(lines[0].strip())
    private_key = int(lines[2].strip())
    return private_key, prime
def decrypt_block(private_key, c1, c2, prime):
    decrypted_value = (pow(c1, prime - 1 - private_key, prime) * (c2 % prime)) % prime
    return decrypted_value
def decrypt_file(read_path="test/testEncrypted.txt", write_path="test/testDecrypted.txt", pri_key_path='test/testprikey.txt', debug=False):
    private_key, prime = read_private_key(pri_key_path)
    with open(read_path, 'r') as read_file:
        cipher_lines = read_file.readlines()
    decrypted_output = ''
    for line in cipher_lines:
        c1, c2 = map(int, line.split())
        decrypted_output += chr(decrypt_block(private_key, c1, c2, prime))
    if debug:
        print(f"DEBUG decrypted output: \n{decrypted_output}\n")
    with open(write_path, 'w', encoding='utf-8') as write_file:
        write_file.write(decrypted_output)
if __name__ == '__main__':
    decrypt_file(debug=True)