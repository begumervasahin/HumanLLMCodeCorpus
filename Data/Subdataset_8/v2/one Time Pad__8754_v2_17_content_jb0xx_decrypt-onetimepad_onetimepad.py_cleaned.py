import texthelper as th
LENGTH_MESSAGE = 31
NUM_MESSAGES = 7
def main():
    with open('./ctexts.txt') as fin:
        ctexts = fin.readlines()
        ctexts = [th.hex_to_nums(line.strip()) for line in ctexts]
        key_pred = predict_key(ctexts)
        ptexts = apply_key_to_all(ctexts, key_pred)
        ptexts_eng = clean_ptexts(ptexts)
        for text in ptexts_eng:
            print(text)
        key = adjust_key(ctexts, key_pred)
        ptexts = apply_key_to_all(ctexts, key)
        print()
        ptexts_eng = clean_ptexts(ptexts)
        for text in ptexts_eng:
            print(text)
def predict_key(ctexts):
    space_locs = predict_space_locs(ctexts)
    key_pred = [None] * LENGTH_MESSAGE
    for i in range(LENGTH_MESSAGE):
        id_msg = space_locs[i]
        if id_msg != -1:
            cipher_char = ctexts[id_msg][i]
            key_pred[i] = cipher_char ^ ord(' ')
    return key_pred
def apply_key_to_all(ctexts, key):
    ptexts = []
    for ctext in ctexts:
        ptexts.append(apply_key(ctext, key))
    return ptexts
def clean_ptexts(ptexts_ascii):
    ptexts = []
    for ptext_ascii in ptexts_ascii:
        ptexts.append(clean_ptext(ptext_ascii))
    return ptexts
def predict_space_locs(ctexts):
    space_locs = []
    for i in range(LENGTH_MESSAGE):
        space_locs.append(find_space(ctexts, i))
    return space_locs
def clean_ptext(ptext_ascii):
    return ''.join(chr(c) if c != 0 else '_' for c in ptext_ascii)
def apply_key(ctext, key):
    return [ctext[i] ^ key[i] if key[i] is not None else 0 for i in range(LENGTH_MESSAGE)]
def find_space(ctexts, i):
    scores = [compare_indices(ctexts, i, j) for j in range(NUM_MESSAGES)]
    try:
        return scores.index(NUM_MESSAGES)
    except ValueError:
        return -1
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