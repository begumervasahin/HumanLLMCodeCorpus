def read_private_key(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    prime = int(lines[0].strip())
    private_key = int(lines[2].strip())
    return private_key, prime
def decrypt_block(private_key, c1, c2, prime):
    return (pow(c1, prime - 1 - private_key, prime) * c2) % prime
def decrypt_file(read_path="test/testEncrypted.txt", write_path="test/testDecrypted.txt", pri_key_path='test/testprikey.txt', debug=False):
    private_key, prime = read_private_key(pri_key_path)
    with open(read_path, 'r') as read_file:
        cipher_lines = read_file.readlines()
    decrypted_output = []
    for line in cipher_lines:
        c1, c2 = map(int, line.split())
        decrypted_output.append(chr(decrypt_block(private_key, c1, c2, prime)))
    decrypted_text = ''.join(decrypted_output)
    if debug:
        print(f"DEBUG decrypted output: \n{decrypted_text}\n")
    with open(write_path, 'w', encoding='utf-8') as write_file:
        write_file.write(decrypted_text)
if __name__ == '__main__':
    decrypt_file(
        read_path="test/testEncrypted.txt",
        write_path="test/testDecrypted.txt",
        pri_key_path='test/testprikey.txt',
        debug=True
    )