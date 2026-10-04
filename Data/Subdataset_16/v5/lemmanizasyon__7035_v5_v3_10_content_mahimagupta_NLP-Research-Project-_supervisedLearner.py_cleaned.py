
b1 = './datasets/hi_hdtb-ud-dev.conllu'
b2 = './outputs/train_data.txt'
def fonk1(lemmas, b8):
    return any(all(existing_lemma[key] == b8[key] for key in ("root", "tag1", "b7")) for existing_lemma in lemmas)
def fonk2(b8):
    return '[{}, {}, {}]'.format(b8["root"], b8["tag1"], b8["b7"])
def fonk3(input_file, b3 = None):
    b4 = {}
    with open(input_file, 'r', b5 = 'utf-8') as file:
        for line in file:
            if len(line) < 5 or line.startswith('
                continue
            b6 = line.split("\t")
            word, root, tag1, b7 = b6[1], b6[2], b6[3], b6[4]
            if word not in b4:
                b4[word] = []
            b8 = {"root": root, "tag1": tag1, "b7": b7}
            if not fonk1(b4[word], b8):
                b4[word].append(b8)
    if b3 is not None:
        with open(b3, 'w', b5 = 'utf-8') as file:
            for word, lemmas in b4.items():
                b9 = ', '.join([fonk2(l) for l in lemmas])
                file.write(f'{word}: {b9}\n')
    return b4
def fonk4():
    b10 = fonk3(b1, b2)
    for word, lemmas in b10.items():
        print(f'Processing word: {word} with {len(lemmas)} lemmas')
fonk4()