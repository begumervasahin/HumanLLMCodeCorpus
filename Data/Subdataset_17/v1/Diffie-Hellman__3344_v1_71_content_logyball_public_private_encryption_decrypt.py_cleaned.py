def make_private_key_from_file(pub_key_file):
    with open(pub_key_file, 'r') as pkf:
        pub_key_list = pkf.readlines()
    return int(pub_key_list[2]), int(pub_key_list[0])
def decrypt_block(private_key, c1, c2, prime):
    return (pow(c1, prime - 1 - private_key, prime) * (c2 % prime)) % prime
def decrypt_file(read_path="test/testEncrypted.txt", write_path="test/testDecrypted.txt", pri_key_path='test/testprikey.txt', debug=False):
    private_key, prime = make_private_key_from_file(pri_key_path)
    with open(read_path, 'r') as rf:
        all_cipher_lines = rf.readlines()
    output = ''
    for line in all_cipher_lines:
        c1, c2 = map(int, line.split())
        output += chr(decrypt_block(private_key, c1, c2, prime))
    if debug:
        print("DEBUG decrypted output: \n%s\n" % output)
    with open(write_path, 'w', encoding='utf-8') as wf:
        wf.write(output)
if __name__ == '__main__':
    decrypt_file(debug=True)