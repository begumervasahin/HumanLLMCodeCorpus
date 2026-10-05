import texthelper as th
LENGTH_MESSAGE = 31
NUM_MESSAGES = 7
def main():
    ctexts = read_ciphertexts('./ctexts.txt')
    key_pred = predict_key(ctexts)
    decrypt_and_print(ctexts, key_pred, "Predicted Key:")
    key = adjust_key(ctexts, key_pred)
    decrypt_and_print(ctexts, key, "\nAdjusted Key:")
def read_ciphertexts(file_path):
    with open(file_path) as fin:
        return [th.hex_to_nums(line.strip()) for line in fin.readlines()]
def predict_key(ctexts):
    space_locs = [find_space(ctexts, i) for i in range(LENGTH_MESSAGE)]
    key_pred = [None if id_msg == -1 else ctexts[id_msg][i] ^ ord(' ') for i, id_msg in enumerate(space_locs)]
    return key_pred
def decrypt_and_print(ctexts, key, label):
    ptexts = [clean_ptext(apply_key(ctext, key)) for ctext in ctexts]
    print(label)
    for text in ptexts:
        print(text)
def clean_ptext(ptext_ascii):
    return ''.join(chr(c) if c != 0 else '_' for c in ptext_ascii)
def apply_key(ctext, key):
    return [ctext[i] ^ key[i] if key[i] is not None else 0 for i in range(LENGTH_MESSAGE)]
def find_space(ctexts, i):
    scores = [compare_indices(ctexts, i, j) for j in range(NUM_MESSAGES)]
    return scores.index(NUM_MESSAGES) if NUM_MESSAGES in scores else -1
def compare_indices(ctexts, i, j):
    xors = [ctexts[j][i] ^ ctexts[k][i] for k in range(NUM_MESSAGES)]
    return sum(1 for xor in xors if xor > 64 or xor == 0)
def adjust_key(ctexts, key_pred):
    key = key_pred.copy()
    key[0] = ctexts[0][0] ^ ord('I')
    key[6] = ctexts[0][6] ^ ord('l')
    key[8] = ctexts[0][8] ^ ord('n')
    key[10] = ctexts[0][10] ^ ord('i')
    key[17] = ctexts[0][17] ^ ord('e')
    key[20] = ctexts[0][20] ^ ord('e')
    key[29] = ctexts[0][29] ^ ord('n')
    key[30] = ctexts[0][30] ^ ord('.')
    return key
if __name__ == '__main__':
    main()