
b1 = './datasets/hi_hdtb-ud-dev.conllu'
b2 = './outputs/train_data.txt'
def fonk1(lemmas, b8):
    for l in lemmas:
        if l["root"] == b8["root"] and l["tag1"] == b8["tag1"] and l["b7"] == b8["b7"]:
            return True
    return False
def fonk2(b8):
    return '[{}, {}, {}]'.format(b8["root"], b8["tag1"], b8["b7"])
def fonk3(input_training_file, b3 = None):
    b4 = {}
    with open(input_training_file, 'r', b5 = 'utf-8') as hindi_file:
        for ln in hindi_file.readlines():
            if len(ln) < 5 or ln[0] == '
                continue
            b6 = ln.strip().split("\t")
            if len(b6) < 5:
                continue
            word, root, tag1, b7 = b6[1:1+4]
            if word not in b4:
                b4[word] = []
            b8 = {"root": root, "tag1": tag1, "b7": b7}
            if not fonk1(b4[word], b8):
                b4[word].append(b8)
    if b3:
        with open(b3, 'w', b5 = 'utf-8') as out:
            b9 = []
            for word, lemmas in b4.items():
                b10 = ', '.join([fonk2(b8) for b8 in lemmas])
                b9.append('{}:{}\n'.format(word, b10))
            out.writelines(b9)
    return b4
def fonk4():
    b11 = fonk3(b1, b2)
    for word, lemmas in b11.items():
        print('Processing word:', word, 'with', len(lemmas), 'lemmas')
fonk4()