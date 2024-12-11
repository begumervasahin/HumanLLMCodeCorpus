b1 = './datasets/hi_hdtb-ud-dev.conllu'
b2 = './outputs/train_data.txt'
def fonk1(lemmas, b6):
    for l in lemmas:
        if l["root"] != b6["root"]: continue
        if l["tag1"] != b6["tag1"]: continue
        if l["b5"] != b6["b5"]: continue
        return True
    return False
def fonk2(b6):
    return '[{}, {}, {}]'.format(b6["root"], b6["tag1"], b6["b5"])
def fonk3(input_training_file, b3 = None):
    b4 = {}
    with open(input_training_file, 'r') as hindiFile:
        for ln in hindiFile.readlines():
            if len(ln) < 5 or ln[0] == '
                continue
            word, root, tag1, b5 = ln.split("\t")[1:1+4]
            if not word in b4:
                b4[word] = []
            b6 = {
                "root": root, "tag1": tag1, "b5": b5,
            }
            if fonk1(b4[word], b6):
                continue
            b4[word].append(b6)
    if b3 is not None:
        with open(b3, 'w') as out:
            b7 = []
            for word, lemmas in b4.items():
                b7.append(
                    '{}:{}\n'.format(word, ', '.join([fonk2(b6) for b6 in lemmas]))
                )
            out.writelines(b7)
    return b4
def fonk4():
    b8 = fonk3(b1, b2)
    for word, lemmas in b8.items():
        print('Processing word:', word, 'with', len(lemmas), 'lemmas')
fonk4()