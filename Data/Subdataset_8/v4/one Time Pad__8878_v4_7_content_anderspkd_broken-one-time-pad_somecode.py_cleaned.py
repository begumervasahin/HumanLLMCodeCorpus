from base64 import b64encode
from time import time
PAD_LEN = 1024 * 100
def is_valid_character(c):
    return ((64 < c < 91) or
            (96 < c < 123) or
            (47 < c < 58) or
            (c == 43) or
            (c == 47) or
            (c == 61))
def split_ciphertext():
    chunks = [[] for _ in range(PAD_LEN)]
    with open('out', 'rb') as f:
        i = 0
        done = False
        while not done:
            c = f.read(1)
            if c != b'':
                chunks[i % PAD_LEN].append(ord(c))
                i += 1
            else:
                done = True
    return chunks
def find_pad():
    ciphertext_chunks = split_ciphertext()
    potential_key = [[] for _ in range(PAD_LEN)]
    t = time()
    for j in range(PAD_LEN):
        chk = ciphertext_chunks[j]
        potential_key_values = []
        for i in range(2**8):
            is_valid = True
            for c in chk:
                if not is_valid_character(c ^ i):
                    is_valid = False
                    break
            if is_valid:
                potential_key_values.append(i)
        if len(potential_key_values) > 1:
            print('Potential key values for ka[{}]: {}'.format(j, potential_key_values))
        potential_key[j] = potential_key_values
        if time() - t > 5:
            t = time()
            print('Progress: {:.4f}%'.format(100 * (j / PAD_LEN)))
    write_key(potential_key)
def write_key(key):
    with open('key', 'w') as f:
        f.write(str(key))
def read_key():
    with open('key', 'r') as f:
        key = eval(f.read())
    return key
if __name__ == '__main__':
    key = read_key()
    ciphertext = ''
    with open('out', 'rb') as f_in:
        ciphertext = f_in.read()
    plaintext = ''.join([chr(ciphertext[i] ^ key[i][0]) for i in range(PAD_LEN)])
    print(plaintext)