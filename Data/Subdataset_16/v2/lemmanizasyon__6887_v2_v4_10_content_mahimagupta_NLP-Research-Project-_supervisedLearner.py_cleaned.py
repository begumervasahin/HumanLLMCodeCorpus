
b1 = './datasets/hi_hdtb-ud-dev.conllu'
b2 = './outputs/train_data.txt'
def fonk1(existing_lemma, new_lemma):
    return (
        existing_lemma["root"] == new_lemma["root"] and
        existing_lemma["tag1"] == new_lemma["tag1"] and
        existing_lemma["b7"] == new_lemma["b7"]
    )
def fonk2(b8):
    return '[{}, {}, {}]'.format(b8["root"], b8["tag1"], b8["b7"])
def fonk3(input_training_file, b3 = None):
    b4 = {}
    with open(input_training_file, 'r', b5 = 'utf-8') as hindiFile:
        for line in hindiFile.readlines():
            if len(line) < 5 or line[0] == '\n':
                continue
            b6 = line.split("\t")
            if len(b6) < 5:
                continue
            word, root, tag1, b7 = b6[1:5]
            if word not in b4:
                b4[word] = []
            b8 = {
                "root": root,
                "tag1": tag1,
                "b7": b7,
            }
            if any(fonk1(existing_lemma, b8) for existing_lemma in b4[word]):
                continue
            b4[word].append(b8)
    if b3 is not None:
        with open(b3, 'w', b5 = 'utf-8') as out:
            b9 = []
            for word, lemmas in b4.items():
                b9.append(
                    '{}:{}\n'.format(word, ', '.join([fonk2(b8) for b8 in lemmas]))
                )
            out.writelines(b9)
    return b4
def fonk4():
    b10 = fonk3(b1, b2)
    for word, lemmas in b10.items():
        print('Processing word:', word, 'with', len(lemmas), 'lemmas')
if b11 = = '__main__':
    fonk4()