b1 = './datasets/hi_hdtb-ud-dev.conllu'
b2 = './outputs/train_data.txt'
def fonk1(existing_lemma, new_lemma):
    return (
        existing_lemma["root"] == new_lemma["root"] and
        existing_lemma["tag1"] == new_lemma["tag1"] and
        existing_lemma["b5"] == new_lemma["b5"]
    )
def fonk2(b6):
    return '[{}, {}, {}]'.format(b6["root"], b6["tag1"], b6["b5"])
def fonk3(input_training_file, b3 = None):
    b4 = {}
    with open(input_training_file, 'r') as hindiFile:
        for line in hindiFile:
            if len(line) < 5 or line[0] == '\n':
                continue
            word, root, tag1, b5 = line.split("\t")[1:5]
            if word not in b4:
                b4[word] = []
            b6 = {
                "root": root,
                "tag1": tag1,
                "b5": b5,
            }
            if not any(fonk1(existing_lemma, b6) for existing_lemma in b4[word]):
                b4[word].append(b6)
    if b3 is not None:
        with open(b3, 'w') as out:
            for word, lemmas in b4.items():
                b7 = ', '.join(fonk2(b6) for b6 in lemmas)
                out.write('{}:{}\n'.format(word, b7))
    return b4
def fonk4():
    b8 = fonk3(b1, b2)
    for word, lemmas in b8.items():
        print('Processing word:', word, 'with', len(lemmas), 'lemmas')
fonk4()