import texthelper as th
len_msg = 31
num_msgs = 7
def main():
    with open('./ctexts.txt') as fin:
        ctexts = fin.readlines()
        ctexts = [th.hex_to_nums(l.strip()) for l in ctexts]
        key_pred = predict_key(ctexts)
        ptexts = apply_key_to_all(ctexts, key_pred)
        ptexts_eng = clean_ptexts(ptexts)
        for text in ptexts_eng:
            print(text)
        key = key_pred.copy()
        key[0] = ctexts[0][0] ^ ord('I')
        key[6] = ctexts[0][6] ^ ord('l')
        key[8] = ctexts[0][8] ^ ord('n')
        key[10] = ctexts[0][10] ^ ord('i')
        key[17] = ctexts[0][17] ^ ord('e')
        key[20] = ctexts[0][20] ^ ord('e')
        key[29] = ctexts[0][29] ^ ord('n')
        key[30] = ctexts[0][30] ^ ord('.')
        ptexts = apply_key_to_all(ctexts, key)
        ptexts_eng = clean_ptexts(ptexts)
        print()
        for text in ptexts_eng:
            print(text)
def predict_key(ctexts):
    space_locs = predict_space_locs(ctexts)
    key_pred = [None] * len_msg
    for i in range(len_msg):
        id_msg = space_locs[i]
        if id_msg == -1:
            char_key_pred = None
        else:
            cipher_char = ctexts[id_msg][i]
            char_key_pred = cipher_char ^ ord(' ')
        key_pred[i] = char_key_pred
    return key_pred
def apply_key_to_all(ctexts, key):
    ptexts = []
    for ctext in ctexts:
        ptext = apply_key(ctext, key)
        ptexts.append(ptext)
    return ptexts
def clean_ptexts(ptexts_ascii):
    ptexts = []
    for ptext_ascii in ptexts_ascii:
        ptext = clean_ptext(ptext_ascii)
        ptexts.append(ptext)
    return ptexts
def predict_space_locs(ctexts):
    space_locs = []
    for i in range(31):
        scores = compare_index(ctexts, i)
        try:
            loc = scores.index(num_msgs)
        except ValueError:
            loc = -1
        space_locs.append(loc)
    return space_locs
def clean_ptext(ptext_ascii):
    ptext = [chr(c) if c != 0 else '_' for c in ptext_ascii]
    return ''.join(ptext)
def apply_key(ctext, key):
    ptext = [0] * len_msg
    for i in range(len_msg):
        if key[i] is not None:
            ptext[i] = ctext[i] ^ key[i]
    return ptext
def compare_index(ctexts, i):
    scores = []
    for j in range(num_msgs):
        list_xors = []
        for k in range(num_msgs):
            xor = ctexts[j][i] ^ ctexts[k][i]
            list_xors.append(xor)
        score = space_score(list_xors)
        scores.append(score)
    return scores
def space_score(list_xors):
    score = 0
    for xor in list_xors:
        if xor > 64 or xor == 0:
            score += 1
    return score
if __name__ == '__main__':
    main()