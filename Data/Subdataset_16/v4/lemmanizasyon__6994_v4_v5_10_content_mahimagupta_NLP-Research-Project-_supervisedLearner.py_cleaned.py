b1 = './datasets/hi_hdtb-ud-dev.conllu'
b2 = './outputs/train_data.txt'
def fonk1(lemma1, lemma2):
    return all(lemma1[key] == lemma2[key] for key in ["root", "tag1", "b5"])
def fonk2(lemma):
    return '[{}, {}, {}]'.format(lemma["root"], lemma["tag1"], lemma["b5"])
def fonk3(input_training_file, b3 = None):
    b4 = {}
    with open(input_training_file, 'r') as hindi_file:
        for line in hindi_file.readlines():
            if len(line) < 5 or line[0] == '\n':
                continue
            word, root, tag1, b5 = line.split("\t")[1:1+4]
            if word not in b4:
                b4[word] = []
            b6 = {"root": root, "tag1": tag1, "b5": b5}
            if any(fonk1(existing_lemma, b6) for existing_lemma in b4[word]):
                continue
            b4[word].append(b6)
    if b3 is not None:
        with open(b3, 'w') as out_file:
            b7 = []
            for word, lemmas in b4.items():
                b8 = ', '.join([fonk2(lemma) for lemma in lemmas])
                b7.append(f'{word}:{b8}\n')
            out_file.writelines(b7)
    return b4
def fonk4():
    b9 = fonk3(b1, b2)
    for word, lemmas in b9.items():
        print('Processing word:', word, 'with', len(lemmas), 'lemmas')
fonk4()