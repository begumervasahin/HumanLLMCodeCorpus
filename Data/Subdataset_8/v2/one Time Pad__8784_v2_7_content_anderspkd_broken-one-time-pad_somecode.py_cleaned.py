from time import time
PAD_LENGTH = 1024 * 100
def is_valid_character(c):
    return ((64 < c < 91) or
            (96 < c < 123) or
            (47 < c < 58) or
            (c == 43) or
            (c == 47) or
            (c == 61))
def split_ciphertext():
    chunks = [[] for _ in range(PAD_LENGTH)]
    with open('out', 'rb') as file:
        index = 0
        done = False
        while not done:
            char = file.read(1)
            if char != b'':
                chunks[index % PAD_LENGTH] += [ord(char)]
                index += 1
                continue
            done = True
    return chunks
def find_possible_keys():
    chunks = split_ciphertext()
    possible_keys = [[] for _ in range(PAD_LENGTH)]
    progress_time = time()
    for index in range(PAD_LENGTH):
        chunk = chunks[index]
        possible_key_values = []
        for value in range(2 ** 8):
            valid = True
            for char in chunk:
                if not is_valid_character(char ^ value):
                    valid = False
                    break
            if valid:
                possible_key_values.append(value)
        if len(possible_key_values) > 1:
            print('Possible keys for chunk {}: {}'.format(index, possible_key_values))
        possible_keys[index] = possible_key_values
        if time() - progress_time > 5:
            progress_time = time()
            print('Progress: {:.2f}%'.format(100 * (index / PAD_LENGTH)))
    write_keys_to_file(possible_keys)
def write_keys_to_file(keys):
    with open('key', 'w') as file:
        file.write(str(keys))
def read_keys_from_file():
    with open('key', 'r') as file:
        keys = eval(file.read())
    return keys
if __name__ == '__main__':
    keys = read_keys_from_file()
    ciphertext = ''
    with open('out', 'rb') as input_file:
        ciphertext = input_file.read()
    plaintext = ''.join([chr(ciphertext[i] ^ keys[i][0]) for i in range(PAD_LENGTH)])
    print(plaintext)