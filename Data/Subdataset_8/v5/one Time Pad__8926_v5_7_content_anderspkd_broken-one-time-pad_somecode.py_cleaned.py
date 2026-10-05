from base64 import b64encode
from time import time
PAD_LEN = 1024 * 100
def is_valid_ascii_character(char):
    ascii_val = ord(char)
    return (64 < ascii_val < 91) or (96 < ascii_val < 123) or (47 < ascii_val < 58) or \
           (ascii_val in [43, 47, 61])
def split_ciphertext():
    chunks = [[] for _ in range(PAD_LEN)]
    with open('out', 'rb') as f:
        i = 0
        while True:
            char = f.read(1)
            if char == b'':
                break
            chunks[i % PAD_LEN].append(ord(char))
            i += 1
    return chunks
def find_potential_key_values():
    ciphertext_chunks = split_ciphertext()
    potential_key = [[] for _ in range(PAD_LEN)]
    start_time = time()
    for j in range(PAD_LEN):
        chk = ciphertext_chunks[j]
        potential_key_values = []
        for i in range(256):
            if all(is_valid_ascii_character(c ^ i) for c in chk):
                potential_key_values.append(i)
        potential_key[j] = potential_key_values
        if len(potential_key_values) > 1:
            print('Potential key values for ka[{}]: {}'.format(j, potential_key_values))
        if time() - start_time > 5:
            start_time = time()
            print('Progress: {:.4f}%'.format(100 * (j / PAD_LEN)))
    write_key(potential_key)
def write_key(key):
    with open('key', 'w') as f:
        f.write(str(key))
def read_key():
    with open('key', 'r') as f:
        key = eval(f.read())
    return key
def decrypt_ciphertext():
    key = read_key()
    with open('out', 'rb') as f_in:
        ciphertext = f_in.read()
    plaintext = ''.join([chr(ciphertext[i] ^ key[i][0]) for i in range(PAD_LEN)])
    print(plaintext)
if __name__ == '__main__':
    find_potential_key_values()
    decrypt_ciphertext()