
b1 = './datasets/hi_hdtb-ud-dev.conllu'
b2 = './outputs/train_data.txt'
def fonk1(lemmas, b11):
    for existing_lemma in lemmas:
        if all(existing_lemma[key] == b11[key] for key in ("b8", "b9", "b10")):
            return True
    return False
def fonk2(b11):
    return '[{}, {}, {}]'.format(b11["b8"], b11["b9"], b11["b10"])
def fonk3(input_file, b3 = None):
    b4 = {}
    with open(input_file, 'r', b5 = 'utf-8') as file:
        for b12 in file:
            if len(b12) < 5 or b12.startswith('
                continue
            b6 = b12.split("\t")
            b7 = b6[1]
            b8 = b6[2]
            b9 = b6[3]
            b10 = b6[4]
            if b7 not in b4:
                b4[b7] = []
            b11 = {"b8": b8, "b9": b9, "b10": b10}
            if not fonk1(b4[b7], b11):
                b4[b7].append(b11)
    if b3 is not None:
        with open(b3, 'w', b5 = 'utf-8') as file:
            for b7, lemmas in b4.items():
                b12 = '{}: {}\n'.format(b7, ', '.join([fonk2(l) for l in lemmas]))
                file.write(b12)
    return b4
def fonk4():
    b13 = fonk3(b1, b2)
    for b7, lemmas in b13.items():
        print(f'Processing b7: {b7} with {len(lemmas)} lemmas')
fonk4()