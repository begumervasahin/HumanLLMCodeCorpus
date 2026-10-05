import texthelper as th
len_msg = 31
num_msgs = 7
def main():
    ctexts = read_ciphertexts('./ctexts.txt')
    key_pred = predict_key(ctexts)
    print("Predicted plaintexts:")
    print_plaintexts(apply_key_to_all(ctexts, key_pred))
    key_manual = adjust_key(key_pred, ctexts[0])
    print("\nUpdated plaintexts:")
    print_plaintexts(apply_key_to_all(ctexts, key_manual))
def read_ciphertexts(file_path):
    with open(file_path) as fin:
        ctexts = [th.hex_to_nums(l.strip()) for l in fin.readlines()]
    return ctexts
def predict_key(ctexts):
    space_locs = predict_space_locs(ctexts)
    key_pred = [ctexts[space_loc][i] ^ ord(' ') if space_loc != -1 else None for i, space_loc in enumerate(space_locs)]
    return key_pred
def predict_space_locs(ctexts):
    space_locs = []
    for i in range(len_msg):
        scores = [space_score([ctext[i] ^ ctexts[k][i] for k in range(num_msgs)]) for ctext in ctexts]
        space_loc = scores.index(num_msgs) if num_msgs in scores else -1
        space_locs.append(space_loc)
    return space_locs
def space_score(list_xors):
    return sum(1 for xor in list_xors if xor > 64 or xor == 0)
def apply_key_to_all(ctexts, key):
    return [apply_key(ctext, key) for ctext in ctexts]
def apply_key(ctext, key):
    return [ctext[i] ^ key[i] if key[i] is not None else 0 for i in range(len_msg)]
def adjust_key(key_pred, ctext):
    key_manual = key_pred.copy()
    key_manual[0] = ctext[0] ^ ord('I')
    key_manual[6] = ctext[6] ^ ord('l')
    key_manual[8] = ctext[8] ^ ord('n')
    key_manual[10] = ctext[10] ^ ord('i')
    key_manual[17] = ctext[17] ^ ord('e')
    key_manual[20] = ctext[20] ^ ord('e')
    key_manual[29] = ctext[29] ^ ord('n')
    key_manual[30] = ctext[30] ^ ord('.')
    return key_manual
def print_plaintexts(ptexts_ascii):
    ptexts = [clean_ptext(ptext_ascii) for ptext_ascii in ptexts_ascii]
    for text in ptexts:
        print(text)
def clean_ptext(ptext_ascii):
    return ''.join(chr(c) if c != 0 else '_' for c in ptext_ascii)
main()